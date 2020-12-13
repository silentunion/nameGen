import random

from ..api import db_request


def get_letters_from_db():
    letters = db_request.get_letters()

    vowels, consonants, v_freq, c_freq = [], [], [], []

    for row in letters:
        if row['is_vowel']:
            vowels.append(row['letter'])
            v_freq.append(float(row['frequency']))
        else:
            consonants.append(row['letter'])
            c_freq.append(float(row['frequency']))

    return vowels, consonants, v_freq, c_freq


def generate(**kwargs):
    vowels, consonants, v_freq, c_freq = get_letters_from_db()

    words = []
    template = kwargs['template']
    num_words = kwargs['num']
    is_weighted = kwargs['is_weighted']
    is_random = kwargs['is_random']

    for num in range(num_words):
        if is_random:
            template = ''
            choices = ['v', 'c']
            word_length = random.randint(2, 12)
            is_double = False
            for l in range(0, word_length):
                letter_type = random.choice(choices)
                print('letter', letter_type)
                while is_double:
                    print('checking double', letter_type, template[-1])
                    if letter_type == template[-1]:
                        letter_type = random.choice(choices)
                    else:
                        is_double = False
                if len(template) > 0 and letter_type == template[-1]:
                    print('setting double')
                    is_double = True
                template += letter_type
                print('template:', template)
            
        word = ''
        for letter in range(0, len(template)):
            let = template[letter]
            if is_weighted:
                if let == 'v':
                    word += random.choices(vowels, weights=v_freq, k=1)[0]          
                else:
                    word += random.choices(consonants, weights=c_freq, k=1)[0]
            else:
                if let == 'v':
                    word += random.choice(vowels)
                else:
                    word += random.choice(consonants)
        words.append({'name': word.capitalize()})
    
    return words

