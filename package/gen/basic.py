import random

from ..api import db_request

def get_letters_from_db():
    letters = db_request.get_letters()

    vowels, consonants = [], []

    for row in letters:
        if row['is_vowel']:
            vowels.append(row['letter'])
        else:
            consonants.append(row['letter'])

    return vowels, consonants


def generate(template, num_words):
    vowels, consonants = get_letters_from_db()

    template = template
    words = []

    for num in range(num_words):
        word = ''
        for letter in range(0, len(template)):
            let = template[letter]
            if let == 'v':
                word += random.choice(vowels)
            else:
                word += random.choice(consonants)
        words.append({'word': word})
    
    return words


def completely_random(num_words):
    vowels, consonants = get_letters_from_db()

    choices = ['v', 'c']
    words = []

    for num in range(num_words):
        template = ''
        word = ''

        word_length = random.randint(2, 12)
        for l in range(0, word_length):
            template += random.choice(choices)

        for letter in range(0, len(template)):
            let = template[letter]
            if let == 'v':
                word += random.choice(vowels)
            else:
                word += random.choice(consonants)
        words.append({'word': word})
    
    return words
