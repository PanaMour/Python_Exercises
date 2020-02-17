fin = open( "lists.txt", "r")
l = []
for line in fin:
    l.append(line.rstrip().split(','))
fin.close()
mylist = [None] * 6
fourlist = [None] * 4
i=0
check = False
while i < 6:
    element = input ("Please enter a list containing 6 numbers in descending order by typing each number one at a time: ")
    while check == False: #checks if user input is an integer
        if element in mylist:
                print ("You can't have the same number twice in your list.")
                element = input ("Please enter a list containing 6 numbers in descending order by typing each number one at a time: ")
        elif element.isdigit():
            check == True
            break
        else:
            print ("Invalid Input.Please enter your", i+1 ,"number.")
            element = input ("Please enter a list containing 6 numbers in descending order by typing each number one at a time: ")
    mylist[i] = element
    while i<4:
        fourlist[i] = element
        break
    i=i+1
print ("\nThe 6-digit list you entered is: ", mylist, "\n")
copylist = fourlist #copies the starting list that the user input into a backup list for later use

#Checks by descending order the 6-digit list and informs the user if the list is available in the file
x = 0   #first digit that can take value from mylist[0]-mylist[2]
y = 1   #second digit that can take value from mylist[1]-mylist[3]
z = 2   #third digit that can take value from mylist[2]-mylist[4]
w = 3   #fourth digit that can take value from mylist[3]-mylist[5]
while x<3:
    if w>=6: #since the fourth digit can take value up to mylist[5] when it becomes 6
        fourlist = copylist # the list resets to the starting list
        z=z+1   #the 3rd digit's value now contains the next element of the 6-digit list (mylist[z+1])
        w=z+1   #the 4rth digit's value contains the element after the 3rd digit's value
    if z>=5:
        y=y+1
        z=y+1
        w=z+1
    if y>=4:
        x=x+1
        y=x+1
        z=y+1
        w=z+1
    if x>=3: #the first digit can take value op to mylist[2] so when it becomes 3 there are no more combinations to check
        print ("There is no 4-digit combination available with the given numbers. Please enter another list. \n")
        break   #stops the loop
    fourlist[0] = int(mylist[x])
    fourlist[1] = int(mylist[y])
    fourlist[2] = int(mylist[z])
    fourlist[3] = int(mylist[w])
    
    fourlist = sorted(fourlist)#I convert the elements to integers so that the sorting is done properly and then convert them back to strings

    fourlist[0] = str(fourlist[0])
    fourlist[1] = str(fourlist[1])
    fourlist[2] = str(fourlist[2])
    fourlist[3] = str(fourlist[3])
    if fourlist in l:
        print ("The 4-digit list",fourlist,"is not available. \n")
        w = w+1 #increases the 4th digit's value by one element in the 6-digit list
    else:
        print ("The 4-digit list",fourlist,"is available.\n") #if the combination is not in the list then one of the 4-digit combinations is available for use
        break

input('Press ENTER to exit')
