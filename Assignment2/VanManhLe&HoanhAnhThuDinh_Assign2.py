'''
Author: Van Manh Le c3503668 & Hoang Anh Thu Dinh c3446404
Date: 15/5/2025 - 27/5/2025
Task: INFT1004/1006 Assignment 2 - Library management system - part 2
This assignment is an advanced version of the assignment 1 - Library management system, which simulates 
a library management system that supports basic functionalities such as loading and saving inventory and
loan data, allowing users to add new genres, checkout and return books, analyze stock levels textually 
and visually, and restock genres while ensuring data validation and error. The system uses Python dictionaries
 to track genre data and matplotlib to visualize inventory. With all the basic function advanced compared to assignment 1

'''
import matplotlib.pyplot as plt

#Define maximum capacity for each genre (new genre has a default maximum of 30)
max_fiction = 30
max_nonFiction = 20
max_history = 25
max_science =15

#Dictionaries for limits, inventory of all genre, list of all genre, loan records and item on loan
limits = {"fiction": max_fiction, "nonfiction": max_nonFiction, "history":max_history, "science": max_science}
all_genre={}   #list of current inventory
genre_list={}  #list of genre
loan_item={}   #list of loan item

#Variable to count genre
count = 0 #count increased by 1 after one new genre added
# Loan inventory and loan data from file and initialise genre list
def initialise_inventory():
    global count
    try:
        file = open('LibraryInventory.txt','r') #initialise the data from the provide file to the all_genre dictionary
        for line in file:
            whole = line.split()       #Split lines in reading file into 2 parts, genre names and current stocks
            genre = whole[0].lower()   #The first part (index 0) of the line is assigned to the variable genre
            stock = int(whole[1])      #The second part of the line is assigned to the variable stock
            all_genre[genre] = stock       #Add the key(genre) and value(stock) to the all_genre dictionary
        file.close()

        try:
            loan_file=open("LoanData.txt", "r") #initialise the data from the LoanData file to the loan_item dictionary
            for line in loan_file:
                whole = line.split()
                genre = whole[0].lower()
                loan_count = int(whole[1])
                loan_item[genre] = loan_count
            loan_file.close()

        except FileNotFoundError:#if LoanData file is not found, initial the loan_item{} to 0 loan item for each genre
            for genre in all_genre.keys():
                loan_item[genre]= 0

        #initialise the genre list
        for genre in all_genre.keys():
            count = count+1
            genre_list[count]= genre

        for genre, stock in all_genre.items():
            print(f"There are {stock} of {genre} books ")
    except FileNotFoundError:
        print('file was not found')

#Add new genre to the genre list
def update_genre_list(new_genre):  
    global count #It is now the number of the current genres in the inventory
    count = count + 1 #Increase by 1 to have more room for the new genre in the genre_list dictionary
    genre_list[count] = new_genre  #Add the value(new_genre) and key(count) to the genre_list dictionary


#Save inventory data to file
def save_inventory(): #save updated inventory
    try:
        file = open("LibraryInventory.txt", "w")
        for genre,stock in all_genre.items():
            file.write(f"{genre} {stock} \n")
        file.close()
    except Exception as e:
        print(f"Failed to save file: {e}")

#Save loan data to file
def save_loan_data(): #save loaned book
    try:
        file = open ("LoanData.txt","w")
        for genre, stock in loan_item.items():
            file.write(f"{genre} {stock} \n")
        file.close()
    except Exception as e:
        print(f"Failed to save loan file: {e}")

#Add new genre allow users to add new genres with validation
def add_new_genre():
    print('\n----------ADD NEW GENRE----------')
    while True:
        new_genre = input('enter new genre: ').strip().lower()#new genre added will be lowercased and removed any leading whitespace
             
        if not new_genre.isalpha(): # to exclude any case of invalid input
            print('genre cannot be a number. Please try again')
            continue
        if new_genre in all_genre.keys(): # to exclude the case that user enter genre that already existed
            print('this genre already existed. Please try again')
            continue
        else:
            while True:
                try:
                    number = int(input('Enter number of new genre(maximum 30): '))
                    if number < 0: # prevent from entering negative value
                        print("Number of book must be positive: ")
                        continue
                    elif number > 30:# limit of all new genre is 30, and cannot input higher number than 30
                        print('Number of book cannot be higher than 30: ')
                        continue
                    else:
                        all_genre[new_genre] = number #add new genre and its stock to all_genre
                        loan_item[new_genre] = 0 #assign 0 loan for new genre
                        update_genre_list(new_genre) #add new genre to genre list 
                        print(f"Genre {new_genre} added with {number} books.")
                        save_inventory()      #save change to the file after adding new genre
                        break
                except ValueError:# avoid string input
                    print("Please enter a valid number")
        break
#Handle both checking out and returning books
def checkout_and_return_book():
    print('\n-----------CHECKOUT AND RETURN BOOK----------')
    print ('CURRENT INVENTORY')
    for genre, stock in all_genre.items(): #print current inventory
            print(f"There are {stock} of {genre} books ")
    while True:
        action = input('Do you want to "checkout" or "return" a book or "quit" to stop: ').lower()
        if not action in ['checkout','return','quit']: 
            print ('Invalid input, please try again.')
            continue #If the input is not checkout or return it will continue run asking action till it receive valid input
        elif action == 'quit':#to stop asking action
            break
        
        while True:
            print(f'Please select options to {action}:') # the output will print the selected action

            for count, genre in genre_list.items(): # the list number of genre
                print(f'{count}. {genre}')

            while True:
                try:
                    genre_number= int(input('Please enter genre number: ')) 
                    if not genre_number in genre_list: #If input number is not in the genre list a message is print and ask user for input again
                            print('Invalid input. Please try again.')
                            continue  
                    break  
                except ValueError:
                    print('Invalid input. Input must be a number.')   

            genre = genre_list[genre_number] #the number input (genre) will be equal to genre name (which is the values in genre_list) 
            

            while True:
                try:
                    quantity = int(input(f'enter number of {genre} book you want to {action}: '))#from previous line, the output can print the name of genre regarding to selected genre number
                    if quantity <= 0: #check if quantity input is positive
                        print('quantity must be positive number') #if not, ask for input again
                        continue                 
                    break
                
                except ValueError:
                    print("Invalid input, quantity must be a number")

            if action == 'checkout': # If the action selected is 'checkout'
                if all_genre[genre] < quantity: # check if stock is not available or not enough for the input quantity
                    print('Not enough books available')
                    
                else: # if there is avialable stock
                    all_genre[genre] -= quantity # the stock of selected genre will be deduct quantity
                    loan_item[genre] += quantity # and add quantity to selected genre in loan_item 
                    print(f'{quantity} book(s) checked out from {genre}.')
                    
            if action == 'return': #If selected action is 'return'
                if loan_item[genre] < quantity:#check if users want to return more books than they checked out
                    print('cannot return more books than checked out books')
                    break

                elif  loan_item[genre] == 0:#check if there is on loan item or quantity return higher than on loan avialable
                    print('cannot return book that have not checked out')
                    break
                    
                else:
                    all_genre[genre] += quantity # add quantity return to stock
                    loan_item[genre] -= quantity # deduct quantity return form loan item
                    print(f" {quantity} book(s) returned to {genre}.")
            save_inventory() #save change of stock to file
            save_loan_data() #save loan item to file
            break
                
# Analysis the inventory textually and visually
def inventoryAnalysis():
    print("\n----------INVENTORY STATUS----------")

    for genre, stock in all_genre.items():
        max_limit = limits.get(genre, 30) #get the max capacities of each kind, all lately added genres have max capacity of 30

        capacity_percent = (stock / max_limit)*100 #the variable used to determine which status of each genre

        if capacity_percent >= 75: #if capacity_percentage is higher than 75
            status = "High" #status output is high 
        elif capacity_percent >= 50: #if capacity_percentage is higher than 50
            status= "Ok"#status output is ok
        else: 
            status="Low" #otherwise it return low
        
        print(f"{genre}: {stock}/{max_limit} books which is {status}") #The status of each genre are printed
    
    genres = list(all_genre.keys())
    stocks = list(all_genre.values())
    plt.bar(genres, stocks) #Show bar chart of x-axis is genre and y-axis is stock
    plt.xlabel("Genre")  
    plt.ylabel("Number of books")
    plt.title("Library Inventory Capacity") 
    plt.xticks(rotation=45) #rotate x text elements 
    plt.show()
def restock_inventory():
    print("The current inventory is: ")
    for number, genre in genre_list.items(): #Show the list of all available genre
        current = all_genre[genre]
        print(f"{number}. {genre} (Current stock: {current})")

    while True:
        try:
            genre_num = int(input("Enter the number of the genre that you want to restock: ")) #Ask users to input the number corresponding to the genre of book they want to restock
            if genre_num not in genre_list:
                print("Invalid number. Please choose the number that has a corresponding genre!")
                continue
            genre = genre_list[genre_num]
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    #Get max limit
    max_limit = limits.get(genre, 30) #Get the litmit of the selected genre, if it is a newly added genre, the default maximum capacity is 30
    current = all_genre[genre] #Get the current number of this genre in the inventory 
    on_loan = loan_item[genre] #Get the number of this genre on loan
    print(f"{genre} has {current}/{max_limit} books and {on_loan} on loan ")

    #Ask for quantity to restock
    if all_genre[genre] == max_limit:
        print(f"Number of {genre} has reached the limit already.")
        return
    while True:
        try:
            amount = int(input("Enter number of books to add: ")) #amout to restock
            if amount < 0:
                print("Quantity must be positive.")
                continue

            if current + amount + loan_item[genre] > max_limit: #If the number of this genre on loan + current + amount over the max capacity 
                allowed = max_limit - (current + loan_item[genre]) #It is the max number of books that user can restock
                print(f"You can only add {allowed} or less to the {genre} book now")  #Show the maximum number of book that user can restock for that genre
                continue
            else:
                all_genre[genre] += amount
                print(f"{amount} books added to {genre}. Total now: {all_genre[genre]} and {on_loan} on loan ") #If the number of books that user want to ask not over the limit, the amount is added into stock and a message is printed
            save_inventory() #Save changes to the files each time restock
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
#The menu function to show the menu and show again after a function is called
def menu():
    while True:
        print("\n-----------WHAT ACTION DO YOU WANT TO DO ?------------")
        print("1. Add new genre")
        print("2. Checkout/Return a book")
        print("3. Inventory analysis")
        print("4. Save changes")
        print("5. Restock inventory")
        print("6. Quit")
        
        choice = input("Press the action number that you want (1),(2),(3),(4),(5),(6): ").strip()

        while choice not in ["1","2","3","4","5","6"]:
            choice=input("Invalid menu option. Please try again: ").strip()

        if choice == '1' :
            add_new_genre() 
        elif choice == '2' :
            checkout_and_return_book()
        elif choice == '3' :
            inventoryAnalysis()
        elif choice == '4' :
            save_inventory()
            save_loan_data()
            print("Inventory saved successfully")
        elif choice == '5':
            restock_inventory()
        elif choice == '6':
            save_inventory()
            save_loan_data()
            print("See you again !!!")
            break
        
                
def main():
    initialise_inventory()
    menu()

main()

