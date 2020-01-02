# -*- coding: utf-8 -*-
import base64
import hashlib
from binascii import b2a_hex, a2b_hex

import Crypto.Cipher as Cipher
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_v1_5_cipper
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Signature import PKCS1_v1_5 as PKCS1_v1_5_sign


# base64 SHA256 直接调用
# aes 对称加密
# rsa 非堆成加密

class Base64Util:
    # encodestr = base64.b64encode('abcr34r344r'.encode('utf-8'))
    # print(str(encodestr, 'utf-8'))
    # 加密
    @staticmethod
    def enc_bytes(text):
        return base64.b64encode(text.encode("utf-8"))

    # 解密
    @staticmethod
    def dec_bytes(text):
        return str(base64.b64decode(text), "utf-8")


class SHA256Util:
    """
        哈希加密使用sha256
    """
    @staticmethod
    def sha256_salt(key, value):
        """
        sha256加密
        return:加密结果转成16进制字符串形式
        """
        hsobj = hashlib.sha256(key.encode("utf-8"))
        hsobj.update(value.encode("utf-8"))
        return hsobj.hexdigest()


class AESUtil:
    def __int__(self):
        self.key = get_random_bytes(16)

    def add_to_16(self, text):
        if len(text.encode('utf-8')) % 16:
            add = 16 - (len(text.encode('utf-8')) % 16)
        else:
            add = 0
        text = text + ('\0' * add)
        return text.encode('utf-8')

    # 加密函数
    def encrypt(self, text):
        # ECB没有偏移量
        mode = AES.MODE_ECB
        text = self.add_to_16(text)
        cryptos = AES.new(self.key, mode)
        cipher_text = cryptos.encrypt(text)
        return str(b2a_hex(cipher_text), "utf-8")

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        mode = AES.MODE_ECB
        cryptor = AES.new(self.key, mode)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')


class RsaUtil:
    """RSA加解密签名类
    """

    def __int__(self, ciper_lib=PKCS1_v1_5_cipper, sign_lib=PKCS1_v1_5_sign, hash_lib=SHA1,
                pub_file=None, pri_file=None, pub_skey=None, pri_skey=None, pub_key=None, pri_key=None,
                reversed_size=11):

        # 加解密库
        self.ciper_lib = ciper_lib
        self.sign_lib = sign_lib
        self.hash_lib = hash_lib

        # 公钥密钥
        if pub_key:
            self.pub_key = pub_key
        elif pub_skey:
            self.pub_key = RSA.importKey(pub_skey)
        elif pub_file:
            self.pub_key = RSA.importKey(open(pub_file).read())

        if pri_key:
            self.pri_key = pri_key
        elif pri_skey:
            self.pri_key = RSA.importKey(pri_skey)
        elif pri_file:
            self.pri_key = RSA.importKey(open(pri_file).read())

        # 分块保留长度
        self.block_reversed_size = reversed_size

    # 根据key长度计算分块大小
    def get_block_size(self, rsa_key):
        try:
            # RSA仅支持限定长度内的数据的加解密，需要分块
            # 分块大小
            reserve_size = self.block_reversed_size
            key_size = rsa_key.size_in_bits()
            if (key_size % 8) != 0:
                raise RuntimeError('RSA 密钥长度非法')

            # 密钥用来解密，解密不需要预留长度
            if rsa_key.has_private():
                reserve_size = 0

            bs = int(key_size / 8) - reserve_size
        except Exception as err:
            print('计算加解密数据块大小出错', rsa_key, err)
        return bs

    # 返回块数据
    def block_data(self, data, rsa_key):
        bs = self.get_block_size(rsa_key)
        for i in range(0, len(data), bs):
            yield data[i:i + bs]

    # 加密
    def enc_bytes(self, data, key=None):
        text = b''
        try:
            rsa_key = self.pub_key
            if key:
                rsa_key = key

            cipher = self.ciper_lib.new(rsa_key)
            for dat in self.block_data(data, rsa_key):
                cur_text = cipher.encrypt(dat)
                text += cur_text
        except Exception as err:
            print('RSA加密失败', data, err)
        return text

    # 解密
    def dec_bytes(self, data, key=None):
        text = b''
        try:
            rsa_key = self.pri_key
            if key:
                rsa_key = key

            cipher = self.ciper_lib.new(rsa_key)
            for dat in self.block_data(data, rsa_key):
                if type(self.ciper_lib) == Cipher.PKCS1_OAEP:
                    cur_text = cipher.decrypt(dat)
                else:
                    cur_text = cipher.decrypt(dat, '解密异常')
                text += cur_text
        except Exception as err:
            print('RSA解密失败', data, err)
        return text

    # RSA签名
    def sign_bytes(self, data, key=None):
        signature = ''
        try:
            rsa_key = self.pri_key
            if key:
                rsa_key = key

            h = self.hash_lib.new(data)
            signature = self.sign_lib.new(rsa_key).sign(h)
        except Exception as err:
            print('RSA签名失败', '', err)
        return signature

    # RSA签名验证
    def sign_verify(self, data, sig, key=None):
        try:
            rsa_key = self.pub_key
            if key:
                rsa_key = key
            h = self.hash_lib.new(data)
            self.sign_lib.new(rsa_key).verify(h, sig)
            ret = True
        except (ValueError, TypeError):
            ret = False
        return ret


if __name__ == '__main__':
    data = SHA256Util.sha256_salt("11", "2")
    print(data)
    SHA256Util.enc_bytes()
