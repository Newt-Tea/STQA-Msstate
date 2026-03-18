import unittest

class test_BMI_value(unittest.TestCase):
    def test_BMI_value(self):
        BMI = BMI("5 10", 150)
        self.assertEqual(BMI, 21.5)

        BMI = BMI("6 0", 200)
        self.assertEqual(BMI, 27.1)

        BMI = BMI("5 5", 120)
        self.assertEqual(BMI, 20.0)

class test_BMI_category(unittest.TestCase):
    def test_BMI_category(self):
        self.assertEqual(BMI_category(0.0), "Underweight")
        self.assertEqual(BMI_category(18.4), "Underweight")
        self.assertEqual(BMI_category(18.5), "Normal weight")
        self.assertEqual(BMI_category(24.9), "Normal weight")
        self.assertEqual(BMI_category(25.0), "Overweight")
        self.assertEqual(BMI_category(29.9), "Overweight")
        self.assertEqual(BMI_category(30.0), "Obese")
        self.assertEqual(BMI_category(100.0), "Obese")

if __name__ == '__main__':
    unittest.main()