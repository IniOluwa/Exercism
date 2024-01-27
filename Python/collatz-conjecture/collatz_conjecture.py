"""Calculate 3x + 1 Numbers"""

# Get Steps
def steps(number):

    # Check
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    # Track Steps
    steps_taken = 0

    # Loop
    while number != 1:
        # Get Collatz Conjecture Steps
        if number % 2 == 0:
            number = number // 2
            steps_taken += 1
        elif number % 2 != 0:
            number = (number * 3) + 1
            steps_taken += 1
    
    # Return Result
    return steps_taken