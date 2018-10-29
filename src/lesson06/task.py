import random

def read_float(msg):
    while True:
        try:
            n1 = float(input(msg))
        except ValueError:
            print('Cannot convert input to a float, try again!')
        else:
            return n1

def bmi():
    height = read_float('Enter height in metres:    ')
    weight = read_float('Enter weight in kilograms: ')
    try:
        bmi = weight / (height*height)
        if (bmi < 18.5):
            label = 'underweight'
        elif bmi < 25:
            label = 'normal'
        elif bmi < 30:
            label = 'overweight'
        elif bmi < 35:
            label = 'obese'
        else:
            label = 'extremely obese'

        print("Your BMI is %.1f (%s)" % (bmi, label))
    except ZeroDivisionError:
        print("Height cannot be zero!")

def lotto():
    result = []
    while len(result) < 5:
        randomnum = random.randint(1,90)
        if randomnum not in result:
            result.append(randomnum)
    print('Lotto results:', result)

def word_counter():
    chars = alphabet = vowels = words = 0
    user_string = input('Enter some text: ')
    for ch in user_string.lower():
        chars += 1
        if ch.isalpha():
            alphabet += 1
        if ch in 'aeiou':
            vowels += 1
        if ch == ' ':
            words += 1

    print('%d words, %d characters, %d alphabetical & %d vowels' %
          ((words+1), chars, alphabet, vowels))

def my_feature():
    print('Not implemented yet')
    
def menu():
    while True:
        print('\n\n\n------------------------------------------------------')
        print('Welcome to my menu-driven, choose one of the following')
        print('1. BMI calculator')
        print('2. Lottery draw')
        print('3. Word counter')
        print('4. Your feature')
        print('5. Quit')
        choice = input('Enter option: ')
        if choice == '1':
            bmi()
        elif choice == '2':
            lotto()
        elif choice == '3':
            word_counter()
        elif choice == '4':
            my_feature()
        elif choice == '5':
            break
        else:
            print('Invalid input')

if __name__ == "__main__":
    menu()
