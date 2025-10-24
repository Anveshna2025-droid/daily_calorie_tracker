""" 
This project is submitted by :
Name- Anveshna 
Btech CSE Core 
Section A
Roll no. - 2501010130
The following code runs a general program called the Calorie Tracker 2.0
Submitted to - Feroz Sir 
Date - 23-10-2025
"""
# TASK 1- Set up and Introduction
print("Welcome to Calorie Tracker 2.0 🥗 ")
print("Begin your journey to a healthy lifestyle with us 🎊!! Calorie Tracker 2.0 is a command-line interface-based calorie tracker module that helps individuals track their calorie intake and control it accordingly. Let's get started!!")
#prints the welcome messages
 
# TASK 2- Input and data collection
goal=float(input("Enter your goal intake "))
# takes the daily calroie limit
num=int(input("Enter the number of meals you've had : "))
# takes number of meals for later operations
list_num=num
# stores number of meals so that after the while operation when we do calculations it wont show division by zero error !
meal_list=[]
cal_list=[]
#blank lists to store data of meals and calories 
print("Please fill the following details ")

while num>0:
    #loop will continue till the condition is fulfilled 
    a=str(input("Name of the meal : "))
    b=float(input("Number of calories : "))
    meal_list.append(a)
    cal_list.append(b)
    #The values/information of the meal and calories will be stored in the blank lists we created first 
    num=num-1
    #After each entry of meal , the original value of num will be subtracted by 1 so at one point num will become zero 

# TASK 3- Calorie Calculations
cal_total=sum(cal_list)
average=cal_total/list_num
#the maths! 
print("Total calorie intake is : ", cal_total)
print("Average calorie intake is : ", average)

# TASK 4- Exceed limit warning system
if (cal_total>goal):
    print("Please control your intake ⚠ ")
else:
    print("You are in control , good to go ✔ !")
    #prints warning message if calorie limit is exceed
summ=str(input("Do you want a summary table ? \n (Yes/No)\n"))

# TASK 5- Neatly formatted output
if(summ=="Yes"):
    print("Meal name"+"  "*8+"Calorie intake")
    print("------------------------------------")
    for i in range(len(meal_list)):
        print(f"{meal_list[i]}"+" "*(20-len(meal_list[i]))+f"{cal_list[i]}")
        # The padding " "*(20-len(meal_list[i])) ensures the calorie count starts at column 21
print("Total calories"+" "*(15-len("cal_total"))+f"{cal_total}")
# Print the total calories, padded to align the numbers
print("Average calories"+" "*(19-len("average calorie"))+f"{average}")
# Print the average calories, padded to align the numbers
if(summ=="No"):
    print("Alright")
print("Thank you for using Calorie Tracker 2.0 🥗 \n Hope to see you soon again")