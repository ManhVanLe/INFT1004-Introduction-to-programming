'''
Author: Manh Van Le c3503668
Date: 31/03/2025(start date) - 28/04/2025(upload date)
Task: INFT1004/INFT1006 Assignment 1 Library Book Management System
'''
fiction = 0
non_fiction = 0
science = 0
history = 0
def initialise_inventory():
    global fiction
    global non_fiction
    global science
    global history
    print('Input the initial amount of each kinds of book: ')

    fiction = int(input('Fiction(maximum 30): '))#ask user to input the number of fiction first
    while not check_inventory_limit(1, fiction):
        fiction = int(input('Invalid input, type again: '))#if the input exceeds the limit, ask again

    non_fiction = int(input('Nonfiction(maximum 20): '))#ask user to input the number of non-fiction first
    while not check_inventory_limit(2, non_fiction):
        non_fiction = int(input('Invalid input, type again: '))#if the input exceeds the limit, ask again

    science = int(input('Science(maximum 15): '))#ask user to input the number of science first
    while not check_inventory_limit(3, science):
        science = int(input('Invalid input, type again: '))#if the input exceeds the limit, ask again

    history = int(input('History(maximum 25): '))#ask user to input the number of history first
    while not check_inventory_limit(4, history):
        history = int(input('Invalid input, type again: '))#if the input exceeds the limit, ask again

def check_inventory_limit(pos, lim):
    if pos == 1 :
        if lim > 30 or lim < 0 : #check the limit and positive of fiction
            return False
        else :
            return True
    if pos == 2: #check the limit of non-fiction and positive number
        if lim > 20 or lim <0:
            return False
        else :
            return True
    if pos == 3 : #check the limit of science and positive number
        if lim > 15 or lim < 0 :
            return False
        else :
            return True
    if pos == 4 : #check the limit of history and positive number
        if lim > 25 or lim < 0 :
            return False
        else :
            return True
def checkOutBook():
    global fiction
    global non_fiction
    global science
    global history
    choice = int(input("What genre of the book you want to borrow ? (1):Fiction, (2):Nonfiction, (3):Science, (4):History :"))#ask the user to input the genre of book they want
    while(choice != 1 and choice != 2 and choice != 3 and choice != 4 ):
        choice = int(input("Please choose between 1 and 4"))#if they input the value that beyones the given value, a message will be sent and ask them to input again

    if choice == 1:
        if fiction > 0: 
            fiction -= 1 #if they choose "1" the number of fiction books will decrease by 1
            print("Checking out successfully")# and a message is printed

        else :
            print("There are no available fiction books")#if the number of books is out, a message is printed

    if choice == 2:
        if non_fiction > 0:
            non_fiction -= 1 #if they choose "2" the number of non-fiction books will decrease by 1
            print("Checking out successfully")# and a message is printed
        else :
            print("There are no available non-fiction books")#if the number of books is out, a message is printed

    if choice == 3:
        if science > 0:
            science -= 1 #if they choose "3" the number of science books will decrease by 1
            print("Checking out successfully")# and a message is printed
        else :
            print("There are no available science books")#if the number of books is out, a message is printed

    if choice == 4:
        if history > 0:
            history -= 1 #if they choose "4" the number of history books will decrease by 1
            print("Checking out successfully")# and a message is printed
        else :
            print("There are no available history books")#if the number of books is out, a message is printed
            
def returnBook():
    global fiction
    global non_fiction
    global science
    global history

    choice = int(input("What genre of the book you want to return ? (1):Fiction, (2):Nonfiction, (3):Science, (4):History :"))#ask the user to input the genre of books that they want to return
    while(choice != 1 and choice != 2 and choice != 3 and choice != 4 ):
        choice = int(input("Please choose between 1 and 4"))
    
    if choice == 1:
        if fiction < 30: #check that the available number is still under the limit
            fiction += 1 #if they choose "1" the number of fiction books will increase by 1
            print("Returning successfully")
        else : #if the number of books returned exceeds the limit, a message is sent  
            print("Number of fiction has reached the limit already")

    if choice == 2:
        if non_fiction < 20: #check that the available number is still under the limit
            non_fiction += 1 #if they choose "2" the number of non-fiction books will increase by 1
            print("Returning sucessfully")
        else :#if the number of books returned exceeds the limit, a message is sent
            print("Number of non-fiction has reached the limit already")

    if choice == 3:
        if science < 15: #check that the available number is still under the limit
            science += 1 #if they choose "3" the number of science books will increase by 1
            print("Returning successfully")
        else :#if the number of books returned exceeds the limit, a message is sent
            print("Number of science has reached the limit already")

    if choice == 4:
        if history < 25: #check that the available number is still under the limit
            history += 1 #if they choose "4" the number of history books will increase by 1
            print("Returning successfully")
        else :#if the number of books returned exceeds the limit, a message is sent
            print("Number of history books has reached the limit already")

def inventoryAnalysis(): 
    for i in range (1, 5): #a while loops is used to assign assign the name of each kind of book to the variable "name" and some need calculations and then print the state of 4 kind of books because it runs 4 times
        if i==1:
            name = "fiction"
            num = fiction
            capacity = 30
        if i==2: 
            name ="non-fiction"
            num = non_fiction
            capacity = 20
        if i == 3:
            name ="science"
            num = science
            capacity = 15
        if i == 4: 
            name = "history"
            num = history
            capacity = 25
        if (num/capacity)*100 < 50: #if the percentage of it below 50 then the state is low
            state = "low"
        if 50 <= (num/capacity)*100 <=74: #if the percentage of it between 50 and 74 then the state is ok
            state = "ok"
        if 75 <= (num/capacity)*100: #if the percentage of it equal or greater than 75 the the state is high
            state = "high"
        print(f"There are {num} of {name} books available, which is {state}") #This statament is excecuted 4 times arrcording to 4 kind of books

def restockInventory():
    global fiction
    global non_fiction
    global science
    global history
    print("The current inventory is: ")#This function first shows the current number of each kinds of books in the library
    print(f"{fiction} of fiction books ")
    print(f"{non_fiction} of non-fiction books ")
    print(f"{science} of science books ")
    print(f"{history} of fiction books ")
    choice= int(input("Do you want to add any books: (1): yes, (2): no :"))#Then it ask users if they want to go add more book or stop
    while choice != 1 and choice != 2: #This statement is to handle the user input
        choice= int(input("Invalid input, please try again: "))#If they input something but not 1 or 2, a message will be sent and ask input again
    while choice != 2 : 
        kind = int(input("Which kind of books that you want to restock: (1)fiction , (2)non-fiction, (3)science, (4)history: "))#when user choose 1, a message it sent and ask user to input the type of books that they want
        while not kind in range (1,5):#if users input something outside the above 4 options, they will be asked to type again
            kind = int(input("Invalid input, please try again: "))

        if kind == 1 : 
            if fiction == 30:# if the number of fiction is 30 already, a message is sent and quit the loop
                print("Can not add more fiction books")
                break

            amount = int(input("How many books you want to add ?"))#ask users how many books they want to add
            while fiction + amount > 30 : #check if the number of fictions after being added is still under limit
                amount = int(input("Can not exceed 30 books, please add again: "))
            fiction += amount #if everything is fine, then the amount will be added in to the current number of fiction and a message is sent
            print(f"The inventory has been restocked! The number of fiction is {fiction} now")

        if kind == 2 :
            if non_fiction == 20:#if the number of non-fiction is 20 already, a message is sent a quit the loop
                print("Can not add more non-fiction books")
                break

            amount = int(input("How many books you want to add ?"))#ask users how many books they want to add
            while non_fiction + amount > 20 : #check if the number of non-fictions after being added is still under limit
                amount = int(input("Can not exceed 20 books, please add again: "))
            non_fiction += amount#if everything is fine, then the amount will be added in to the current number of non-fiction and a message is sent
            print(f"The inventory has been restocked! The number of non-fiction is {non_fiction} now")

        if kind == 3 :

            if science == 15: #if the number of science is 15 already, a message is sent a quit the loop
                print("Can not add more science books")
                break

            amount = int(input("How many books you want to add ?"))#ask users how many books they want to add
            while science + amount > 15 : #check if the number of science after being added is still under limit
                amount = int(input("Can not exceed 15 books, please add again: "))
            science += amount#if everything is fine, then the amount will be added in to the current number of science and a message is sent
            print(f"The inventory has been restocked! The number of sicence is {science} now")

        if kind == 4 :

            if history == 25:#if the number of history is 25 already, a message is sent a quit the loop
                print("Can not have more history books")
                break

            amount = int(input("How many books you want to add ?"))#ask users how many books they want to add
            while history + amount > 25 : #check if the number of history after being added is still under limit
                amount = int(input("Can not exceed 25 books, please add again: "))

            history += amount#if everything is fine, then the amount will be added in to the current number of history and a message is sent
            print(f"The inventory has been restocked! The number of history is {history} now")
            
        break
               
def menu():#when the function is called, it shows a menu first
    print("What action do you want to do ?")
    print("1. Check out a book")
    print("2. Return a book")
    print("3. Inventory analysis")
    print("4. Restock inventory")
    print("5. Quit")
    choice = int(input("Press the action number that you want (1),(2),(3),(4),(5): "))
    while not choice in range (1, 6):
        choice = int(input("Please choose the valid input: "))#check if users input the right value
    while choice != 5: #while user not choose 5(quit) the program calls the corresponding function
        if choice == 1 :
            checkOutBook() 
        if choice == 2 :
            returnBook()
        if choice == 3 :
            inventoryAnalysis()
        if choice == 4 :
            restockInventory()#after a function is called, a menu is showed again and asks users for input the option they want
        print("What action do you want to do ?")
        print("1. Check out a book")
        print("2. Return a book")
        print("3. Inventory analysis")
        print("4. Restock inventory")
        print("5. Quit")
        choice = int(input("Press the action number that you want (1),(2),(3),(4),(5): ")) 
        while choice not in range (1,6):
            choice = int(input("Invalid input, please try again: "))

    print("See you again !!")

def main(): #the main funcion will call these function

    initialise_inventory()
    menu()

main() #program starts by calling the main() function
