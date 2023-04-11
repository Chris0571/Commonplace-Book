"""
Functions used in preparing Guido's gorgeous lasagna.
Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven
    as an argument and returns how many minutes the lasagna still needs to
    bake based on the `EXPECTED_BAKE_TIME`.
    """
    remain = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remain

    pass


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.

def preparation_time_in_minutes(number_of_layers):
    """each layer takes 2 minutes
    time = layer * 2
    """
    time = number_of_layers * 2
    return time

#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_time_in_minutes: int - baking time already elapsed + numer of layers.
    :return: int - total time elapsed (in minutes).
    """
    total = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total
    