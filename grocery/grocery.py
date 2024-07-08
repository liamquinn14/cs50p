items_dict = {}

def format_dict(dict):
    items_arr = []
    for item in dict:
        items_arr.append(f"{dict[item]} {item}")
    return "\n".join(items_arr)

while True:
    try:
        user_choice = input("")
    except EOFError:
        formatted_items_dict = format_dict(items_dict)
        print("\n")
        print(formatted_items_dict)
        break
    capitalised_item = user_choice.upper()
    if items_dict.get(capitalised_item):
        items_dict[capitalised_item] += 1
    else:
        items_dict[capitalised_item] = 1
    continue