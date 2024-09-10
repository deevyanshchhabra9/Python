# Data types in python

x=5 #int type

y=5.5 # float dtype

z = 3e6 # 3*10^6 e repesent to the power 10 

complex1 = 4 + 5j # this how we can represnt complex in python
print(complex1)

print(type(y))  # to finf which type of dtype

print(abs(-5)) # will return 5

print(pow(2,3)) # means 2^3

print(round(4.73))

nums = [3,12,33,33,99]

print(max(nums))
print(min(nums))


# list data types
# list can hv multiple dtypes but we should prefer single dtype in one list
# mutable

students = ["Mohan","Deevyansh","Radha"]   #WAY 1 OF CREATING LIST USING SQUARE BRACKET NOTTATION
print(students)
print(type(students))

list2 = list(students)       # WAY 2 OF CREATING LIST USING LIST CONSTRUCTOR
print(list2)

list3 = list("deevyansh")
print(list3)


list4 = (3,4,"vishwah");
print(list4)

# Aceesing elements of list they arfe indexed from 0

li=[1,2,3,44,99]
print(li[0]) # will give me 1 as 1 is indexed at 0

# aceesing listm using -ve indexing

print(li[-1])
# -ve ranges from(-lenghth,-1)

# inserting elements in list

arr = [1,3,4,5,8]

# adding element at end of list
arr.append(11)  # add 11 at last of list
print(arr)

# adding elemnt at specific index
arr.insert(3,5)  # at index 3 i want to add 5 everything else would be shifted to right
print(arr)

#this proves list is mutable or arr is mutable

# creating a list from another list

l1 = [1,2]
l2 = ["Deevyansh","Chhabra"]
l1.extend(l2) # we are putting or basically extending l1 with the help of l2   
print(l1)

# Removing elements from the list

# removing elemts using reove method

l5 = [1,2,3,4,55,33,55]
l5.remove(55) # it will remove first ocuurence of 55 
print(l5)

# removing elemts using pop method

l5.pop()  # will remove last elemts from list
print(l5)

l5.pop(1) # reomoving element from index 1
print(l5)  # 2 would be removed

# replacing value in list

l6 = [33,44,5,6,7,8]
l6[1]=22 # replacing 44 with 22
print(l6)

# replacing elements in a range

l7 = [33,99,88,11,22,55]
# relplacing elemts bw 99 to 11 so our indexing would be 1:4 # this would include elemets bw indexing of 1 to 3
l7[1:4] = "d","q","r"
print(l7)

# suppose i hv defined range that i hv to relace 3 elemts but i only give d q so only 99 will bw relace by d 88 with q 11 will be deleted

# lets check

l8 = [33,99,88,11,22,55]
l8[1:4] = "d","q"
print(l8) # yes 11 is deleted

# reversing list

l8.reverse()
print(l8)

# creating copy

l10 = [1,2,3,4]
l10_copy= l10.copy()
print(l10_copy)  # all elemts would be same as in l10

# but their adress would be totally different

print(id(l10))
print(id(l10_copy))

# sort method 

l13 = [99, 88, 5, 101]

l13.sort() # will sort your list in ascending order

print(l13)

