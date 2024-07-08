while True:
    fraction_str = input("How much fuel do you have left? ")
    try:
        top_num = int(fraction_str.split("/")[0])
        bottom_num = int(fraction_str.split("/")[1])
    except ValueError:
        print("Invalid fraction provided.")
        continue
    else:
        try:
            fuel_float = top_num / bottom_num
        except ZeroDivisionError:
            print("Invalid fraction. Cannot divide by zero.")
            continue
        else:
            fuel_percentage = int(fuel_float * 100)
            if fuel_percentage == 100:
                print("F")
            elif fuel_percentage == 0:
                print("E")
            else:
                print(f"{str(fuel_percentage)}%")
            break


