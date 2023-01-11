#tire volume assignment

#first collect the data:
#ask the width of the tire in mm

width = input ("Enter the width of the tire in mm (ex 205): ")

#ask the tire ratio

ratio = input ("Enter the aspect ratio of the tire (ex 60): ")

#input the diameter

diameter = input ("Enter the diameter of the wheel in inches (ex 15): ")

#import pi 
import math
#convert the data into integer:
w = float (width)

a = float (ratio)

d = float (diameter)

#calculate the data:

v = float (math.pi) * w ** 2 * a * (w * a + 2540 * d) / 10000000000

#print out the result of calculation.

print (f"The approximate volume is {v:.2f} liters")