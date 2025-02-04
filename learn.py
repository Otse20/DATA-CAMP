# Hit run code to see the output!
print(5 / 8)


savings = 100 
print(savings)


monthly_savings = 10
num_months = 4 
new_savings = 10*4
print(new_savings)


half=0.5
print(half)


intro= "Hello! How are you?"
print(intro)
is_good=True
print(is_good)

savings = 100
new_savings = 40

total_savings = 100 + 40
print(total_savings)

# Print the type of total_savings
print(type)


intro = "Hello! How are you?"

doubleintro = intro + intro
print(doubleintro)

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = [hall, kit, liv, bed, bath]


print(areas)

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)


house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"


# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]


areas_1 = areas + ["poolhouse" , 24.5]


areas_2 = areas_1 + ["garage" , 15.45]

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
print(areas)
del areas[10]
print(areas)

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy =list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)


# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type((var1)))

# Print out length of var1
print(len((var1)))

# Convert var2 to an integer: out2
out2 = int(var2)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse =True)

# Print out full_sorted
print(full_sorted)

# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()


# Print out place and place_up
print(place)
print(place_up)


# Print out the number of o's in place
o_count = place.count ('o')
print(o_count)


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append( 24.5)
areas.append(15.45)





# Print out areas
print (areas)


# Reverse the orders of the elements in areas
areas.reverse()


# Print out areas
print (areas)


# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))


# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

