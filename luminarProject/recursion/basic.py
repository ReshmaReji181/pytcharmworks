# recursion  -function call itself

# def printhi():
#     print("hi")
#     printhi()
# printhi()




# sum of n

def findsum(n):
    if n==1:
        return 1
    else:
        return n+findsum(n-1)
print(findsum(3))