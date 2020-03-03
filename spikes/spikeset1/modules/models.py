import sys, curses


def intro():
    print("Welcome to Qsolver!")
    print("This program allows you to enter the coefficients of a quadratic")
    print("function, and finds the real roots of that function if any exist.")
    print("Please enter input as space seperated numerical values.")


def getline():
    print("Enter 'quit' to exit program")
    abc_line = input("Enter a, b, c: ")
    return abc_line

def validate(input):
    result = {
        'valid': True,
        'a' : 0.0, 'b' : 0.0, 'c' : 0.0,
        'quit': False
    }
    #check for quit condition
    if(input == "quit"):
        result['quit'] = True
        return result
    
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



