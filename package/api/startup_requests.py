from . import db_request

def get_letters_from_db():
    letters = db_request.get_letters()

    l, v, c = [], [], []
    lb, vb, cb = [], [], []
    lm, vm, cm = [], [], []
    le, ve, ce = [], [], []

    for row in letters:
        if row['property'] == 'None' and row['location'] == 'Any':
            l.append((row['part'], row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'Any':
            v.append((row['part'], row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'Any':
            c.append((row['part'], row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'beginning':
            lb.append((row['part'], row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'beginning':
            vb.append((row['part'], row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'beginning':
            cb.append((row['part'], row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'middle':
            lm.append((row['part'], row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'middle':
            vm.append((row['part'], row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'middle':
            cm.append((row['part'], row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'end':
            le.append((row['part'], row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'end':
            ve.append((row['part'], row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'end':
            ce.append((row['part'], row['frequency']))

    result = {'l' :l, 'v': v, 'c': c,
              'lb':lb,'vb':vb,'cb':cb,
              'lm':lm,'vm':vm,'cm':cm,
              'le':le,'ve':ve,'ce':ce}

    return result

def get_clusters_from_db():
    clusters = db_request.get_clusters()

    cl, v, c = [], [], []
    clb, vb, cb = [], [], []
    clm, vm, cm = [], [], []
    cle, ve, ce = [], [], []

    for row in clusters:
        if row['property'] == 'None' and row['location'] == 'Any':
            cl.append((row['part'], row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'Any':
            v.append((row['part'], row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'Any':
            c.append((row['part'], row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'beginning':
            clb.append((row['part'], row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'beginning':
            vb.append((row['part'], row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'beginning':
            cb.append((row['part'], row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'middle':
            clm.append((row['part'], row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'middle':
            vm.append((row['part'], row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'middle':
            cm.append((row['part'], row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'end':
            cle.append((row['part'], row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'end':
            ve.append((row['part'], row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'end':
            ce.append((row['part'], row['frequency']))

    result = {'l' :cl, 'v': v, 'c': c,
              'lb':clb,'vb':vb,'cb':cb,
              'lm':clm,'vm':vm,'cm':cm,
              'le':cle,'ve':ve,'ce':ce}

    return result
