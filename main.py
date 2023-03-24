from hashlib import *

Hash_algorithms = [md5, sha1, sha224, sha256, sha384, sha512]
HashListStr =  ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
result = ""
# =================================
print("select yor type Hash")
for i in HashListStr:
    print("|",i, end=" ")
print('|')

select = input("-->")
while select not in HashListStr:
    print("your type not defined!")
    select = input("-->")
# =================================
text = input("your text: ")

for i in range(Hash_algorithms.__len__()):
    if select == HashListStr[i]:
        result = Hash_algorithms[i](text.encode())
        break

print(result.hexdigest())
