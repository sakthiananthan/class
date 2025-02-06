from fun import *

print("welcome to student manager !")

while True:
    print("what would you like to do today ?")
    print("1. Register new student\n2. View record\n3. Update student record\n4. Delete record")
    choice=input("Enter your choice[1,2,3,4] : ")
    if choice=="1":
        create()
    elif choice=="2":
        view()
    elif choice=="3":
        update()
    elif choice=="4":
        delete()
    else:
        print("invalid choice")
    con=input("do you want to continue y/n: ")
    if con=="y":
        continue
    else:
        print("Thanks for using the app")
        exit()