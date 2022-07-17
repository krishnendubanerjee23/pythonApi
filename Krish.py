# a = int(input('Please enter the initial range:'))
# b = int(input('Please enter the end range :'))
# l = []
# for i in range(a,b):
#     if i%2 != 0:
#         l.append(i)
#     if len(l)>19:
#         break
# print(l)

#Write a program to display all the numbers which are divisible
#by 11 but not by 2 between 100 and 500.

# a = int(input('Please enter the initial range:'))
# b = int(input('Please enter the end range :'))
# l = []
# for i in range(a,b):
#     if i%2 != 0 and i%11==0:
#         l.append(i)
#     # if len(l)>19:
#     #     break
# print(l)

#Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

# a = int(input('Please enter the initial range:'))
# b = int(input('Please enter the end range :'))
# l = []
# l1 =[]
# for i in range(a,b):
#     if i%2 != 0:
#         l.append(i)
#     else :
#         l1.append(i)
    
# print("sum of odd number:",sum(l))
# print("sum of even number:  ",sum(l1))

#Q.// a program to print all prime numbers  that fall between two numbers including both(accept two numbers from the user)

# b = int(input('Please enter the end range :'))
# l=[]
# for i in range(2,b+1):
#    for j in range(2,i):
#       if i%j == 0:
#          break
#    else :
#       l.append(i)
# print(l)

# Q.//Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#              Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

# n = int(input("Pleae input the unit of consumption : "))
# if n in range(0,101):
#    print("No charge") 
# elif n in range(101,201):
#    print('Rs :',(n-100)*5)
# else:
#    print('Rs :',(n-100)*10)

# Q.// Write a program to display the last digit of a number.
# (hint : any number % 10 will return the last digit)

# n= int(input('Please enter a number.'))
# x=n%10
# print('Last digit of thisnumber is ',x)

# Q.// Write a program to check whether the last digit of a number( entered by user ) is 
# divisible by 3 or not.

# n= int(input("Please a number : "))
# p = n%10
# if p%3 == 0:
#    print("Number is divisible by 3 ")
# else :
#    print("Number is not divisible by 3 ")







