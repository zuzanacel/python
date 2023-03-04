"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Zuzana Čelková
email: zuzana.celkova7@gmail.com
discord: Zuzana Čelková#5969
"""
database = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

login_username = str(input("Please enter your username\n"))
login_password = str(input("Please enter your password\n"))

login_username, login_password = login_username.strip(), login_password.strip() 
if login_username in database and login_password == database[login_username]: 
    print("Welcome to the app,",login_username,"\nWe have 3 texts to be analyzed.")  
else:
    print("Unregistered user, terminating the program")
    exit() 

chosen_text = int(input("Enter a number btw. 1 and 3 to select:\n"))
x = (chosen_text - 1)
if chosen_text > 0 and chosen_text < 4:
    print("There are ",len(TEXTS[x].split())," words in the selected text")
    titlecase = 0
    uppercase = 0
    lowercase = 0
    digit = 0
    sum = 0
    d = dict()
    i = 1
    for word in TEXTS[x].split():                                            
                if word.istitle():                                                                                             
                    titlecase += 1
                if word.  isupper():
                     uppercase += 1 
                if word.istitle():                                                                                             
                    lowercase += 1
                if word.isdigit():                                                                                             
                    digit += 1
                    sum += int(word)     
                if len(word) in d:
                    d[len(word)] = d[len(word)] + 1
                else:
                    d[len(word)] = 1
                    
    print("There are ",titlecase," titlecase words")
    print("There are ",uppercase," uppercase words")
    print("There are ",lowercase," lowercase words")
    print("There are ",digit," numeric strings")
    print("The sum of all the numbers ",sum)
    print("-"* 20 ,"\nNR.| LEN |OCCURENCES\n","-"* 20)
    for key in list(d.keys()):
                    print(i,"|",key, "|", d[key])
                    i += 1

else:
    print("Číslo textu není v zadání")
    exit() 


