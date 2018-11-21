def readsettings(filename):
    settings = {}
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        key, val = tuple(line.strip(',').strip().split(': '))
        key = key.strip('"')
        if val[0]=='"':
            val = val.strip('"')
        elif val=='None':
            val = None
        else:
            val = float(val.strip('"'))
        settings[key] = val
    return settings

def writesettings(settings, filename):
    with open(filename,'w') as f:
        for key, val in settings.items():
            f.write('"%s": ' % key)
            if type(val) == type('string'):
                f.write('"%s"\n' % val)
            else:
                f.write('%s\n' % str(val))
    return True
