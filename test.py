count = 0
tax_brackets = [(0, 150000, 0), (150001, 300000, 0.05), (300001, 500000, 0.1), (500001, 750000, 0.15),(750001,1000000,0.2),(1000001,2000000,0.25),(2000001,5000000,0.3),(50000001,float("inf"),0.35)]
tax_deduction = []
def calculate_net_income(income):
    income - 60000#ลดหย่อนต่อปี
print("*"*78)
print("Welcome to tax calculation programme".center(78))
print()
Id = input("Please provide you national ID number: ")

Id = input("Please provide you national ID number: ")
fullic = input("Please input your annual income:  ")
status = input("Please input your status 1-4 \n1 Single\n2 Divorce\n3 Married\n4 Marreid but did not earn money\n")
if status == 3 or 4:
    q = input("How do you pay tax? \n1 report taxes seperately\n2 combind with your partner\n: ")
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

parents = "How many parents do you have?: "
disable = "Do you have any disability?: "
private = "Please input your personal allowance: "
insurance = "Please input tax deduction regarding life insurance: "
donate = "Please input your taxdeduction on donation: "
fullspent = input("Please input your total annual spending: ")

print(tax_deduction)
#ประกันสังคม*12 ปี


