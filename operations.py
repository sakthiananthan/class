import json_utils
from tabulate import tabulate


def registration():
    data=json_utils.json_read("stud.json")
    noofstud=len(data["students"])
    
    stud_dict={
        "Sno" : noofstud+1,
        "Name": input("Enter student name : "),
        "Age" : input("Enter student age : "),
        "Course" : input("Enter student course : "),
        "course duration" : input("Enter course duration : ")
    }
    data["students"].append(stud_dict)
    json_utils.json_write("stud.json",data)
    print("Student registered successully !!")

def viewstudent():
    data=json_utils.json_read("stud.json")
    table=[]
    for stud in data["students"]:
        row=[stud["Sno"],stud["Name"],stud["Age"],stud["Course"],stud["course duration"]]
        table.append(row)
    print(tabulate(table,headers=["Sno","Name","Age","Course","Course Duration"],tablefmt="grid",stralign="center",numalign="center"))
    
def delete_stud():
    viewstudent()
    data=json_utils.json_read("stud.json")
    try:
        id=int(input("Enter the sno of student you want to delete : "))
    except:
        print("invalid input")
    
    flag="n"
    for stud in data["students"]:
        if stud["Sno"]==id:
            flag="y"
            data["students"].remove(stud)
            i=1
            for stud_1 in data["students"]:
                stud_1["Sno"]=i
                i+=1
            json_utils.json_write("stud.json",data)
            print("student deleted successfully !")
    if flag=="n":
        print(f"{id} not found !!")
        
def update_stud():
    viewstudent()
    data=json_utils.json_read("stud.json")
    try:
        id=int(input("Enter the sno of student you want to update : "))
    except:
        print("invalid input")
        id=0
    
    flag="n"
    for stud in data["students"]:
        if stud["Sno"]==id:
            flag=stud["Name"]
            choice=input("what would you like to update ?[1,2,3,4]\n1. Name\n2. Age\n3. Course\n4. Course duration\n5. All the above \nEnter your choice : ")
            if choice in ["1","2","3","4","5"]:
                if choice=="1":
                  stud["Name"] = input("Enter student name : ") 
                elif choice=="2":
                    stud["Age"]=input("Enter student age : ")
                elif choice=="3":
                    stud["Course"]=input("Enter student course : ")
                elif choice=="4":
                    stud["course duration"]=input("Enter student course duration : ")
                else:
                    stud["Name"] = input("Enter student name : ") 
                    stud["Age"]=input("Enter student age : ")
                    stud["Course"]=input("Enter student course : ")
                    stud["course duration"]=input("Enter student course duration : ")
            else:
                print("invalid operation")
            json_utils.json_write("stud.json",data)
            print(f"student {flag} updated successfully !")
    if flag=="n":
        print(f"{id} not found !!")