from quad_solver.quad_solver import intro_prompt, prompt_for_abc, read_input_for_abc, solve
from quad_solver.validate import validate

def main():
    intro_prompt()
    quit_condition = False

    while( quit_condition != True ):
        prompt_for_abc()

        result = validate( read_input_for_abc() )

        if( result['quit'] == False and result['valid'] == True): #if valid input and not quit
            
            solve( **result )

        elif( result['quit'] == False ): #not quit but not valid

            print("Innappropriate input, please enter ONLY 3 space seperated numerical values")
        
        quit_condition = result['quit']
    
    #end while, user quit

    print("Goodbye!")

if __name__ == "__main__":
    main()