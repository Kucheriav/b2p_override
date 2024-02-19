import hashlib

file = open('02002090-06-000113-001-20240214.b2p').read()

# for j in range(100):
#     for i in range(1000):
#         this_file = file[i:-j].encode()
#         result = hashlib.md5(this_file)
#         if str(result.hexdigest()) == '4F58CEF165CD94665198AC1026713A73':
#             print(i)

print(file[200:600].encode())