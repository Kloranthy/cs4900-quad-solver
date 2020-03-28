

#from quad_solver.quad_solver import intro_prompt, prompt_for_abc, read_input_for_abc, solve

from quad_solver.read_input import read_input
from quad_solver.validate import validate
from quad_solver.calculate_roots import calculate_roots

from quad_solver.messages import (
    make_program_intro_message,
    prompt_for_coefficients_message,
    invalid_input_message,
    make_solving_coefficients_message,
    make_calculate_roots_result_message
)




print( make_program_intro_message() )


while( True ):

    print( prompt_for_coefficients_message )

    input_line = read_input()

    validation_result = validate( input_line )

    if ( validation_result['quit'] ) :
        break
    # quit

    if( validation_result['valid'] == True ) :

        a = validation_result['a']
        b = validation_result['b']
        c = validation_result['c']


        solving_coefficients_message = make_solving_coefficients_message( a, b, c )

        print( solving_coefficients_message )
        

        calculation_results = calculate_roots( a, b, c )


        calculate_roots_result_message = make_calculate_roots_result_message( calculation_results )

        print( calculate_roots_result_message )
    # valid input and not quit
    else : # not quit and not valid

        print( invalid_input_message )
    # invalid input
    
# main loop


print( "Goodbye!" )

