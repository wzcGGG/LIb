import hashlib
h = hashlib.sha256()
password = '000000'
h.update(bytes(password, encoding='UTF-8'))
result = h.hexdigest()
# 注释下面一行即可加密
# result = val
print(result)
