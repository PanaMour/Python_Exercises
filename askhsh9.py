usernum = input ("Enter a number: \n")
check = False
while check == False: #checks if user input is an integer
    if usernum.isdigit():
        check == True
        break
    else:
        print ("Invalid Input.Please enter another number.")
        usernum = input ("Enter a number: \n")
intusernum = int(usernum)
print ("The number you entered is: ", intusernum , "\n")
a = intusernum * 3
print ("The number you entered multiplied by 3 is: ", a , "\n")
a = a + 1
print ("The number you entered multiplied by 3 and raised by 1 is: ", a , "\n")
dlist = [int(d) for d in str(a)]
print ("The list containing this number's digits is ", dlist, "\n")
num = 0
while len(dlist) > 1:
    for x in dlist:
        num = x + num
    print ("The digits added together equal to ", num, "\n")
    dlist.clear()
    dlist = [int(d) for d in str(num)]
    print ("The list containing this number's digits is ", dlist, "\n")
    if len(dlist) > 1:
        num = 0
print ("The single-digit number you are looking for is: ", num , "\n")
input('Press ENTER to exit')