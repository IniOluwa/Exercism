# Check String
def is_isogram(string):
    # Check If String Is Isogram
    string = string.lower()
    repeated_chars = [letter for letter in string if string.count(letter) > 1]
    final_list = [character for character in repeated_chars if character.isalpha()]
    result = False if bool(final_list) else True
    return result