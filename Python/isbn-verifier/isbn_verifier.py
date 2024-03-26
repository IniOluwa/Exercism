"""Check If Number Is ISBN 10"""
def is_valid(isbn):
    # Replace Hypens(If Any)
    isbn = isbn.replace('-', '')
    
    # Run Checks 
    letter_check = [str(value) for value in isbn if not value.isdigit() and value != 'X' or (value == 'X' and isbn.index(value) != len(isbn) - 1)]
    if len(isbn) > 10 or len(isbn) < 10 or any(letter_check):
        return False
    
    # Combine Values
    isbn = list(isbn)
    x_index = None if 'X' not in isbn else isbn.index('X')
    if x_index: isbn[x_index] = 10
    isbn_zip = zip(isbn, list(range(1, 11))[::-1])
    
    # Check ISBN 10 Status
    isbn_status = True if (sum([int(value) * number for value, number in isbn_zip]) % 11 == 0) else False

    # Return
    return isbn_status