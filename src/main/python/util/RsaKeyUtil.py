# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/24 15:23
"""

from Crypto import Random
from Crypto.PublicKey import RSA

# 利用伪随机数来生成私钥和公钥
random_generator = Random.new().read

rsa = RSA.generate(2048, random_generator)

private_pem = rsa.exportKey()

f = open('MY_KEY1_pri.pem', 'w')
f.write(str(private_pem, "utf-8"))
f.close()

public_pem = rsa.publickey().exportKey()
f = open('MY_KEY1_pub.pem', 'w')
f.write(str(public_pem, "utf-8"))
f.close()

######################################################

# 利用默认的generate来生成私钥和公钥
rsa = RSA.generate(2048)
private_pem = rsa.exportKey('PEM')
f = open('MY_KEY2_pri.pem', 'w')
f.write(str(private_pem, "utf-8"))
f.close()

public_pem = rsa.publickey().exportKey()
f = open('MY_KEY2_pub.pem', 'w')
f.write(str(public_pem, "utf-8"))
f.close()

######################################################

# 根据已有的RSA私钥来生成公钥
f = open('MY_KEY2_pri.pem', 'r')
rsa = RSA.importKey(f.read())
f.close()

public_pem = rsa.publickey().exportKey()
f = open('MY_KEY3_pub.pem', 'w')
f.write(str(public_pem, "utf-8"))
f.close()

######################################################

# # 根据已有的RSA PEM格式的私钥来转换成DER格式的私钥
# f = open('MY_KEY2_pri.pem', 'r')
# rsa = RSA.importKey(f.read())
# f.close()
#
# private_der = rsa.exportKey('DER')
# f = open('MY_KEY3_pri.der', 'w')
# f.write(str(private_der,"ascii"))
# f.close()
