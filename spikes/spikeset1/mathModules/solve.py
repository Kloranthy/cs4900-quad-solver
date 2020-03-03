from math import sqrt

def solve(**data):
    print(f"Solving valid: {data['valid']} - { data['a'] }x^2 + { data['b'] }x + { data['c'] } = 0")

def discrim(a, b, c):
    disc_info = {
        'valid': True,
        'value': 0
    }
    v = b * b - (4* a * c)
    if( v < 0 ):
        disc_info['valid'] = False
    
    disc_info['value'] = v

    return disc_info