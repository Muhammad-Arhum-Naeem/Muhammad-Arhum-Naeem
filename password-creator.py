import random
alphabets =("abcdefghijklmnopqrstuvwxyz")
numbers = ("123456789")
symbol = ("{}[]()\/")

all = (alphabets + numbers + symbol)
length = 16

password = "".join(random.sample(all, length))
print("Password is  " + password)

print("Password is not available at rockyou.txt")