import collections
import re

# # Word Count Algorithm
# def count_sentence(sentence):
#     sentence = sentence.decode('utf-8', 'ignore')
#     sentence = sentence.split()
#     io = collections.defaultdict(int)
#     exp = ' '
#     for word in sentence:
#         word = word.replace(u'\U0001f596', ' ')
#         word = word.lower()
#         exp += " " + word
#     sentence = re.sub(r'[!&@$%^&:,_.]+', ' ', exp)
#     sentence = sentence.split()
#     for word in sentence:
#         io[word] += 1
#     return io

# Word Count Algorithm
def count_sentence(sentence):
    # sentence = sentence.decode('utf-8', 'ignore')
    # sentence = sentence.split()
    # io = collections.defaultdict(int)
    # exp = ' '
    # for word in sentence:
    #     word = word.replace(u'\U0001f596', ' ')
    #     word = word.lower()
    #     exp += " " + word
    # sentence = re.sub(r'[!&@$%^&:,_.]+', ' ', exp)
    # sentence = sentence.split()
    # for word in sentence:
    #     io[word] += 1
    # return io

    # Convert Sentence To Lower Case & Split
    sentence = sentence.lower().split()

    # Declare Results Dictionary
    results = {}

    # Return Results
    return sentence

# Check Code Results
print(count_sentence("That's the password: 'PASSWORD 123'!, cried the Special Agent.\nSo I fled"))
