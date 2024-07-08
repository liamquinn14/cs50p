menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    try:
        user_choice = input("Item: ")
    except EOFError:
        print("Finished Order!")
        break
    try:
       cost = menu[user_choice.title()]
    except:
        print("Item not found on menu. Please try again.")  
        continue
    else:
       total += cost
       print(f"Total: ${total}")
       continue 