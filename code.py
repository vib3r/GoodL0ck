# -------------------------
# [1] Project => GoodL0ck.py;
# [2] Coder => Abdullah, @Vib3r;
# [3] Created => 1/23/2022
# [4] Updated => 1/23/2022 6:51PM
# -------------------------
import random
import array

PASS_LEN = 10
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
LOW_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPER_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
VIB3R_LIST = NUMBERS + UPPER_CASE + LOW_CASE + SYMBOLS

vib3rDigit = random.choice(NUMBERS)
vib3rUpper = random.choice(UPPER_CASE)
vib3rLower = random.choice(LOW_CASE)
vib3rSymbol = random.choice(SYMBOLS)
# @Abdullahwk
GoodL0ck = vib3rDigit + vib3rUpper + vib3rLower + vib3rSymbol
for x in range(PASS_LEN - 4):
    GoodL0ck = GoodL0ck + random.choice(VIB3R_LIST)
    GoodL0ck_list = array.array('u', GoodL0ck)
    random.shuffle(GoodL0ck_list)
password = ""
for x in GoodL0ck_list:
        password = password + x
# print out password
print(password)
