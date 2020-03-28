

from quad_solver.quad_solver import intro_prompt, prompt_for_abc, read_input_for_abc, solve

from quad_solver.validate import validate


intro_prompt()
quit_condition = False

while( not quit_condition ):
    prompt_for_abc()

    result = validate( read_input_for_abc() )

    if ( result['quit'] ) :
        quit_condition = True
        continue
    # quit

    if( result['valid'] == True ): #if valid input and not quit
        
        solve( result )

    else: #not quit but not valid

        print("Innappropriate input, please enter ONLY 3 space seperated numerical values")
    

#end while, user quit

print("Goodbye!")

