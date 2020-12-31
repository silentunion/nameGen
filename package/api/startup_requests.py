from . import db_request

def get_letters_from_db():
    letters = db_request.get_letters()

    l, v, c = [], [], []
    lb, vb, cb = [], [], []
    lm, vm, cm = [], [], []
    le, ve, ce = [], [], []

    lf, vf, cf = [], [], []
    lbf, vbf, cbf = [], [], []
    lmf, vmf, cmf = [], [], []
    lef, vef, cef = [], [], []

    for row in letters:
        if row['property'] == 'None' and row['location'] == 'Any':
            l.append(row['part'])
            lf.append(float(row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'Any':
            v.append(row['part'])
            vf.append(float(row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'Any':
            c.append(row['part'])
            cf.append(float(row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'beginning':
            lb.append(row['part'])
            lbf.append(float(row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'beginning':
            vb.append(row['part'])
            vbf.append(float(row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'beginning':
            cb.append(row['part'])
            cbf.append(float(row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'middle':
            lm.append(row['part'])
            lmf.append(float(row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'middle':
            vm.append(row['part'])
            vmf.append(float(row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'middle':
            cm.append(row['part'])
            cmf.append(float(row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'end':
            le.append(row['part'])
            lef.append(float(row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'end':
            ve.append(row['part'])
            vef.append(float(row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'end':
            ce.append(row['part'])
            cef.append(float(row['frequency']))

    result = {'l' :l, 'v': v, 'c': c,
              'lb':lb,'vb':vb,'cb':cb,
              'lm':lm,'vm':vm,'cm':cm,
              'le':le,'ve':ve,'ce':ce,
              'lf' :lf, 'vf': vf, 'cf': cf,
              'lbf':lbf,'vbf':vbf,'cbf':cbf,
              'lmf':lmf,'vmf':vmf,'cmf':cmf,
              'lef':lef,'vef':vef,'cef':cef}

    return result

def get_clusters_from_db():
    clusters = db_request.get_clusters()

    cl, v, c = [], [], []
    clb, vb, cb = [], [], []
    clm, vm, cm = [], [], []
    cle, ve, ce = [], [], []

    clf, vf, cf = [], [], []
    clbf, vbf, cbf = [], [], []
    clmf, vmf, cmf = [], [], []
    clef, vef, cef = [], [], []

    for row in clusters:
        if row['property'] == 'None' and row['location'] == 'Any':
            cl.append(row['part'])
            clf.append(float(row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'Any':
            v.append(row['part'])
            vf.append(float(row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'Any':
            c.append(row['part'])
            cf.append(float(row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'beginning':
            clb.append(row['part'])
            clbf.append(float(row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'beginning':
            vb.append(row['part'])
            vbf.append(float(row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'beginning':
            cb.append(row['part'])
            cbf.append(float(row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'middle':
            clm.append(row['part'])
            clmf.append(float(row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'middle':
            vm.append(row['part'])
            vmf.append(float(row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'middle':
            cm.append(row['part'])
            cmf.append(float(row['frequency']))

        elif row['property'] == 'None' and row['location'] == 'end':
            cle.append(row['part'])
            clef.append(float(row['frequency']))
        elif row['property'] == 'vowel' and row['location'] == 'end':
            ve.append(row['part'])
            vef.append(float(row['frequency']))
        elif row['property'] == 'consonant' and row['location'] == 'end':
            ce.append(row['part'])
            cef.append(float(row['frequency']))

    result = {'cl' :cl, 'v': v, 'c': c,
              'clb':clb,'vb':vb,'cb':cb,
              'clm':clm,'vm':vm,'cm':cm,
              'cle':cle,'ve':ve,'ce':ce,
              'clf' :clf, 'vf': vf, 'cf': cf,
              'clbf':clbf,'vbf':vbf,'cbf':cbf,
              'clmf':clmf,'vmf':vmf,'cmf':cmf,
              'clef':clef,'vef':vef,'cef':cef}

    return result
