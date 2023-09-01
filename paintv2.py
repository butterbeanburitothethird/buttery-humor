##watch paint dry sim
import time
import random
debt = 45000
tempmoney = 0
mulit = 1
mulit_cost = 500
mulit_tutor = False
brush = "dollar store brush"
money = 0
trash = 0
average = 0
good = 0
great = 0
van_go = 0
paint_time = 15
brush_rng = 250
Tchance = 100
Achance = 200
G1chance = 225
G2chance = 250
##new player
NewPlayer = input("welcome. have you played before?(y/n): \n")
if NewPlayer == "n":
    time.sleep(0.5)
    print("\ngreat it is a pleasure to meet you new artist.\n")
    time.sleep(2)
    print("this is a simple game about painting\n")
    time.sleep(2)
    print("first you will make a painting\n")
    time.sleep(2)
    print("and finally profit! you will sell the paintings on esty\n")
    time.sleep(2.5)
    print("then you take your money to pay off your student loan debt of $45,000\n")
    time.sleep(2.5)
    print("ok lets start\n")
if NewPlayer == "y":
    print("") ###used as enter
##game loop
while True:
    to_do = input("would you like to paint(p), goto the store(s), sell art(e), or pay debt(d)\n")
 
    ##painting
    if to_do == "p":
        rarity1 = random.randint(1,brush_rng)
        print(f"\nyou start painting with the {brush}\n")
        time.sleep(paint_time)
        print("you are still painting...\n")
        time.sleep(paint_time)
        print("you are still painting...\n")
        time.sleep(paint_time)
        if rarity1 > Tchance:
            if rarity1 > Achance:
                if rarity1 > G1chance:
                    if rarity1 == G2chance:
                        van_go += 1
                        print(f"you finished painting and made a van go painting it is a master piece now you have {van_go}\n")
                        time.sleep(3)
                        continue
                    great += 1
                    print(f"you finished painting and made a great painting now you have {great}\n")
                    time.sleep(2.5)
                    continue
                good += 1
                print(f"you finished painting and made a good painting now you have {good}\n")
                time.sleep(2.5)
                continue
            average += 1
            print(f"you finished painting and made a average painting now you have {average}\n")
            time.sleep(2.5)
            continue
        trash += 1
        print(f"you finished painting and made a trash painting now you have {trash}\n")
        time.sleep(2.5)
 
    ##store 
    if to_do == "s":
        if brush == "dollar store brush":
            print(f"\nwelcome to the shop, you have {money} dollars\n")
            time.sleep(2)
            buy = input("would you like to buy a paint brush for $50 (y/n): \n")
            if buy == "y":
                if money >= 50:
                    money -= 50
                    brush = "paint brush"
                    Tchance = 75
                    Achance = 175
                    G1chance = 200
                    G2chance = 225
                    paint_time = 12
                    brush_rng = 225
                    print(f"you have bought {brush} you now have ${money}\n")
                    time.sleep(1.5)
                    print("thank you come again")
                    continue
                print("you are too poor get out.\n")
            if buy == "n":
                print("\nplease come again\n")
 
        if brush == "paint brush":
            print(f"\nwelcome to the shop, you have {money} dollars\n")
            time.sleep(2)
            buy = input("would you like to buy a paint roller for $100 (y/n): \n")
            if buy == "y":
                if money >= 100:
                    money -= 100
                    brush = "paint roller"
                    Tchance = 50
                    Achance = 150
                    G1chance = 175
                    G2chance = 200
                    paint_time = 9
                    brush_rng = 200
                    print(f"you have bought {brush} you now have ${money}\n")
                    time.sleep(1.5)
                    print("thank you come again\n")
                    continue
                print("you are too poor get out.\n")
            if buy == "n":
                print("\nplease come again\n")
 
        if brush == "paint roller":
            print(f"\nwelcome to the shop, you have {money} dollars\n")
            time.sleep(2)
            buy = input("would you like to buy a kolinsky brush for $250 (y/n): \n")
            if buy == "y":
                if money >= 250:
                    money -= 250
                    brush = "kolinsky brush"
                    Tchance = 25
                    Achance = 125
                    G1chance = 150
                    G2chance = 175
                    paint_time = 6
                    brush_rng = 175
                    print(f"you have bought {brush} you now have ${money}\n")
                    time.sleep(1.5)
                    print("thank you come again\n")
                    continue
                print("you are too poor get out.\n")
            if buy == "n":
                print("\nplease come again\n")
 
        if brush == "kolinsky brush":
            print(f"\nwelcome to the shop, you have {money} dollars\n")
            buy = input("would you like to buy a golden brush for $1000 (y/n): \n")
            if buy == "y":
                if money >= 1000:
                    money -= 1000
                    brush = "golden brush"
                    Tchance = 0
                    Achance = 100
                    G1chance = 125
                    G2chance = 150
                    paint_time = 3
                    brush_rng = 150
                    print(f"you have bought {brush} you now have ${money}\n")
                    time.sleep(1.5)
                    print("thank you come again\n")
                    continue
                print("you are too poor get out.\n")
            if buy == "n":
                print("\nplease come again\n")
 
        if brush == "golden brush":
            if mulit_tutor == False:
                print(f"\nwelcome to the shop, you have {money} dollars\n")
                time.sleep(1.5)
                print("I am sorry but we are out of brushes.\n")
                time.sleep(2)
                print("but you can pay some rich people to indorce your paintings\n")
                time.sleep(2.5)
                print("each time you buy it it will multiply your money per a painting\n")
                time.sleep(2.5)
                mulit_tutor = True
            buy_multi = input(f"one indorcment costs ${mulit_cost}\nWould you like to buy it?(y/n)\n")
            if buy_multi == "y":
                if mulit_cost <= money:
                    money -= mulit_cost
                    mulit_cost *= 2
                    mulit += 1
                    print(f"you now have ${money} left and {mulit}x multiplyer\n")
                    time.sleep(2)
                print("sorry you are to poor.\n")
                time.sleep(1.5)
            if buy_multi == "n":
                print("\nthank you come again.\n")
                time.sleep(1.5)
            continue
 
    ##sell paintings 
    if to_do == "e":
        print(f"\nyou have {trash} trash paintings, {average} average paintings, {good} good paintings,\n{great} great paintings, and {van_go} van go paintings\n")
        time.sleep(3.5)
        if mulit_tutor == True:
            print(f"and your multiplyer is {mulit}x\n")
            time.sleep(2)
        sell = input("would you like to sell ALL of your paintings(y/n)\n")
        if sell == "y":
            tempmoney += trash * 5 
            trash = 0
            tempmoney += average * 10
            average = 0
            tempmoney += good * 25
            good = 0
            tempmoney += great * 50
            great = 0 
            tempmoney += van_go * 250
            van_go = 0
            tempmoney *= mulit
            money += tempmoney
            tempmoney = 0
            print(f"you sold all of your paintings you now have ${money}\n")
            time.sleep(2.5)
            continue
        if sell == "n":
            print("\nplease come again.\n")
            continue
    
    if to_do == "d":
        print(f"\nyou have ${debt} of debt and have ${money}\n")
        time.sleep(2)
        paydebt = input("\nhow much of your debt would you like to pay?\n(please put whole number)\n")
        if int(paydebt) <= money:
            if int(paydebt) <= debt:
                debt -= int(paydebt)
                money -= int(paydebt)
                if debt == 0:
                    print("\ncongrats you won. gg! you are no longer in debt.\nbye bye")
                    break
                print(f"your new debt it ${debt}\n")
                continue
