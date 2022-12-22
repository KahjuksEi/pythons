myDict = {
    "Apple": {"Price": 2, "Quantity": 100},
    "Pear": {"Price": 3, "Quantity": 400},
    "Kiwi": {"Price": 5, "Quantity": 60},
}

summaryGoods = 0
summaryQuantities = 0

def userInputs():
    inputName = input("Enter product: ")
    inputPrice = int(input("Enter price: "))
    inputQuantity = int(input("Enter quantity: "))
    myDict[inputName] = {"Price": inputPrice, "Quantity": inputQuantity}

userInput = input("Do you wanna to add new goods (y/n)")
if userInput.lower() == 'y':
    userInputs()
    userElseInput = input("Do you wanna to add one more (y/n)")
    while userElseInput.lower() == 'y':
        userInputs()
        userElseInput = input("Do you wanna to add one more (y/n)")       

for i in myDict:
    print(i, "-", "Price:", myDict[i].get('Price'), "-", "Quantity:", myDict[i].get('Quantity'))
    summaryGoods += myDict[i].get('Price')
    summaryQuantities += myDict[i].get('Quantity')
print("All products:", summaryGoods, "-", "Total quantity:", summaryQuantities)