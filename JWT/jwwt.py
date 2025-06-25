import jwt
key = "secret"
encode_jwt = jwt.encode({'some': 'Payload'}, key, algorithm="HS256") 
decode_jwt = jwt.decode(encode_jwt, key, algorithms="HS256")

print(encode_jwt)
print(decode_jwt)