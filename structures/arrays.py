myArray = [1,2,3,4]

print(myArray[0])

#Traversing through an array:
for i in range(len(myArray)):
    print(myArray[i])

i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1

#Delete an array at the end of an array:
def removeElement(arr, length):
    if length > 0:
        arr[length-1] = 0

#Delete an element in between the array:
def removeMiddle(arr, i, length):
    for index in range (i+1, length):
        arr [index-1] = arr[index]

#Insert a value at the end of the array:
def insertEnd(arr, val, length):
    arr[length]=val

#Insert a value inbetween the array:
def insertMiddle(arr, i, val, length):
    for index in range(length-1, i-1, -1 ):
        arr[index + 1] = arr[index]
    arr[i] = val