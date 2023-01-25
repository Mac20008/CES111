"""
Jose Machuca: Tire volume assignment 

for this project; when you are shopping for tires, this collects the data of a tire you are looking for, then it will show you the 
volume of the tire. If you choose to buy the tire with these dimensions, it will print out the data with the date that you looked 
for the tires. If you choose not to, it will print a friendly thank you note.

"""
#import math & time data
import math
from datetime import datetime
current_date_and_time = datetime.now()
#first collect the data:
#ask the width of the tire in mm

width = input ("Enter the width of the tire in mm (ex 205): ")

#ask the tire ratio

ratio = input ("Enter the aspect ratio of the tire (ex 60): ")

#input the diameter

diameter = input ("Enter the diameter of the wheel in inches (ex 15): ")


#convert the data into integer:
w = float (width)

a = float (ratio)

d = float (diameter)

#calculate the data:

v = float (math.pi) * w ** 2 * a * (w * a + 2540 * d) / 10000000000

#print out the result of calculation.

print (f"The approximate volume is {v:.2f} liters")
print()

#This part of the project will ask if the clinet would like to print out the demisions of the tire

buy_tires = input ("would you like to buy tires with these dimensions (Yes/No)?: ")

#run if statement to print info to "volume txt file"
if buy_tires == "yes":
    phone_number = input ("please enter your phone number: ")
    with open ("volumes.txt", "at") as volume_file:

#what will print if the client says "Yes"
        print(f"Date:{current_date_and_time:%y-%m-%d}", file = volume_file)
        print(f"Width: {width}, Ratio: {ratio}, Diameter: {diameter}, Volume: {v:.2f}, Phone number: {phone_number}", file = volume_file)

else:

    with open ("volume.txt", "at" ) as volume_file:
        
#what will print if the clinet says "no"
        print (f"{current_date_and_time:%y-%m-%d}", file = volume_file)
        print ("thank you! please come again soon.", file= volume_file)

input()