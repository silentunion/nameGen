import random

from ..api import db_request
from ..api import startup_requests as sr

sr.get_clusters_from_db

vowels, consonants, v_freq, c_freq = sr.get_letters_from_db()
cl_vowels, cl_consonants = sr.get_clusters_from_db()


def generate_random(**kwargs):    
    num_names = kwargs['num']
    is_weighted = kwargs['is_weighted']
    is_random = kwargs['is_random']
    min_letters = kwargs['min_letters'] if 'min_letters' in kwargs else 2
    max_letters = kwargs['max_letters'] if 'max_letters' in kwargs else 12

    names = []

    for num in range(num_names):
        name = ''

        name_length = random.randint(min_letters, max_letters)
        is_double = False
        choices = ['v', 'c']
        choice = ''
        
        for letter in range(0, name_length):
            prev_choice = choice
            choice = random.choice(choices)

            while is_double:
                if choice == prev_choice:
                    choice = random.choice(choices)
                else:
                    is_double = False

            if len(name) > 0 and choice == prev_choice:
                is_double = True

            name += choose_letter(choice, is_weighted)
        
        names.append({'name': name.capitalize()})
    
    return names

def generate_from_template(**kwargs):
    template = kwargs['template']
    num_names = kwargs['num']
    is_weighted = kwargs['is_weighted']
    is_random = kwargs['is_random']
    min_letters = kwargs['min_letters'] if 'min_letters' in kwargs else 2
    max_letters = kwargs['max_letters'] if 'max_letters' in kwargs else 12

    names = []
    is_literal = False

    for num in range(num_names):
        name = ''
        literal = ''
        for letter in range(0, len(template)):
            choice = template[letter]

            if is_literal:
                if choice == ')':
                    is_literal = False
                    name += choose_literal(literal)
                else:
                    literal += choice
            elif choice == '(':
                literal = ''
                is_literal = True
            else:
                name += choose_letter(choice, is_weighted)

        names.append({'name': name.capitalize()})

    return names

def choose_literal(literal):
    choices = literal.split('|')
    return random.choice(choices)

def choose_letter(choice, is_weighted=False):
    if choice == 'v':
        return letter_vowel(is_weighted)
    elif choice == 'c':
        return letter_consonant(is_weighted)
    elif choice == 'l':
        return letter()
    elif choice == 'V':
        return cluster_vowel()
    elif choice == ' ' or choice == '-' or choice == '\'':
        return choice
    else:
        return ''

def letter():
    return random.choice(vowels + consonants)

def letter_vowel(is_weighted):
    if is_weighted:
        return random.choices(vowels, weights=v_freq, k=1)[0]
    else:
        return random.choice(vowels)

def letter_consonant(is_weighted):
    if is_weighted:
        return random.choices(consonants, weights=c_freq, k=1)[0]
    else:
        return random.choice(consonants)

def cluster_vowel():
    return random.choice(cl_vowels)
