from . import db_request

def get_letters_from_db():
    letters = db_request.get_letters()

    vowels, consonants, v_freq, c_freq = [], [], [], []

    for row in letters:
        if row['property'] == 'vowel':
            vowels.append(row['part'])
            v_freq.append(float(row['frequency']))
        else:
            consonants.append(row['part'])
            c_freq.append(float(row['frequency']))

    return vowels, consonants, v_freq, c_freq

def get_clusters_from_db():
    clusters = db_request.get_clusters()
    cl_vowels, cl_consonants = [], []

    for row in clusters:
        if row['property'] == 'vowel':
            cl_vowels.append(row['part'])
        else:
            cl_consonants.append(row['part'])

    return cl_vowels, cl_consonants
