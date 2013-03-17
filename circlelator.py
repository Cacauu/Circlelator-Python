# Getting the maths stuff used for sqrt() and pi
import math

# Defining Pi (TODO: Replace with maths function Pi)
pi = math.pi

# Getting input
known_element = raw_input('What do you know about the circle? ').lower()

known_value = raw_input('How much is %s? ' % (known_element))
known_value = float(known_value)

# If diameter is entered
if known_element == 'diameter' or known_element == 'd':
	diameter = known_value
	radius = diameter/2
	circumference = pi * diameter
	area = pi * float(radius) ** 2
	
# If radius is entered
if known_element == 'radius' or known_element == 'r':
	radius = known_value
	diameter = radius * 2
	circumference = pi * float(diameter)
	area = pi * float(radius) ** 2

# If circumference is entered
if known_element == 'circumference' or known_element == 'c':
	circumference = known_value
	diameter = circumference / pi
	radius = diameter / 2
	area = pi * float(radius) ** 2

# If area is entered
if known_element == 'area' or known_element == 'a':
	area = known_value
	radius = math.sqrt(area) / math.sqrt(pi)
	
	diameter = radius * 2
	circumference = pi * float(diameter)
	
# Printing results
print "The diameter is %s" % (diameter)
print "The circumference is %s" % (circumference)
print "The radius is %s" % (radius)
print "The area is %s" % (area)