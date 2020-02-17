#The products available for purchase
goods = {
  "milk": 1.1,
  "sugar": 2.2,
  "eggs" : 0.5,
  "ham": 2.0
}

def computebill(x,y): #function that calculates the bill depending on the products that the user buys and the VAT he chooses
  total = 0
  for i in x:
    total = goods[i] + total
  fsum = total + total * y
  print ("The total sum is",fsum)

print("####################################################################################################")
print("The available products with their prices are:", goods)
print("####################################################################################################")
print ("\n")
buy = []

product = input ("Please enter a product you bought:\n")
while product!="stop":
  if product in goods.keys():
    buy.append(product)
    print ("The products you have bought are:", buy)
    product = input ("Please enter a product you bought or type stop to see your total:\n")
  else:
    print ("No such product is available")
    if buy!=[]:
      print ("The products you have bought are:", buy)
    product = input ("Please enter a product you bought or type stop to see your total:\n")

check = False
while check == False: #checks if user input is a number
  try:
    vat = float(input ("Please enter the Value Added Tax:"))
    check = True
  except ValueError:
    print ("Invalid input")

computebill(buy, vat)

input('Press ENTER to exit')