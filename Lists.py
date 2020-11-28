l1 = [1,4,3,2,9,16,5,8,34,98]
print("This is a list",l1)
l1.append(10)
print("This is list in which 10 is appended",l1)
l1.insert(5,16)
print("This is a list in which 5 and 16 is inserted",l1)
l1.sort()
print("This is a sorted list :",l1)
l1.reverse()
print("This is a reversed list",l1)
l1.pop(5)
print("This ia alist in which 9 index number is removed",l1)
l1.remove(16)
print("In this list 16 is removed from the list",l1)
print("This list will only print the value which is at 7 index and value is : ",l1[7])


#  Input from user in list
f1 = input("Enter fruit number 1")
f2 = input("Enter fruit number 2")
f3 = input("Enter fruit number 3")
f4 = input("Enter fruit number 4")
f5 = input("Enter fruit number 5")
f6 = input("Enter fruit number 6")
f7 = input("Enter fruit number 7")

myFruitlist = [f1,f2,f3,f4,f5,f6,f7]

myFruitlist.sort()
print(myFruitlist)
myFruitlist.reverse()
print(" The reversed list is",myFruitlist)