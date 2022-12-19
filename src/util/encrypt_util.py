# -*- coding: utf-8 -*-
import base64
import binascii
import binhex
import hashlib

from Crypto.Cipher import AES
from binascii import a2b_hex, b2a_hex


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

    @staticmethod
    def get_key(secret_key=""):
        return AESUtil.add_to_16(secret_key)[0:16]

    @staticmethod
    def add_to_16(text):
        if len(text.encode('utf-8')) % 16:
            add = 16 - (len(text.encode('utf-8')) % 16)
        else:
            add = 0
        text = text + ('\0' * add)
        return text.encode('utf-8')

    # 加密函数
    @staticmethod
    def encrypt(secret_key, text):
        # ECB没有偏移量
        mode = AES.MODE_ECB
        cryptos = AES.new(AESUtil.get_key(secret_key), mode)
        text = AESUtil.add_to_16(text)
        cipher_text = cryptos.encrypt(text)
        return str(b2a_hex(cipher_text), "utf-8")

    # 解密后，去掉补足的空格用strip() 去掉
    @staticmethod
    def decrypt(secret_key, text):
        mode = AES.MODE_ECB
        cryptor = AES.new(AESUtil.get_key(secret_key), mode)
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
    jiami_byte = AESUtil.encrypt(key, origin)

    jiemi = AESUtil.decrypt(key, jiami_byte)

    print(jiemi == origin)

    base64.encode
    base64.decode

    base64.encodebytes  # binascii.b2a_base64(chunk)
    base64.decodebytes  # binascii.a2b_base64(s)

    base64.b64encode
    base64.b64decode

    base64.urlsafe_b64decode
    base64.urlsafe_b64encode

    binascii.a2b_hex
    binascii.b2a_hex
    binascii.a2b_base64
    binascii.b2a_base64

    b = base64.b64encode(b"123")
    ret = base64.b64decode(b)

    # uu.encode()
    # uu.decode()

    binhex.Error
    b'\0'.hex
