def main():
    user_input = input("Input: ")
    shortened_str = shorten(user_input)
    print(shortened_str)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    without_vowels = ""
    for letter in word:
        if letter.lower() not in vowels:
            without_vowels += letter
    return without_vowels
    


if __name__ == "__main__":
    main()