swapped = True
while swapped:
    swapped = False
    for i in range(len(myList)-1):
        if myList[i] > myList[i+1]:
            swapped = True
            myList[i],myList[i+1] = myList[i+1],myList[i]
        
print(myList)
