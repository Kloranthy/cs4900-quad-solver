from modules import models
from mathModules import solve
from time import sleep


def main():
    models.intro()
    result_dict = models.validate(models.getline())
    #main loop start
    while(result_dict['quit'] != True):
        
        sleep(3)
        
        if( result_dict['valid'] ):
            solve.solve(**result_dict)
        else:
            print("Innappropriate input, please enter ONLY 3 space seperated numerical values")

        result_dict = models.validate( models.getline() )
    #main loop end 

    print("Goodbye!")
if __name__ == "__main__":
    main()