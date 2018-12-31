# last year was so random
# that I'm bound to
import random

# only one thing kept going
# and I've to 
import time


while True:

    cur_t = time.localtime()

    # sleep before 11
    if(cur_t.tm_hour < 23):
        
        hdiff=24-cur_t.tm_hour
        time.sleep(hdiff*60*60)

    # sleep till last minute
    elif(cur_t.tm_min<59):

        mdiff=59-cur_t.tm_min
        time.sleep(mdiff*60)

    # else wish me
    else:

        print('\n BOOM !! CONGRATS FOR SURVIVING ONE MORE YEAR !')
        print('\n')
        print('                 -__-                  ')
        print('%     YOU HAVE HAD AN AWESOME 2018    %')
        print('                 -__-                  ')
        print('\n')
   
        print('Its time for RESOLUTION !!')
        time.sleep(2)
        print('\nLet me choose a RESOLUTION for you !')
        print('................')
        time.sleep(2)
        print('................')
        time.sleep(2)
        print('................')
        print('DONE')
        time.sleep(2)

        print('\n%%      HERS IS YOUR RESOLUTION      %%')

        res=['Come on start a Startup and become CEO','Go to Foreign Trip','Join Google as ML \
        Engineer', 'No girlfriend this year please !!', 'Start sticking to your commitiment \
        boy','Read 4 books a month, that makes 48 books a year + 2 bonus = 50 books','Practice \
        GUITAR Daily, come on man thats fun !!']

        rn=random.randint(0,len(res))
        print("====> "+res[rn-1]+" <====")
        time.sleep(3)
        print('\n')
        print('        MAKE SURE YOU FOLLOW IT        ')
        print('       RELAX AND HAVE A GOOD SLEEP     ')
        print('                 -__-                  ')
        print('\n')

######################################## that's it ###########################################