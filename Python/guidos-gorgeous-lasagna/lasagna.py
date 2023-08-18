"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# Define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40

# Consider defining the 'PREPARATION_TIME' constant
# equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2

# Define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time=EXPECTED_BAKE_TIME):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining


# Define the 'preparation_time_in_minutes()' function
# and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):

    """
    Calculate Time To Prepare All Layers.

    This funtion takes the lasagna number of layers as a parameter and 
    mutiplies that value with the designated preparation time.
    """

    layers_preparation_time = number_of_layers * PREPARATION_TIME
    return layers_preparation_time


# Define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """
    Calculate Total Elapsed Time.

    This funtion takes the lasagna number of layers as a parameter and 
    also the elapsed bake time and adds both values to aquire an accurate
    result hoe much time we have spent baking the lasagna.
    """

    preparation_time = preparation_time_in_minutes(number_of_layers)
    total_bake_time = preparation_time + elapsed_bake_time
    return total_bake_time
