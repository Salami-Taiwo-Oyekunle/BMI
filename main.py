weight=float(input('Enter your weight in kg'))
height=float(input('Enter your height in mtr'))
bmi=weight/height**2
if bmi<18.5:
        print('You are under weight')
elif bmi<25:
        print('You are healthy')
elif bmi<30:
        print('You are over weight')
elif bmi<38:
        print('You are severely over weight')
elif bmi<40:
        print('You are obess')
else:
        print('You are severerly obess')