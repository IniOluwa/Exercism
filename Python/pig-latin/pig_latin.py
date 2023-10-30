import string

# Get Alphabets
alphabets = string.ascii_lowercase
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_sounds = ('xr', 'yt')
consonants = [letter for letter in [*alphabets] if letter not in vowels]

# Check To Differentiate Vowels From Consonants
def check_word(word):
    word_status = []
    for letter in word:
        if letter in vowels:
            word_status.append('v')
        if letter in consonants:
            word_status.append('c')
    return word_status

# Translate To Pig Latin
def translate(text):
    words = text.lower().split()
    sentence = []
    for word in words:
        word_check = check_word(word)
        try:
            if 'y' in word and 'v' not in word_check:
                sentence.append(word[word.index('y'):] + 
                word[:word.index('y')] + 'ay')
            if word.startswith(vowels) or word.startswith(vowel_sounds):
                sentence.append(word + 'ay')
            elif word_check.index('v') and word[word_check.index('v')
            ] == 'u' and word[word_check.index('v')-1] == 'q':
                sentence.append(word[word.index('u')+1:] + 
                word[:word.index('u')+1] + 'ay')
            elif word_check.index('v'):
                sentence.append(word[word_check.index('v'):] + 
                word[:word_check.index('v')] + 'ay')
        except Exception as e:
            pass
    return ' '.join(sentence)