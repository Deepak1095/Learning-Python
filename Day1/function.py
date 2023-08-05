# add two Numbers
def addNum(a,b):
    return a+b

res = addNum(4,6)

print(res)

# Add all elements of list

def listSum(list):
    total=0
    for num in list:
        total+=num
    return total

list=[1,2,3,4,5,6,7]

res = listSum(list)

print(res)