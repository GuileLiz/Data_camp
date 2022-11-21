# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

# Print out the type of house
print(type(areas))

#The index is off by 1, hence first element is has index of 0
# Print out second element from areas
print(areas[1])
# Print out last element from areas
print(areas[-1])
#extracted values from a list, you can use them to perform additional calculations. 
print(areas[1] + areas[-1])

################################### 
####    Slicing and dicing    #####
###################################

# my_list[start:end]

# Use slicing to create downstairs
downstairs=areas[:6]
print(downstairs)
# Use slicing to create upstairs
upstairs=areas[6:]
print(upstairs)

#If we want to start at beginning, we can leave it blank 
print(areas[:6]==areas[0:6])
#If we want to end at last element, we can leave it blank 
print(areas[6:]==areas[6:10])
print(areas[6:]==areas[6:-1]) #For list -1 is second to the last

#Extend a list
# Add poolhouse data to areas, new list is areas_1
areas_1=areas+["poolhouse", 24.5]


# Create areas_copy
areas_copy = areas     #By doing this we are just referencing the element to variable 'areas'
print(areas_copy)
areas[-1]=10.50
print(areas_copy)

areas_copy = areas[:]  #By doing this we are assigning the element to variable 'areas'
print(areas_copy)
areas[-1]=10.50
print(areas_copy)
