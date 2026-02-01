import sys
import time
import random
import os
def cooldown(range2=8,timewait=0.18):
    time.sleep(1)
    for _ in range(range2):
        print("\033[F\033[K", end="", flush=True)  # \033[F moves cursor up, \033[K clears the line
        time.sleep(timewait)

    if os.name == 'nt':
        os.system('cls')
cooldown(range2=20,timewait=0.08)
def printslow(text):
    for char in text:
        print(char, end='', flush=True)
        # Determine delay based on character type
        if char == " ":
            delay = random.uniform(*(0.02, 0.03))
        elif char in ".!?,;:😢😉🌹🤗🏎️🚘✅🦾❌👍👌💥✅🌓🚘🌹💅'":
            delay = random.uniform(*(0.3, 0.6))
        else:
            delay = random.uniform(0.04, 0.10)
        time.sleep(delay)

        if random.random() < 0.05:
            time.sleep(random.uniform(0.1, 0.3))
    print()


#VAzifa 1: Greet the user by their family name 
printslow("Familiyangizni ni kiriting janob pomidor -- ")
familyname = input("")
time.sleep(0.5)
printslow("\nSalam aleykum, janob " + familyname + " 🤗🌹")


cooldown()

#VAzifa 2: State the users school name 
printslow("Maktabizni nomini aytvoring janob " + familyname + " --  ")
schoolname = input("")
printslow(f"\nSiz {familyname}, {schoolname}da o‘qivotkaningizni bilib oldim🤗🌹")

cooldown()

#VAzifa 3: Calculate АНИК Ёши 
printslow("Qachon tug'ilding janob JIGULI🚗🚘🏎️ (DD.MM.YYYY): ")
birthdate = input("")
birthdate = birthdate.split(".")
birthday = int(birthdate[0])
birthmonth = int(birthdate[1])
birthyear = int(birthdate[2])

currentyear = time.localtime().tm_year
currentday = time.localtime().tm_mday
currentmonth = time.localtime().tm_mon
year = currentyear - birthyear

month = currentmonth - birthmonth
if month < 0:
    year -= 1
    month += 12
day = currentday - birthday
if day < 0:
    month -= 1
    if month < 0:
        year -= 1
        month += 12
    if currentmonth in [1, 3, 5, 7, 8, 10, 12]:
        day += 31
    elif currentmonth in [4, 6, 9, 11]:
        day += 30
    else:
        day += 28
if year < 0:
    printslow("Bor, roddomga qayt, sen hali tug‘ilmading🌹😢")
    time.sleep(2)
    sys.exit()
elif year <= 2:
    printslow("ishonmadim karoch, o'tib ketamiz")
    time.sleep(2)
elif year <= 4:
    printslow("Yoo bratishka, komputer oldida o'tirib nima qilasan, bor uyga🌹😭")
    time.sleep(2)
    sys.exit()
elif year < 7:
    printslow("Bor, bog'chadan chaqirishyapti seni🌹😭")
    time.sleep(2)
    sys.exit()

finalage = f"{year} yil, {month} oy, {day} kun"
printslow(f"Siz {finalage} yashagansiz, janob {familyname}🤗🌹")

cooldown()

#VAzifa 4: calcutlate CУММА of three numbers
printslow("Birinchi sonni ayting🤗: ")
num1 = int(input(""))
printslow("Ikkinchi sonni ayting🤗: ")
num2 = int(input("")) 
printslow("Uchinchi sonni ayting🤗: ")
num3 = int(input(""))
sum = num1 + num2 + num3
printslow(f"shu uchta sonning yigindisi🌹: {sum}")
time.sleep(0.5)

cooldown()

#VAzifa 5: Calculate the perimeter of a rectangle
printslow("tortburchakni uzunligini kiriting😉 --  ")
length = float(input(""))
printslow("tortburchakni kengligini kiriting😂😂😂😂 --  ")
width = float(input(""))
perimeter = float(2 * (length + width))
stage1mock = f"ehhh, siz uzizni {year} yoshingizda, {schoolname}da o'qib turib,\nshu to'rtburchakning perimetri {perimeter} ekanligini bilmaysiz, janob {familyname}. 😢🌹"
printslow(stage1mock)
time.sleep(1)
cooldown()
