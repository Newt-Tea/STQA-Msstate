def test_BMI_value():
    BMI = BMI("5 10", 150)
    assert BMI == 21.5

    BMI = BMI("6 0", 200)
    assert BMI == 27.1

    BMI = BMI("5 5", 120)
    assert BMI == 20.0

def test_BMI_category():
    assert BMI_category(0.0) == "Underweight"
    assert BMI_category(18.4) == "Underweight"
    assert BMI_category(18.5) == "Normal weight"
    assert BMI_category(24.9) == "Normal weight"
    assert BMI_category(25.0) == "Overweight"
    assert BMI_category(29.9) == "Overweight"
    assert BMI_category(30.0) == "Obese"
    assert BMI_category(100.0) == "Obese"