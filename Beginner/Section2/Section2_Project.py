print("welcome! let's calculate tip")

bill = float(input("how much is the bill?\n"))
tipPercentage = int(input("what percentage tip you wanna give?\n"))
peopleNumber = int(input("how many people is the bill split between\n"))

totaltip = (tipPercentage * bill)/100
tipPerPerson = totaltip / peopleNumber

print(tipPerPerson)