# -*- coding: utf-8 -*-
import base64
import binhex
import hashlib

from Crypto.Random import get_random_bytes
from binascii import a2b_hex, b2a_hex

from Crypto.Cipher import AES


# base64 SHA256 直接调用
# aes 对称加密
# rsa 非堆成加密

class Base64Util:
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
    def sha256_salt(value, salt):
        """
        sha256加密
        return:加密结果转成16进制字符串形式
        """
        hsobj = hashlib.sha256(salt.encode("utf-8"))
        hsobj.update(value.encode("utf-8"))
        return hsobj.hexdigest()


class AESUtil:
    def __int__(self):
        self.key = get_random_bytes(16)

    @staticmethod
    def add_to_16(text):
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


if __name__ == '__main__':
    # js base64编码
    # window.btoa('china is so nb') # 'Y2hpbmEgaXMgc28gbmI='
    # base64.encodebytes 编码会多出换行符
    origin = 'china is so nb'
    b = base64.b64encode(origin.encode('utf8'))
    s = str(b, encoding="utf8")
    print(s == "Y2hpbmEgaXMgc28gbmI=")

    s = str(base64.b64decode(b), encoding="utf8")
    print(s == origin)

    key = "123456"
    key_16 = AESUtil.add_to_16(key)
    aes = AES.new(key_16, AES.MODE_ECB)

    text_to16 = AESUtil.add_to_16(origin)
    jiami_byte = aes.encrypt(text_to16)

    jiemi = aes.decrypt(jiami_byte)

    print(jiemi == text_to16)

    base64.encode
    base64.decode

    base64.encodebytes  # binascii.b2a_base64(chunk)
    base64.decodebytes  # binascii.a2b_base64(s)

    base64.b64encode
    base64.b64decode

    base64.urlsafe_b64decode
    base64.urlsafe_b64encode

    b = base64.b64encode(b"123")
    ret = base64.b64decode(b)

    # uu.encode()
    # uu.decode()

    binhex.Error
