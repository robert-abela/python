#BMI Calculator
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in metres:    "))

bmi = weight / (height*height)
label = ''

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
