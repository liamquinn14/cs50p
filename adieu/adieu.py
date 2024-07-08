import sys

names = []
while True:
    try:
        next_name = input("Name: ")
    except EOFError:
        print("\n")
        if len(names) == 1:
           print(f"Adieu, adieu, to {names[0]}")
        elif len(names) == 2:
            print(f"Adieu, adieu, to {names[0]} and {names[1]}") 
        else:
            comma_names = ", ".join(names[0: -2])
            print(f"Adieu, adieu, to {comma_names} and {names[-1]}")
        sys.exit()
    else:
        names.append(next_name)
