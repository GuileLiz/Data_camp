################################### 
####      2D NumPy Array      #####
###################################
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out the type of np_baseball
print(np_baseball)

# Print out the shape of np_baseball
print(type(np_baseball))
print(np_baseball.shape)   
# for shape (How many row '---', How many column '|' )

###################################### 
####    2D Slicing and dicing    #####
######################################
# The indexes before the comma refer to the rows, 
# while those after the comma refer to the columns. 
# baseball is available as a regular list of lists

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb=np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])

################################
####     2D Arithmetic     #####
################################
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

np_mat * 2                      # All element are multipy by 2
np_mat + np.array([10, 5])      # 1st column add 10, 2nd column add 5
np_mat + np_mat                 # Element wise addition since same shape

##################################
####     Basic statistics    #####
##################################

import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)

stddev = np.std(x)
print("Standard Deviation: " + str(stddev))

corr = np.corrcoef(x[0],x[1])
print("Correlation: " + str(corr))