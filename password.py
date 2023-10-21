#create a random password generator!

#import random
import random

#gather our characters
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
symbols = "!@#$%^&*()."
all = lower + upper + numbers + symbols

#input the length of password
length = int(input("enter the length of password:"))

#loop through each character
password = ''
for _ in range(length):
    password = ''.join([password,random.choice(all)])

print(password)



print('Done by santhosh')
    
