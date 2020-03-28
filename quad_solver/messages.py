
# move to another file?
program_version = '0.0.1'



program_intro_message_template = (
    'Welcome to Qsolver  v{program_version} \n'
    'This program allows you to enter the coefficients '
    'of a quadratic function, and finds the real roots '
    'of that function if any exist. \n'
)


def make_program_intro_message() :

    message = (
        program_intro_message_template
        .format(
            program_version = program_version
        )
    )

    return message
# make_program_intro_message



prompt_for_coefficients_message = 'Please enter input as space seperated numerical values.'


invalid_input_message = 'Innappropriate input, please enter exactly 3 space seperated numerical values for the coefficients or "quit" to terminate the program.'



solving_coefficients_message_template = 'Solving : {a}x^2 {b_sign} {b}x {c_sign} {c} = 0'


def make_solving_coefficients_message( a, b, c ):

    b_sign = '+' if ( b >= 0 ) else '-'
    c_sign = '+' if ( c >= 0 ) else '-'

    message = (
        solving_coefficients_message_template
        .format(
            a = a,
            b_sign = b_sign,
            b = abs( b ),
            c_sign = c_sign,
            c = abs( c )
        )
    )

    return message
# make_message_for_calculate_roots_result




calculate_roots_result_no_real_roots_message = 'no real roots'


def make_calculate_roots_result_message( roots ):


    num_roots = len( roots )

    message = ''


    if ( num_roots == 0 ):

        message = calculate_roots_result_no_real_roots_message

    # num_roots == 0
    elif ( num_roots == 1 ):

        x1 = roots[ 0 ]

        message = 'x1 : {}'.format( x1 )

    # num_roots == 1
    else:  # ( num_roots == 2 ):

        x1 = roots[ 0 ]
        x2 = roots[ 1 ]

        message = 'x1 : {}, x2 : {}'.format( x1, x2 )

    # num_roots == 2


    # additional info such as warnings about stability
    # would be appended here


    message += '\n'


    return message
# make_calculate_roots_result_message
