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

# Write a program to display only those numbers from a list that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

def fun(list):
    for num in list:
        if(num>500):
            break
        elif(num>150):
            continue
        elif(num%5==0):
            print(num)


fun(numbers)


