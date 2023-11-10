
from tkinter import *
root = Tk()
root.title("Tzx calculation programme")
root.geometry("300x200")
label = Label(root, text = "Welcome to tax calculator")

var1 = StringVar()
var1.set("")
entry = Entry(root, width=20, textvariable=var1)

clearbutton = Button(root, text = "clear")

def cleartext(event):
    var1.set("")

clearbutton.bind("<Button-1>", cleartext)

label.pack(pady=20)
entry.pack(pady=20)
clearbutton.pack(ipadx=10,ipady=10)
root.mainloop()


count = 0
tax_brackets = [(0, 150000, 0), (150001, 300000, 0.05), (300001, 500000, 0.1), (500001, 750000, 0.15),(750001,1000000,0.2),(1000001,2000000,0.25),(2000001,5000000,0.3),(50000001,float("inf"),0.35)]
tax_deduction = []
def calculate_net_income(income):
    income - 60000
    return income

Id = input("Please provide you national ID number: ")
fullic = input("Please input your annual income:  ")
status = input("Please input your status 1-4 \n1 Single\n2 Divorce\n3 Married\n4 Marreid but did not earn money\n")
if status == 3 or 4:
    q = int(input("How do you pay tax? \n1 report taxes seperately\n2 combind with your partner\n: "))
    if q == 1:
        tax_deduction.append(60000)
    elif q == 2:
        tax_deduction.append(120000)

kids = int(input("How many child do you have below 20 years old?: "))
for i in range(kids):
    age = int(input("How old is your "+str(i+1)+"st child"))
    if age<5:
        tax_deduction.append(30000)
        count +=1
    elif age>5 and age<=20:
        tax_deduction.append(30000)
for i in range(count):
    tax_deduction.append(30000)
if kids == 1:
    tax_deduction.append(30000)

parents = int(input("How many parents do you have that their age is older than 60 and does not earn money?: "))
if parents == 2:
    tax_deduction.append(60000)
if parents == 1:
    tax_deduction.append(30000)

disable = str(input("Do your family have any disability?"))
if disable == "yes":
    gg = int(input("how many? eg. mother father & only one relatives are able to use for deduction (maximum 3)"))
    if gg == 1:
        tax_deduction.append(60000)
    if gg == 2:
        tax_deduction.append(120000)
    if gg == 3:
        tax_deduction.append(160000)
pwd = "Please input provident fund"
insurance = int(input("Please input tax deduction regarding life insurance: "))
if insurance > 0.15*fullic:
    insurance = 0.15*fullic
tax_deduction.append(insurance)
socialsec = int(input("Please input social security contributions: "))
if socialsec>9000:
    socialsec = 9000
tax_deduction.append(socialsec)
houseinsure = "Please input your Interest on housing purchases: "
if houseinsure > 100000:
    houseinsure = 100000
tax_deduction.append(houseinsure)
funds = "Please input other funds: "
donate = "Please input your taxdeduction on donation: "
left = fullic-sum(tax_deduction)
if donate>left:
    donate = left*0.1
    tax_deduction.append(donate)
print(tax_deduction)



