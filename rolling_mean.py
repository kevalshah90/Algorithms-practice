# Running / rolling mean algorithm
import statistics
import numpy as np

input_list = [1, 4, 2, 3, -10, 3, 2, 5, 50, 20, 3, 5, 13, 20]

window_size = 5

#output_list = [0.0, 0.4, 0.0, 0.6, 10.0, 16.0, 16.0, 16.6, 18.2, 12.2]


# Function to calculate running mean
def running_mean(input_list, window_size):

    # Declare output list
    output_list = []

    # calculate rolling mean
    if len(input_list) >= window_size: 


        for i in range(window_size, len(input_list), 1):

            s1 = np.mean(input_list[i-window_size : i]) 

            output_list.append(s1)  
            
    return output_list



running_mean(input_list, window_size)
