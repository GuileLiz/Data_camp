# in datacamp, it is assume that the value was already importer

# Python lists store a collection of ordered, alterable data objects, 
# NumPy arrays only store a single type of object.

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in=np.array(height_in)

# Print out np_height_in
print(np_height_in)
##############################################################
#####   Numpy array have element by element operation    #####
##############################################################
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg=np.array(weight_lb)*0.453592

# Calculate the BMI: bmi
bmi=np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)

####################################################
#####  Used boolean to express element that    #####
#####         we only want to return           #####
####################################################
light=np.array(bmi)<21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
# Value that is will return
print(bmi[light]) 

###################################### 
####    1D Slicing and dicing    #####
######################################
# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

