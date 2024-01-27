# Detremine If a Number is ArmStrong
def is_armstrong_number(number):
    # Resolve Number
    str_num_list = list(str(number))
    num_list = [int(x)**len(str_num_list) for x in str_num_list]
    
    # Check If Number is ArmStrong
    if sum(num_list) == number:
        return True
    return False