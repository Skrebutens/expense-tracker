#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#

expenses = []
izdevumi = []
import json
from statistics import mean


# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)

f = open('expenses.json',)
data = json.load(f)
f.close()

def average(expenses):
    return mean (expenses)

pass

while True:
    print("\nChoose command:")
    print("1. ievadīt izdevumus: nosaukumu, summu un kategoriju")
    print("2. atspoguļot uz ekrāna visus izdevumus")
    print("3. iespēja atlasīt 10 lielākus izdevumus")
    print("4. iespēja atlasīt 10 mazākus izdevumus")
    print("5. iespēja apskatīt vidējo izdevumu summu")
    print("6. Iziet")
    command = input("Ievadiet jūsu izvēli (1-6): ")

    
    if command == '1':
        nosaukums = input("Ievadiet nosaukumu: ")
        summa = input("Ievadiet summu(eiro): ")
        kategorija = input("Ievadiet kategoriju: ")

        izdevumi = {"nosaukums": nosaukums,"summa":summa,"kategorija": kategorija}
        expenses.append(izdevumi)
        pass
    elif command == '2':
        print(expenses)
        pass
    elif command == '3':
        def summa(expenses):
            return int(expenses["summa"])
        expenses.sort(key = summa, reverse = True)
        print(expenses[0:10])

        pass
    elif command == '4':
        def summa(expenses):
            return int(expenses["summa"])
        expenses.sort(key = summa, reverse = False)
        print(expenses[0:10])
        pass
    elif command == '5':
        print(average)
        pass
    if command == "6":
        print("Exiting...")
        break
with open("expenses.json", "w") as outfile:
    json.dump(expenses, outfile)
# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass
