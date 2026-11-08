try:
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
except ValueError:
    print("Invalid input: enter height and weight as numbers.")
    raise SystemExit

if height <= 0 or weight <= 0:
    print("Invalid input: height and weight must be greater than zero.")
    raise SystemExit

# WHO BMI classification for adults
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print("You are overweight")
else:
    print("You are obese")
