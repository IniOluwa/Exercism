# Rotational/Caeser Cipher
import string

def rotate(text, key):
    """Cipher Text and Return Results"""
    # Get Alphabets
    lower = string.ascii_lowercase + string.ascii_lowercase
    upper = string.ascii_uppercase + string.ascii_uppercase

    # Check Safe Keys
    if key == 0 or key == 26:
        return text

    # Rotate
    cipher = ''
    for char in text:
        if char != char.lower():
            cipher += upper[upper.index(char) + key]
        elif char.lower() not in lower:
            cipher += char
        else:
            cipher += lower[lower.index(char) + key]

    # Return
    return cipher