months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date_str = input("Date: ")
    except EOFError:
        print("N/A.")
        break
    if "/" in date_str:
        date_arr = date_str.split("/")
        try:
            year = int(date_arr[2])
            month = int(date_arr[0])
            day = int(date_arr[1])
            if day == 0 or month == 0:
                print("Invalid date. Try again.")
                continue 
        except:
            print("Invalid date. Try again.")
            continue
        year_length = len(str(year))
        if year_length < 4:
            missing_zeroes = 4 - year_length
            padding = missing_zeroes * "0"
            year = padding + str(year)
            print(year)
        if len(str(day)) == 1:
            day = "0" + str(day)
        if len(str(month)) == 1:
            month = "0" + str(month)
        if int(month) > 12 or int(day) > 31:
            print("Invalid date. Try again.")
            continue 
        print(f"{str(year)}-{month}-{day}")
        break
    elif "," in date_str:
        date_arr = date_str.split()
        try:
            year = int(date_arr[2])
            day = int(date_arr[1].split(",")[0])
            month = months.index(date_arr[0]) + 1
            if day == 0 or month == 0:
                print("Invalid date. Try again.")
                continue 
        except:
            print("Invalid date. Try again.")
            continue
        year_length = len(str(year))
        if year_length < 4:
            missing_zeroes = 4 - year_length
            padding = missing_zeroes * "0"
            year = padding + str(year)
            print(year)
        if len(str(day)) == 1:
            day = "0" + str(day)
        if len(str(month)) == 1:
            month = "0" + str(month)
        if int(month) > 12 or int(day) > 31:
            print("Invalid date. Try again.")
            continue 
        print(f"{str(year)}-{month}-{day}")
        break
    else:
        print("Invalid date. Try again.")
        continue 



