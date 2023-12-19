# a = 4.5
# b = 2
# c = a * b
# print("hello " + str(c))
# print(2 != 5)
# l = ['octopus', 'whale', 'dolphin']
# l.append('seahorse')
# l.remove(l[1])
# print(l)
# print(len(l))
# age = input("enter your age: ")
# print("Double your age is " + str(2 * int(age)))

# a = 6
# b = 6
# if a > b:
#     print("a is greater")
# elif a < b:
#     print("b is greater")
# else:
#     print("a is equal to b")

# l = [3, 4, 12, 53]
# for num in l:
#     print(num)

# for i in range(2, 14, 3):
#     print(i)

# count = len(l)
# for i in range(count):
#     print(l[i])

#print first one, skip the second one, print third one, leave loop before printing last one
# count = len(l)

# for i in range(count):
#     if i == 0 or i == 2:
#         print(l[i])
#     elif i == 1:
#         break

# z = [46, 612, 44, 305, 487]
# total = 0

#indices of list
# count = len(z)
# for i in range(count):   
#     total += z[i]

# actual items in list
# for num in z: 
#     total += num

# average = total / 5
# print(average)

# def calculateArea(base, height):
#     area = base * height
#     return area

# a = calculateArea(2, 4)
# print(a)

# import math

# b = math.sqrt(25)
# print(b)

x = 0
y = 0
while x < 2:
    y = 0
    while y < 4:
        print(y)
        y = y + 1
    x = x + 1