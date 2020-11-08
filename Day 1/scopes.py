# LEGB --- local enclosing global builtin

# n = "15"

# def test(): 
#     print(type(int(n)))

# test()
# print(type(n))





n = 5

print("let me start")


try:
    print(n/0)
except:
    print("some error occured in division")


print(n)

print("hello i am ending")


