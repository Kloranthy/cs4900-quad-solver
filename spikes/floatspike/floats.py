#this is a spike to demonstrate floating point inaccuracies and how to fix them
import signal
from sigcatch import sigint_catch
from math import floor

def truncate(f, prec):
    return floor(f * (10 ** prec) ) / (10 ** prec)
    #raises by prec decimal places, truncates, then brings back down prec decimal places


def main():
    signal.signal(signal.SIGINT, sigint_catch)

    print("Spike to explore floating point accuracy/errors")
    print("Press ctrl-c to exit")

    while( 1 ):
        ui = input('Enter a floating point number: ') 
        a = format(float(ui), '.27f')

        print(ui + ' with 27 decimal precision: ' + str(a) )
        print("now we use math.floor to truncate to 4 decimal places")

        print("giving us: " + str(truncate(float(ui), 4)) )


if __name__ == "__main__":
    main()
