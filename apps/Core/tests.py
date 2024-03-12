# print(1)
# try:
#     raise ValueError('Привет')
#     print(3)
# except Exception:
#     print(2)
def x(**u):
    print(u)


print(x(a=1, b='AAAA', username='ASDASD'))
