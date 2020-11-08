# def isodd(n):
#     if(n%2!=0):
#         return True
#     else:
#         return False


# n = isodd(5)

# print(isodd(6))

# print(isodd(9))



def cube(n):
    ans = []
    for i in range(1, n+1):
        c = i ** 3
        ans.append(c)
    return ans

print(cube(51))
print(cube(5))


# def test():
#     return 5, 6

# a, b = test()
# print(a, b)


# def test():
#     print("hello world")


# print(test())

# def test():
#     print("hello")

# print(type(test()))