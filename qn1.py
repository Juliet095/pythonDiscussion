# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 

def Temparature_classifier():
     Temperature = float(input("Enter Temperature in Celsius degrees :"))
     Celsius_degrees= ("°C")
     if Temperature<=0:
          print("Freezing")
     elif Temperature>=0 and Temperature<=10:
          print("Cold")
     elif Temperature>=11 and Temperature<=20:
          print("Moderate")
     elif Temperature>=21 and Temperature<=30:
          print("Warm")
     else:
          print("Hot")
Temparature_classifier()

# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place
 
def volume_of_a_sphere():
     import math
     pie =math.pi
     radius = float(input("Enter the radius: "))
     volume = (4/3)*pie*radius**2
     print (f"volume_of_a_sphere with radius{radius} is {volume:.1f} ")
volume_of_a_sphere()