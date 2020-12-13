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


def generate(num_words=5, is_weighted=False, is_random=True, template=''):
    vowels, consonants, v_freq, c_freq = get_letters_from_db()

    choices = ['v', 'c']
    template = template
    words = []

    for num in range(num_words):
        if is_random:
            template = ''
            word_length = random.randint(2, 12)
            for l in range(0, word_length):
                template += random.choice(choices)
            
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

