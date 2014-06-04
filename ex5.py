# -- coding: utf-8 --
name = "Roberto A. Hernandez"
age = 35 # not a lie
height_in = 68 # inches
inch = 2.54 # ctmeter
pound = 0.453592 #kilograms
weight_lbs = 158 # pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
height_cm = inch * height_in
weight_kg = pound *  weight_lbs
# %s is for display
#%r is for debugging and is "raw" representation

print "Let's talk about %s." % name
print "He's %r inches tall" % height_in
print "he's %d pounds heavy." % weight_lbs
print "Actually, that's not too heavy."
print "He's got %s  eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "His height in centimeters is %s." % height_cm
print "His weight in kilograms is %s." % weight_kg

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height_in, weight_lbs, age + height_in + weight_lbs)
