def BMI(height=None, weight=None):
    if height is None:
        height = input("Enter height in feet and inches('5,10'): ")
    if weight is None:
        weight = int(input("Enter weight in pounds: "))

    height = height.split(",")
    feet = int(height[0])
    inches = int(height[1])
    height = (feet * 12  + inches)

    BMI = round((weight * 0.45) / ((height * 0.025) ** 2), 1)
    return BMI

def BMI_category(BMI):
    if BMI <= 18.4:
        return "Underweight"
    elif BMI <= 24.9:
        return "Normal weight"
    elif BMI <= 29.9:
        return "Overweight"
    else:
        return "Obese"
    
def main():
    bmi = BMI()
    category = BMI_category(bmi)
    return bmi, category

if __name__ == "__main__":
    print(main())