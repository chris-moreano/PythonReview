# create empty list
mylist = []

# ask user for input numbers until hotkey is pressed

controlNumber = True

# Populate list
while controlNumber == True:
	tempVar = input("Enter a number to add to list or enter nothing to exit\n")

	if tempVar == "":
		controlNumber = False
		print("Exiting while loop")

	else:
		mylist.append(int(tempVar))

# Add all numbers 
sumofList = 0;
for numbers in mylist:
	sumofList = sumofList + numbers

print("List total = ", sumofList)


fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]

print "Good bye!"