def validate(input):
    result = {
        'valid': True,
        'a' : 0.0, 'b' : 0.0, 'c' : 0.0,
        'quit': False
    }
    #check for quit condition
    if(input == "quit"):
        result['quit'] = True
     #   return result
    
    #check for proper input format
    try:
        tokens = input.split(' ')
        if( len( tokens ) != 3):
            result['valid'] = False

        result['a'] = float( tokens[0] )
        result['b'] = float( tokens[1] )
        result['c'] = float( tokens[2] )

        if( result['a'] == 0 ):
            result['valid'] = False
            print("'a' cannot be zero")
            
    except:
        result['valid'] = False

    return result