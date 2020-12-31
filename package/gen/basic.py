import random

from ..api import db_request
from ..api import startup_requests as sr

sr.get_clusters_from_db

letters = sr.get_letters_from_db()
clusters = sr.get_clusters_from_db()


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
    if choice == 'l':
        return get_letter('l', 'lf', is_weighted)
    elif choice == 'v':
        return get_letter('v', 'vf', is_weighted)
    elif choice == 'c':
        return get_letter('c', 'cf', is_weighted)

    elif choice == 'V':
        return get_cluster('v', 'vf', is_weighted)
    elif choice == 'C':
        return get_cluster('cl', 'clf', is_weighted)

    elif choice == 'b':
        return get_cluster('vb', 'vbf', is_weighted)    
    elif choice == 'm':
        return get_cluster('vm', 'vmf', is_weighted)
    elif choice == 'e':
        return get_cluster('ve', 'vef', is_weighted)

    elif choice == 'B':
        return get_cluster('cb', 'cbf', is_weighted)    
    elif choice == 'M':
        return get_cluster('cm', 'cmf', is_weighted)
    elif choice == 'E':
        return get_cluster('ce', 'cef', is_weighted)

    elif choice == ' ' or choice == '-' or choice == '\'':
        return choice
    else:
        return ''

def get_letter(l, freq, is_weighted):
    if is_weighted:
        return random.choices(letters[l], weights=letters[freq], k=1)[0]
    else:
        return random.choice(letters[l])

def get_cluster(c, freq, is_weighted):
    if is_weighted:
        return random.choices(clusters[c], weights=clusters[freq], k=1)[0]
    else:
        return random.choice(clusters[c])
