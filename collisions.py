from __future__ import division
from random import SystemRandom
import time
from math import sqrt, ceil

def check_collisions(N):
    """
    Function that keeps guessing random numbers 1 to N incluside, until it hits a collision (or doesn't)
    """
    cryptogen = SystemRandom() # OS Internal system for generating cryptographic random numbers
    already_found = set([]) # Set of numbers the adversary already found
    iterations = 1
    start = time.time()
    try:
        while True:
            item = cryptogen.randrange(1,N)
            if item in already_found: 
                print "duplicate found in %.2e tries in %f seconds" % (iterations, time.time()-start)
                print "The upper bound on this probability is %.2f %%" % (coll(iterations,N)*100)
                return
            else:
                already_found.add(item)
                iterations+=1
    except KeyboardInterrupt:
        total_time = time.time()-start
        print "Program cancelled - made %.2e attempts in %.4f seconds" % (iterations, total_time)
        print "The upper bound on getting a duplicate is %.2f %%" % (coll(iterations,N)*100)
        onepercent = ntimes(.01,N)
        rate = total_time/iterations
        print "To have 1%% probability of guessing you need at least %d tries, at this rate it would take %f seconds" % (onepercent, onepercent*rate)
        raise
            
            
def coll(q,N):
    return float((q**2)/(2*N))
    
def ntimes(P,N):
    return ceil(sqrt(2*N*P))