filename = input ("Please enter the name of the file: ")
fin = open( filename + ".txt", "r")
fullText = fin.read()
words = fullText.split(' ')
print (words)
for x in words:
    if len(x) > 3:
        print (x, "--> ", x[1:]+x[0]+"ay")
fin.close()

print("\n \n \n ")
input('Press ENTER to exit')