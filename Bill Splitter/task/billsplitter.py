# write your code here
import random

people_count = int(input("Enter the number of friends joining (including you):"))

if people_count <= 0:
    print("No one is joining for the party")
    exit()

friends = {}

name = input("Enter the name of every friend (including you), each on a new line:")

friends[name] = 0

for n in range(people_count - 1):
    friends[input()] = 0


bill_amount = float(input("Enter the total bill value:"))

lucky_draw = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')

payers = people_count
lucky_person = None

if lucky_draw == 'Yes':
    payers -= 1
    lucky_person = random.choice(list(friends.keys()))
    print(f"{lucky_person} is the lucky one!")
else:
    print("No one is going to be lucky")

split = round(bill_amount / payers, 2)

for f in friends.keys():
    friends[f] = split if f != lucky_person else 0

print(friends)
