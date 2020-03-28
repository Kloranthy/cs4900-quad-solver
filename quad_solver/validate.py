

from .predicates.abc import check_abc_values, acceptable_digits_of_precision


def validate( input ) :

    result = {
        'valid': True,
        'a' : 0.0, 'b' : 0.0, 'c' : 0.0,
        'quit': False
    }
    
    # print( f'input in validate : "{input}"' )

    if ( input == "quit" ):
        result['quit'] = True
        return result
    # quit

    
    # check for proper input format
    try :
        tokens = input.split( ' ' )

        if ( len( tokens ) != 3  ):
            result['valid'] = False
        # invalid number of tokens


        a = float( tokens[ 0 ] )
        b = float( tokens[ 1 ] )
        c = float( tokens[ 2 ] )

        abc_pred_result = check_abc_values( a, b, c )

        result['valid'] = abc_pred_result['valid']

        if ( not abc_pred_result[ 'a_is_not_zero' ] ):
            print( 'error : the \'a\' coefficient cannot be zero' )
        # show error message


        if ( not abc_pred_result['acceptable_digits_of_precision'] ):
            print( f'warning : more than {acceptable_digits_of_precision} digits of precision' )
        # show warning message


        result['a'] = a
        result['b'] = b
        result['c'] = c
            
    except :
        result['valid'] = False
    

    return result
# validate
