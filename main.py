#!/usr/bin/python3

#The Selector function, selects what Program to run
def selector(num):
    if num  == "1":
        checker()
    elif num == "2":
        print("Calculator coming soon ...")
    else:
        #If it's anything other than the above call function again
        selector(input("Enter either 1 or 2: "))

#The Odd/Even Checker Function
def checker():
    print("\n------------------------------------")
    print("======= THE ODD/EVEN CHECKER =======\n")
    
    #Added this function to skip the intro if "except" was fired for incorrect input
    def checker_main():
        #Try & Except to catch any non intergers entered
        try:
            num = int(input("Enter a number to Test: "))
            if num % 2 == 0:
                print(f"\n{num} is an Even number.")
            else:
                print(f"\n{num} is an Odd number.")
        except:
            #If num is not an interger give them another chance to type 
            checker_main() #Invoke the main part of "checker" directly 
     
    checker_main()


#The Holy Main Function
def main():
    #Welcome message
    print("------------------------------------")
    print("======= WELCOME TO THE TOOLBOX =======")
    print("------------------------------------\n")

    #Call the Selector Function and pass it a program number to run
    selector(input("SELECT PROGRAM TO RUN:\n1 -> Odd/Even checker:\n2 -> Calculator: "))


if __name__== "__main__":
    main()
