def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/(height**2)
    print("BMI = " + str(bmi))
    if bmi<18.5:
        print("you are underweight")
        return -1
    elif bmi>25: 
        print("you are overweight")
        return 1
    else:
        print("you are normalweight")
        return 0
    
calculate_bmi(weight=57, height=1.73)
calculate_bmi(weight=37, height=1.73)
calculate_bmi(weight=97, height=1.73)