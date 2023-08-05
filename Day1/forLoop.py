
# normal for loop

for i in range(10):
    print(i)


# print element from string

str = "hello world"

for i in str:
    print(i)

# nested loop

for i in range(5):
    for j in range(i+1):
        print("*",end=(" "))
    print()