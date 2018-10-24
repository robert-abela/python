def input_number():
    while True:
        try:
            string = input("Enter a number: ")
            num = int(string)
            return num
        except ValueError:
            print("Not a valid numner, try again!")

number = input_number()
