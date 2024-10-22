# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 
 
def calculate_BMI():
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))
    BMI = (weight/height)
    if BMI<18.5:
        print("uderweight")
    elif BMI>=18.5 and BMI<=24.9:
        print("Normal weight")
    elif BMI >= 25 and BMI<=29.9:
       print("Overweight")
    else:
       print("obese")
calculate_BMI()


# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h.
#  Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters.
#  Make sure you use the real pie value (import math)

def volume_of_cylinder():
    import math
    pie = math.pi
    r =("radius")
    h = ("height")
    r= float(input("Enter the radius "))
    h = float(input("Enter the height "))
    v = pie*r**2*h
    print(f"volume_of_cylinder with radius {r} and height {h} is:{v} ")
volume_of_cylinder()