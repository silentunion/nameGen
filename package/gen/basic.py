import random
import json

from ..api import db_request

def generate():
    letters = db_request.get_letters()

    vowels, consonants = [], []

    for row in letters:
        if row['is_vowel']:
            vowels.append(row['letter'])
        else:
            consonants.append(row['letter'])

    template = 'cvcvcv'
    words = []
    num_words = 10

    for num in range(num_words):
        word = ''
        for letter in range(0, len(template)):
            let = template[letter]
            if let == 'v':
                word += random.choice(vowels)
            else:
                word += random.choice(consonants)
        words.append({'word': word})
    
    words_json = json.dumps(words)
    return words
