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

    names = []
    template = kwargs['template']
    num_names = kwargs['num']
    is_weighted = kwargs['is_weighted']
    is_random = kwargs['is_random']
    min_letters = kwargs['min_letters'] if 'min_letters' in kwargs else 2
    max_letters = kwargs['max_letters'] if 'max_letters' in kwargs else 12

    for num in range(num_names):
        if is_random:
            template = ''
            choices = ['v', 'c']
            name_length = random.randint(min_letters, max_letters)
            is_double = False
            for l in range(0, name_length):
                letter_type = random.choice(choices)
                while is_double:
                    if letter_type == template[-1]:
                        letter_type = random.choice(choices)
                    else:
                        is_double = False
                if len(template) > 0 and letter_type == template[-1]:
                    is_double = True
                template += letter_type
            
        name = ''
        for letter in range(0, len(template)):
            let = template[letter]
            if is_weighted:
                if let == 'v':
                    name += random.choices(vowels, weights=v_freq, k=1)[0]          
                else:
                    name += random.choices(consonants, weights=c_freq, k=1)[0]
            else:
                if let == 'v':
                    name += random.choice(vowels)
                else:
                    name += random.choice(consonants)
        names.append({'name': name.capitalize()})
    
    return names

