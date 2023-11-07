#Random Password Generator:

import random as rand

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCEDFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()*+-=?@[]"

Use_for = lower_case + upper_case + number + symbols 
length_for_pass = 8

password = "".join(rand.sample(Use_for, length_for_pass))

print("Your Generated Password is: " + password)