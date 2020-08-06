#The weight of a person
user_input = input("Enter your weight in kg: ")
kg = float(user_input)

#ID number
id_num = input("Enter your ID card number: ")

#Telephone Number
user_input = input("Enter your telephone number: ")
tel = int(user_input)

#Address
address = input("Enter your address: ")

#Date of birth
dob = input("Enter your date of birth: ")

#Bank Account balance
user_input = input("Enter your account balance: ")
balance = float(user_input)

#The height of a person
user_input = input("Enter your height: ")
height = float(user_input)

#A Maltese number plate
plate = input("Enter your car number plate: ")

print()
print("-"*80)
print("%s\n\t%d\n\t%s\n\t%s\n\t€ %.2f\n\t%.2f m\n\t%.2f kg\n\t%s" 
	% (id_num, tel, address, dob, balance, height, kg, plate))

data = {}
data['id'] = id_num
data['tel'] = tel
data['addr'] = address
data['dob'] = dob
data['bal'] = balance
data['height'] = height
data['weight'] = kg
data['plate'] = plate

print()
print("-"*80)
print(data)
