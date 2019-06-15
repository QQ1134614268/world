"""
@author:huangran
"""
import jwt


import base64
herder={
  "alg": "HS256",
  "typ": "JWT"
}
encodestr = base64.b64encode(herder.__repr__().encode('utf-8'))
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
print(encodestr)

payload={ "iss": "Online JWT Builder",
  "iat": 1416797419,
  # "exp": 1448333419,
  # "aud": "www.gusibi.com",
  "sub": "uid",
  "nickname": "goodspeed",
  "username": "goodspeed",
  "scopes": [ "admin", "user" ]
}
encodestr = base64.b64encode(payload.__repr__().encode('utf-8'))
# eydpc3MnOiAnT25saW5lIEpXVCBCdWlsZGVyJywgJ2lhdCc6IDE0MTY3OTc0MTksICdleHAnOiAxNDQ4MzMzNDE5LCAnYXVkJzogJ3d3dy5ndXNpYmkuY29tJywgJ3N1Yic6ICd1aWQnLCAnbmlja25hbWUnOiAnZ29vZHNwZWVkJywgJ3VzZXJuYW1lJzogJ2dvb2RzcGVlZCcsICdzY29wZXMnOiBbJ2FkbWluJywgJ3VzZXInXX0
print(encodestr)
encoded_jwt = jwt.encode(payload, 'secret', headers=herder,algorithm='HS256')
# b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE0MTY3OTc0MTksInN1YiI6InVpZCIsIm5pY2tuYW1lIjoiZ29vZHNwZWVkIiwidXNlcm5hbWUiOiJnb29kc3BlZWQiLCJzY29wZXMiOlsiYWRtaW4iLCJ1c2VyIl19.nuR24_D7HoHB_zufV0uEXaBu-ewVy85STe5WEJGS5Eg'
# b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE0MTY3OTc0MTksInN1YiI6InVpZCIsIm5pY2tuYW1lIjoiZ29vZHNwZWVkIiwidXNlcm5hbWUiOiJnb29kc3BlZWQiLCJzY29wZXMiOlsiYWRtaW4iLCJ1c2VyIl19.nuR24_D7HoHB_zufV0uEXaBu-ewVy85STe5WEJGS5Eg'

print(encoded_jwt)
decode=jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])
print(decode)