import random   #"Random" is used to choose computer attack.
def main(): #The main funcion connects other functions together. Thema in function consist of input, processing, output.
    print("Welcome to Ultimate Ninja Battle Combat!!!")
    name = str(input("Please enter your name: "))
    print("Welcome, ", name)
    balance=100
    print("Your cuurent balance is $100")
    print("Please choose from the following menu: ")
    print("(I)nstructions")
    print("(P)lay game")
    print("(Q)uit")
    menu = str(input())
    historyBalance=[] #The historyBalance list is used to store the balance of each round.
    while not((menu=="Q" or menu=="q") or balance<=0): #The loop is used to quit the game if player want, or if balance is less than 0, the game can not continue.
        if menu == "i" or menu=="I":
            Instruction()
            menu=str(input())
        else:
            if menu == "P" or menu == "p":
                bet = int(input("Please enter the amount to bet. All bets must be multiples of 5. "))

                Bet(bet)
                Play(name)
                attack=int(input())
                Checkpmove(attack)
                cattack=int(random.random()*6)
                Playermove(attack)
                Computermove(cattack)
                balance=Winner(attack,cattack,bet,balance,name)
                historyBalance.append(balance)
                menu=str(input("Please choose follow menu:\n(I)nstructions\n(P)lay game\n(Q)uit game"))
            else:
                print("You must Enter I,P,Q")
                menu=str(input("Please choose follow menu:\n(I)nstructions\n(P)lay game\n(Q)uit game"))
    print("Goodbye",name,"Your final balance is",balance)

    print("Your balance history is: ")
    print("Starting Balance: $100")
    for i in range(len(historyBalance)): # List and print the balance of each round.
        print("After round",(i+1),historyBalance[i])
            


def Instruction(): #The Instruction function is the menu of the game.
    print("Welcome to Ultimate Ninja Battle Combat!!! You will be fighting against the computer, and the winner gets bragging rights. For each turn you will be asked to use one of the 6 attacks below:")
    print("(1) Punch of Fury")
    print("(2) Kick of Punishment")
    print("(3) Sword of Justice")
    print("(4)Shuriken of Vengeance")
    print("(5)Nunchucks of Anger")
    print("(6) Knife of Freedom.")
    print("Choose wisely.")
    print("Your current balance is $100")
    print("(I)nstructions")
    print("(P)lay game")
    print("(Q)uit")

def Play(name): #The Play function is used to ask player to choose an attack.
    print(name,",You must choose one of the following attacks: ")
    print("(1) Punch of Fury")
    print("(2) Kick of Punishment")
    print("(3) Sword of Justice")
    print("(4)Shuriken of Vengeance")
    print("(5)Nunchucks of Anger")
    print("(6) Knife of Freedom.")

def Bet(bet): #The Bet function is used to check whether play's bet is a multiple of 5.
    while not(bet%5==0) :
        print("That is not a valid amount. You bet must be a multiple of 5, and be within your means.")
        print("Please enter the amount to bet. All bets must be multiples of 5.")
        bet=int(input())
    else:
        print("You choose to bet$",bet)
        return bet

def Playermove(pmove): #The Playermove function use "if" to let computer know which attack player choose.
    if pmove==1:
        print("You chose: 1: Punch of Fury")
    else:
        if pmove==2:
            print("You chose 2: Kick of Punishment")
        else:
            if pmove==3:
                print("You chose 3: Sword of Justice")
            else:
                if pmove==4:
                    print("You chose 4: Shuriken of Vengeance")
                else:
                    if pmove==5:
                        print("You chose 5: Nunchucks of Anger")
                    else:
                        if pmove==6:
                            print("You chose 6: Knife of Freedom")
                        else:
                            print("NULL")
    
    return pmove

def Computermove(cmove): #The Computermove function is similar to Playermove founction.
    if cmove==0:
        print("Computer chose: 1: Punch of Fury")
    else:
        if cmove==1:
            print("Computer chose 2: Kick of Punishment")
        else:
            if cmove==2:
                print("Computer chose 3: Sword of Justice")
            else:
                if cmove==3:
                    print("Computer chose 4: Shuriken of Vengeance")
                else:
                    if cmove==4:
                        print("Computer chose 5: Nunchucks of Anger")
                    else:
                        if cmove==5:
                            print("Computer chose 6: Knife of Freedom")
                        else:
                            print("NULL")
    return cmove
def Winner(p,c,bet,balance,name): #The Winner function is used to judge player or computer win the game. And this founction also calculate the current balance. If player won, former balance plus the bet. If player lost, former balance minus the bet.

    if p==c+1: #Because computer attack range is from 0 to 5, and player move is range is from 1-6. If tie, value "p" should equal to "c+1".
        print("It's a tie! Your bet is returned.")
        print("Your current balance is $",balance)
    else:
        if (p==2 and c==0) or (p==3 and c==0) or (p==6 and c==0) or (p==3 and c==1) or (p==4 and c==1) or (p==6 and c==1) or (p==4 and c==2) or (p==5 and c==2) or (p==1 and c==3) or (p==5 and c==3) or (p==1 and c==4) or (p==2 and c==4) or (p==6 and c==4) or (p==3 and c==5) or (p==4 and c==5):
            balance=balance+bet # Won and get reward.
            print("Congratulations,you won",name)
            print("Your current balance is $",balance)
        else:
            balance=balance-bet # Lost and loss money.
            print("Unfortunately,",name,",you lost")
            print("Your current balane is $",balance)
    return balance
def Checkpmove(pmove): #The Checkpmove function is used to check whether the attack player choose is valid. The number which player choose must within 1 to 6.
    while not (pmove==1 or pmove==2 or pmove==3 or pmove==4 or pmove==5 or pmove==6):
        print("Number invalid")
        pmove=int(input("Please choose an attack"))
    print("Number valid")
    return pmove
main()
