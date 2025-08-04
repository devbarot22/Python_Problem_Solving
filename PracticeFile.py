# age = int(input("enter your age: "))

# verification = ("You can vote", "You can't vote") [age<=18]

# verify = ("False", "True") [age<18]

# print(verification)
# print(verify)


# age = int(input("enter age:"))

# verifyVotingRight = "can vote" if age > 18 else "can't vote"

# print(verifyVotingRight)


# salary = float(input("enter salary:"))

# calc = salary*(0.1, 0.2) [salary>50000]

# print(calc)


# num1, num2 = int(input("Enter number1:")), int(input("enter number2:"))

# def sum(*args):
#   return __builtins__.sum(args)

# print(sum(num1, num2))

# squareSide = int(input("enter the side:"))

# def squareArea(squareSide):
#   return squareSide*squareSide

# print(squareArea(squareSide))


# flt1, flt2 = float(input("enter num 1:")), float(input("enter num 2:"))

# def avg(*args):
#   return __builtins__.sum(args)/len(args)

# print(avg(flt1, flt2))


# a,b = int(input("enter num:")), int(input("enter num:"))

# # verify = "True" if a >= b else "false"
# verify = ("false", "true") [a >= b]

# print(verify)

# str = "Hi! there how are you!"

# vl = str[:4]
# l = len(vl)
# print(l)


# print(vl)


# userName = input("Enter Your Name:")

# print(len(userName))


# number = int(input("Enter a Number:"))

# if number % 7 == 0:
#   print("Number multiple of 7.") 
# else:
#   print("Number not multiple of 7.")


# print(("Odd", "Even") [number%2==0])

# if number1 > number2:
#   print("Number 1 is greater")
# elif number2 > number3:
#   print("Number 2 is greater")
# else:
#   print("Number 3 is greater")

# numbers = [12, 32, 43, 54, 65, 76, 87, 9, 8, 54]
# for number in numbers:
#   print(number)

# listt = []

# for i in range(3):
#   Movies = input("Enter Your Top 3 Favourite Movies:")
#   listt.append(Movies)

# print(listt)

# list1 = [1, 2, 1]
# list2 = [1, 2, 3, 4]

# copy_list1 = list1.copy() 

# copy_list1.reverse()

# copy_list2 = list2.copy()

# copy_list2.reverse()


# if copy_list2 == list2:
#   print("Its Palindrome")
# else:
#   print("Its not Palindrome")


# tup = ("A", "B", "C", "A", "B", "O", "P", "V", "S")

# list1 = list(tup)

# list2 = sorted(list1, reverse=True)

# print(list2)

# A_Graders = tup.count("A")

# print("Total",A_Graders,"Students Are there who has scored A grade")


# dict1 = {
#   "name": "Dev",
#   "subs":{"sub1":"Math", "sub2":"Science"}
# }

# dict1.get("subs")
# print(dict1["subs"]["sub1"])



# dict1 = {}

# for i in range(2):
#   key = input("Enter key:")
#   value = input("Enter a value for {}:".format(key))
#   dict1.update({key:value})

# print(dict1)

# i = 100
# while i >= 1:
#   print("Printing this....{}".format(i))
#   i-=1

# n = int(input("Enter Number:"))
# # i = 1 
# for i in range(n):
#   print(i)

# i = 0
# n = int(input("Enter the Number:"))

# for i in range(100):
#   print(i*n)


# i = 0
# n = int(input("Enter a number:"))

# while i <= 10:
#   print(n*i)
#   i+=1

# list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for list in list1:
#   print(list)

# ind = 0

# while ind < len(list1):
#   print(list1[ind])
#   ind+=1

# tup = (1, 3, 2, 5, 4, 16, 95, 20, 50)
# lst = list(tup)

# i=0
# while i < len(lst)-1:
#   if lst[i] > lst[i+1]:
#     temp = lst[i]
#     lst[i] = lst[i+1]
#     lst[i+1] = temp
#   i += 1

# print(lst)
# tup = tuple(lst)
# print(tup)


# index = 0

# searchingX = int(input("Enter a number to search in this tuple:"))

# while index < len(tup):
#   if searchingX == tup[index]:
#     print("Found number {} sitting on index {}".format(searchingX, index))
#     break
#   index+=1

# print(index)
# if searchingX != tup[index-1]:
#   print("No matching number.")


# i = 0

# while i < 10:
#   if (i == 3):
#     i += 1
#     continue
#   print(i)
#   i+=1



# dit = {
#   "key": "Value",
#   "Key1": "Value1"
# }

# for keys, values in dit.items():
#   print(keys, values) 

# lit = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for val in lit:
#   print(val)

# for i in range(100, 0, -1):
#   print(i)

# i = 1
# n = int(input("Enter number:"))
# summed = 1
# while (i <= n):
#   summed = summed * i
#   i+=1


# print(summed)

# summed = 1
# for i in range(1, 6):
#   summed *= i

# print(summed)



# def avg(*numbers):
#   print(type(numbers))
#   sum = 0
#   for number in numbers:
#     print(type(number))
#     # sum += number

#   avg = sum/len(numbers)
#   return avg

# print(avg([1, 3, 5, 3, 6]))



# def listLenPrint(arg):
#   print(type(arg))
#   print(len(arg))


# listLenPrint([1, 3, 4, 5, 6, 64, 43, 24, 56])



# def listPrint(arg):
#   for number in arg:
#     print(number, end="")


# listPrint([1, 3, 4, 5, 6, 64, 43, 24, 56])


# def factN(n):
#   fact = 1
#   for i in range(1, n+1):
#     fact *= i
#   return fact


# print(factN(5))


# def convertUSDtoINR(USD):
#   return USD*87.23

# print(convertUSDtoINR(8))


# def returnEvenOdd(number):
#   if number%2 == 0:
#     print("Even")
#   else:
#     print("Odd")


# returnEvenOdd(657353421)



# def see(n):
#   if n == 0:
#     return
#   print(n)
#   see(n-1)

# see(9)


# def fact(n):
#   if n==1 or n == 0:
#     return 1
#   return fact(n-1)*n

# print(fact(4))


# def fact(n):
#   if(n == 0 or n == 1):
#     return 1
#   return fact(n-1) * n


# print(fact(6))


# def printList(list, idx=0):
#   if idx == len(list):
#     return
#   print(list[idx])
#   printList(list, idx+1)

# listt = [1, 2, 4, 5, "Jai ho", "Whassup", 10]

# printList(listt)



# f = open("file.txt", "w+")

# print(f.write(""))
# f.write("Hi there new line!")
# print()

# import os

# os.remove("file.txt")

# class Student:

#   def __init__(self, name):
#     self.name = name

#   def hello(self):
#     print("Hello", self.name)

# student2 = Student("Jai")
# student2.hello()


# class Student_marks:
#   def __init__(self, Subject_name, marks):
#     self.Subject_name_ = Subject_name
#     self.marks = marks


#   def AvgPrint(self):
#     sum = 0
#     for mark in self.marks:
#       sum = sum + mark
#     avg = sum/len(self.marks)
#     print(round(avg, 2))
#     # print("This is list", self.marks)

# Class12 = Student_marks("Maths", [50, 40, 60, 70, 80, 96, 72])

# Class12.AvgPrint()



# class Account: 

#   def __init__(self, Account_Holder, balance, accountNo, accountPasscode):
#     self.balance = balance
#     self.__accountNo = accountNo
#     self.__accountPasscode = accountPasscode
#     self.Account_Holder = Account_Holder

  
#   def debitAmount(self, amount):
#     passcode = input("Enter Your Passcode: ")
#     if self.__accountVerification(passcode):
#       if self.balance < amount: return "Insufficient Balance"
#       print("debiting...")
#       self.balance -= amount
#       print("Your Balance After Debit Is ", self.balance)
#     else:
#       return "Incorrect Password."
  
#   def creditAmount(self, amount):
#     print("Crediting...")
#     self.balance += amount
#     print("Your Balance After Credit Is ", self.balance)

#   def __accountVerification(self):
#     password = input("Enter your password:")
#     if password == self.__accountPasscode:
#       return True
#     else:
#       return False

#   def viewInfo(self):
#     self.__ViewAccountInfo()

#   def __ViewAccountInfo(self):
#     if self.__accountVerification():
#       print("Your Account Number is ", self.__accountNo, " and the password is ", self.__accountPasscode)
#     else:
#       print("Incorrect Password")

  

# FirstCustomer = Account("Jaiwant", 20000, 403, "devBarotLoveToCode@22")

# FirstCustomer.debitAmount(400)
# FirstCustomer.creditAmount(6000)
# FirstCustomer.viewInfo()

# lst = [1, 3, 4, 6, 10, 42]
# lst1 = [10, 20, 50, 40, 60, 20]

# lst2 = []

# idx = 0
# for val in lst:
#     # print(val)
#     # print(lst[idx])
#     lst2.insert(idx, val*lst1[idx])
#     idx+=1

# print(lst2)


# class Complex:
#   def __init__(self, real_number, img):
#     self.real_number = real_number
#     self.img = img

#   def ShowNumber(self):
#     print(self.real_number, "i +", self.img, "j")

#   def __add__(self, num2):
#     newReal = self.real_number + num2.real_number
#     newImg = self.img + num2.img
#     return Complex(newReal, newImg)

# num1 = Complex(43, 50)
# num1.ShowNumber()

# num2 = Complex(23, 17)
# num2.ShowNumber()

# num3 = num1 - num2
# num3.ShowNumber()


# class Circle:

#   def __init__(self, rad):
#     self.rad = rad

#   def Area(self):
#     return (22/7)*self.rad**2
  
#   def perimeter(self):
#     return 2*(22/7)*self.rad

# circle = Circle(21)

# print(circle.Area())
# print(circle.perimeter())



# class Employee:

#   def __init__(self, role, department, salary):
#     self.role = role
#     self.department = department
#     self.salary = salary

#   def showdetails(self):
#     print("You're an",self.role,"and you're assigned in", self.department, "department and your decided salary will be", self.salary, "₹/m")

# class Engineer(Employee):
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#     super().__init__("Engineer", "IT", "69,000")

# jack = Engineer("Dev", "80")
# jack.showdetails()

# class Order: 
#   def __init__(self, item, price):
#     self.item = item
#     self.price = price

#   def __gt__(self, order2):
#     return self.price > order2.price

# order1 = Order("Chips", "Rs.20")
# order2 = Order("tea", "Rs.50")

# print(order1 > order2)