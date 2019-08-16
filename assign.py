# # Question One

radius = float(input("Enter the radius"))
height = float(input("Enter the height"))

volume = 3.14*(radius**2)*height
print(volume)

def calc_volume():
    radius = float(input("Enter the radius"))
    height = float(input("Enter the height"))
    return 3.14*(radius**2)*height

print(calc_volume())

def calVolume(radius,height):
    return 3.14*(radius**2)*height
print (calVolume(radius = float(input("Enter the radius"), height = float(input("Enter the height")))))

# def calc_volume():
#     vol = 3.14*radius*radius*height
    
#     pi = 3.14 
#     c = input("Enter radius here: ")
#     d = input("Enter height here: ")

#     volume = f"{'pi'}*{'c'} * {'c'}* {'d'}
#     print ("volume is:", volume)

# Question Two
myList = [5,6,8,9,5,32]
for index in range(len(myList)):
    if len(myList)> 1:
        removedItem = myList.pop(1)
        print(removedItem)

# a = [2,3,4,5,6,7]
# print (a[:0] + a[3:])


#Question three

name = 'abcd'
for i in range(len(name)):
    print (1, name[i])

# s = ['a','b','c','d']
# for items in s:
#     if items == len(s):
#         print (s)
#     else:
#         print ('invalid position')  

#Question four

total = 0
for item in myList:
    total = total + item

# input = [1,2,3,4,5,6,7]
# print (sum(input))


#Question five
def largest(*numbers):
    largeNum = 0
    for item in numbers:
        if item > largeNum:
            largeNum = item

    return largeNum

print(largest(23,67,889,999,4))

# def largest_number(b):
#     b = (1,2,3,4,5,6)
#     for items in b:
#         if b >1 and b < 8:
#             print (b)
#         else:
#             print('invalid')




