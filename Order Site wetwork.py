"""
Eric Schwenn
CIS 188
Lab 2.2
"""

import random
import sys

keyword = "* "

print("This is *INSERT APP NAME HERE*. We are pleased that you are using our *METHOD OF PRODUCT DEPLOYMENT HERE*")

user_name = input("What is your name?\n")
    

while True:
    print("Hello " + user_name + "! For legal reasons, how old are you?")
    user_age = int(input())
            
    random_num = random.randint(1, 6)  
    for x in range(random_num):
        print(keyword * (x + 1))
        break

            
    if user_age >= 18:
        income = int(input("And what is your income?\n"))
        dinner = ""
        if income < 10000:
            print("You should probably be saving your money and not eating out. Closing app")
                    
            random_num = random.randint(1, 6)
            for x in range(random_num):
                print(keyword * (x + 1))
            break
        elif 10000 <= income <= 20000:
            dinner = input("Would you like PIZZA or PASTA for dinner? (enter in lowercase only!)\n")
                    
            random_num = random.randint(1, 6)
            for x in range(random_num):
                print(keyword * (x + 1))
                break

            
            time = input("And what time would you like to eat tonight?\n")
            if dinner == 'pasta':
                print("Wonderful, " + user_name + "! I've booked an appointment for Olive Garden at " + time + "pm tonight for a " + dinner + " dinner.")
                        
                random_num = random.randint(1,6)
                for x in range(random_num):
                    print(keyword * (x + 1))
                    break

            elif dinner == 'pizza':
                print("I know the best pizza place, " + user_name + ". I will call ahead and reserve a table for you at " + time + "pm tonight")
                        
                random_num = random.randint(1,6)
                for x in range(random_num):
                    print(keyword * (x + 1))
                    break

            else:
                print("Looking for a " + dinner + " place for you. *LOADING LIST*")
                        
                random_num = random.randint(1,6)
                for x in range(random_num):
                    print(keyword * (x + 1))
                    break
        elif 20000 < income <= 100000:
            dinner = input("Would you like SUSHI or STEAK for dinner? (enter in lowercase only!)\n")
            dinner = dinner
                    
            random_num = random.randint(1, 6)
            for x in range(random_num):
                print(keyword * (x + 1))
                break
            time = input("And what time would you like to eat tonight?\n")
            if dinner == 'sushi':
                print("Wonderful, " + user_name + "! I've booked an appointment for the Sushi Shack at " + time + "pm tonight for a " + dinner + " dinner.")
                        
                random_num = random.randint(1,6)
                for x in range(random_num):
                    print(keyword * (x + 1))
                    break

            elif dinner == 'steak':
                print("I know the best steakhouse, " + user_name + ". I will call ahead and reserve a table for you at " + time + "pm tonight")
                        
                random_num = random.randint(1,6)
                for x in range(random_num):
                    print(keyword * (x + 1))
                    break
            else:
                print("Looking for a " + dinner + " place for you. *LOADING LIST*")
                        
                random_num = random.randint(1,6)
                for x in range(random_num):
                    print(keyword * (x + 1))
                    break

        elif 100000 < income <= 200000:
            dinner = input("Would you like Caviar or Wagyu for dinner (enter in lowercase only!)?\n")
            dinner = dinner
                    
            time = input("And what time would you like to eat tonight?\n")
            if dinner == 'caviar':
                print("Wonderful, " + user_name + "! I've booked an appointment at Nobu at " + time + "pm tonight for a " + dinner + " dinner.")
                        
                random_num = random.randint(1,6)
                for x in range(random_num):
                    print(keyword * (x + 1))
                    break

            elif dinner == 'wagyu':
                print("I know the best luxury steakhouse, " + user_name + ". I will call ahead and reserve a table for you at " + time + "pm tonight")
                        
                random_num = random.randint(1,6)
                for x in range(random_num):
                    print(keyword * (x + 1))
                    break
            else:
                print("Looking for a " + dinner + " place for you. *LOADING LIST*")
                        
                random_num = random.randint(1,6)
                for x in range(random_num):
                    print(keyword * (x + 1))
                    break

        elif income > 200000:
            print("I will feed you gold bars.")
                
            random_num = random.randint(1, 6)
            for x in range(random_num):
                print(keyword * (x + 1))
                break

        print("Hope you enjoy your dinner " + user_name + "!")
                
        for x in range(random_num):
            print(keyword * (x + 1))
            break

    else:
        dinner = input("Would you like PIZZA or PASTA for dinner? (enter in lowercase only!)\n")
        dinner = dinner
            
        time = input("And what time would you like to eat tonight?\n")
        if dinner == 'pasta':
            print("Wonderful, " + user_name + "! I've booked an appointment for Olive Garden at " + time + "pm tonight for a " + dinner + " dinner.")
                    
            random_num = random.randint(1, 6)
            for x in range(random_num):
                print(keyword * (x + 1))
                break

        elif dinner == 'pizza':
            print("I know the best pizza place, " + user_name + ". I will call ahead and reserve a table for you at " + time + "pm tonight")
                    
            random_num = random.randint(1, 6)
            for x in range(random_num):
                print(keyword * (x + 1))
                break

        else:
            print("Looking for a " + dinner + " place for you. *LOADING LIST*")
                    
            
    print("Hope you enjoy your dinner " + user_name + "!")
                
    random_num = random.randint(1, 6)
    for x in range(random_num):
        print(keyword * (x + 1))
        break

    while True:
        repeat_order = input("Would you like to make another reservation? (yes/no): ")
        if repeat_order == "yes":
            break
        elif repeat_order == "no":
            print("Thank you for using our service, " + user_name + "!")
            sys.exit()