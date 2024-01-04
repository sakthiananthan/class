from operations import *
from tabulate import tabulate

print("Welcome to student manager app !")

while True :
    print("You can perform the below operations :")
    print("1. Register new student\n2. View student data\n3. Update Student data")
    print("4. Delete Student")

    choice=input("Enter your choice[1,2,3,4] : ")

    if choice=="1":
        print("you have chosen registration module !")
        registration()
    elif choice=="2":
        print("you have chosen view students !")
        viewstudent()
    elif choice=="3":
        print("you have chosen Update module")
        update_stud()
    elif choice=="4":
        print("you have chosen delete module !")
        delete_stud()
    else:
        print("Invalid option ! please try again")
        
    
    cont=input("do you want to continue(y/n) : ")

    if cont=="n":
        print("Thanks for using this application")
        exit()