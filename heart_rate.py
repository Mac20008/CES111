"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

#first ask the age of the person
text = input ("please enter your age: ")

#convert the age of the person into a interger
age = int (text)

#calculate the fastest and the slowest harte rate possible
#use the user's age 
max_rate = 220 - age
slowest = max_rate * .65
fastest = max_rate * .85

#print out the result with the data
print ("When you exercise to strengthen your heart, you should")
print (f"keep your heart rate between {slowest:.0f} and {fastest:.0f}")
print ("beats per minute.")
