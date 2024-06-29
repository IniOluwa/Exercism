import re

def answer(question):
    
    # Get Signs
    signs = {'plus': '+', 'minus': '-', 'multiplied by': '*', 'divided by': '/'}

    # Check Numbers
    numbers = any(value.isdigit() for value in question)
    if not numbers and question.startswith('What is'):
        raise ValueError('syntax error')

    # Parse
    for sign, symbol in signs.items():
        question = question.replace(sign, symbol)
        question = question.replace('What is ', '')
        question = question.replace('?', '')

    # Validate Question After Parse
    pattern = '([0-9]|[\-+*])+'
    match = re.search(pattern, question)
    if (not match or not any(value in signs.values() for value in question.split()
                            ) and len(question.split()) > 1):
        raise ValueError('unknown operation')

    try:
        ques = question.split(' ')
        if len(ques) <= 3:
            return eval(question)
        left = eval(' '.join(ques[:3]))
        right = ' '.join(ques[3:])
        return eval(' '.join([str(left), right]))
    except SyntaxError:
        raise ValueError('syntax error')