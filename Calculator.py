def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight (in kilograms) and height (in meters).
    Formula: BMI = weight / (height * height)
    """
    bmi = weight / (height * height)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value and return corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    print("Your BMI is:", bmi)
    print("You are categorized as:", category)

if __name__ == "__main__":
    main()
