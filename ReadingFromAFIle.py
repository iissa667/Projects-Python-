
print("Options")
print("1. Print the numbers")
print("2. Print the length of the list")
print("3. Print the max (without using the built in max function)")
print("4. Print the average")
print("5. Print the 2 – 5 number in the list – if the list is long enough to support positions 2-5")
print("6. Quit")

user = int(input("Enter an Option: "))

def readInFile(): 
      arr_intValues = [] 
      myFile = open("C:\\Users\\ACC\\Desktop\\CIS 115\\RandomNum.txt") 
      
      for myLine in myFile: 
            arr_intValues.append(int(myLine)) 
      return arr_intValues

def avgList(myNewList): 
      s = 0 
      for n in myNewList: 
            s += n

      avg = s/len(myNewList) 
      print(avg)

myNewList = readInFile()

while user <=5:
      if user == 1:
            print(myNewList)

      if user == 2:
            print(len(myNewList))
            
      if user == 3:
            print(max(myNewList))

      if user == 4:
            print(avgList(myNewList))

      if user == 5:
            print(myNewList[2:5])

      if user ==6:
            print()

      
      print("Options")
      print("1. Print the numbers")
      print("2. Print the length of the list")
      print("3. Print the max (without using the built in max function)")
      print("4. Print the average")
      print("5. Print the 2 – 5 number in the list – if the list is long enough to support positions 2-5")
      print("6. Quit")
      user = int(input("Enter an Option: "))

      
