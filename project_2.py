"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Zuzana Čelková
email: zuzana.celkova7@gmail.com
discord: Zuzana Čelková#5969
"""
#Cows And Bulls

import random
import time

def getDigits(num):
    return [int(i) for i in str(num)]

def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False
    
def generateNum():
    while True:
        num = random.randint(1000,9999)
        if noDuplicates(num):
            return num
        
def numOfBullsCows(num,guess):
    bull_cow = [0,0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)
      
    for i,j in zip(num_li,guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1        
    return bull_cow

print("Hi there!\n",
      "-"*47,
      "\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.\n"
      ,"-"*47,
      "\nEnter a number:\n","-"*47)

num = generateNum()
tries = 0
start = time.time()

def check_input(input):
    try:
        guess = int(input)
    except ValueError:
        print("Value is not a number,terminating the program")
        exit() 
    
while True:
    guess = input()
    check_input(guess)
    guess = int(guess)
      
    if not noDuplicates(guess):
        print("Number should not have repeated digits. Try again.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again.")
        continue
      
    bull_cow = numOfBullsCows(num,guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries += 1
      
    if bull_cow[0] == 4:
        end = time.time()
        print("Correct, you've guessed the right number in\n",tries, "guesses!\n","-"*47)
        if tries < 10:
            print("That's amazing")
        elif tries < 20:
            print("That's average")
        else: 
            print("That's not so good")
        print("Elapsed time:",int(end - start),"seconds")
        break