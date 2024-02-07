def bmi():
    weight = input('Input your weight (in kg): ')
    height = input('Input your height (in meters): ')
    return print('Your BMI is: ', float(weight)/float(height))

# not much to explain; simply divide weight by height to get BMI

bmi()
