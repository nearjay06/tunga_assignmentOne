# Question One
# Write a Python program which accepts the radius 
# and height from the user and computes the volume
# of a cylinder. Formula is: 3.14 x radius x radius x height 
def calc_volume():
    vol = 3.14*radius*radius*height
    
    pi = 3.14 
    c = input("Enter radius here: ")
    d = input("Enter height here: ")

    volume = f"{'pi'}*{'c'} * {'c'}* {'d'}
    print ("volume is:", volume)



# Question Two
a = [2,3,4,5,6,7]
print (a[:0] + a[3:])




#Question three

s = ['a','b','c','d']
for items in s:
    if items == len(s):
        print (s)
    else:
        print ('invalid position')


#Question four
input = [1,2,3,4,5,6,7]
print (sum(input))


#Question five
def largest_number(b):
    b = (1,2,3,4,5,6)
    for items in b:
        if b >1 and b < 8:
            print (b)
        else:
            print('invalid')



