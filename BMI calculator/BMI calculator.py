height = float(input("Enter your height in meters"))
weight = float(input("Enter your weight in kilograms"))
BMI = weight/(height*height)
print(f"your BMI is{BMI}")
if BMI <18.5:
  print("you are underweight")
if BMI>=18.5 and BMI<=24.9:
  print("you are normal weight")
if BMI>24.9 and BMI<=29.9:
  print("you are over weight")
if BMI>=30:
  print("you are obese")
