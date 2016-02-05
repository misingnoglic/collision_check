from __future__ import division # real division instead of integer division
from random import SystemRandom
import time
from math import sqrt, ceil

def check_collisions(upper_bound):
    """
    Function that keeps guessing random numbers 1 to N incluside, until it hits a collision (or doesn't)
    """
    cryptogen = SystemRandom() # OS Internal system for generating cryptographic random numbers
    already_found = set([]) # Set of numbers the adversary already found
    iterations = 1
    start = time.time()
    found = False
    try:
        while not found: # Runs until a collision is found
            item = cryptogen.randrange(1,upper_bound) # Uses the cryptographically secure PRNG to generate a random number
            if item in already_found: # If it's in the set of things already found - print the statistics
                found = True
                print "duplicate found in %.2e tries in %f seconds" % (iterations, time.time()-start)
                print "The upper bound on this probability is %.2f %%" % (coll(iterations,upper_bound)*100)
            else: # If it's a new number, add it to the set of numbers checked
                already_found.add(item)
                iterations+=1
    except KeyboardInterrupt: # If someone cancels the program midway - prints some statistics about the current progress
        total_time = time.time()-start
        print "Program cancelled - made %.2e attempts in %.4f seconds" % (iterations, total_time)
        print "The upper bound on getting a duplicate is %.2f %%" % (coll(iterations,upper_bound)*100)
        onepercent = ntimes(.01,upper_bound)
        rate = total_time/iterations
        seconds = onepercent*rate
        print "To have 1%% probability of guessing you need at least %d tries, at this rate it would take %f seconds" % (onepercent, seconds)
        print "%.2f minutes, %.2f hours, %.2f days, %.2f years" % (seconds/60, seconds/60/60, seconds/60/60/24, seconds/60/60/24/365)
            
            
def coll(q,N):
    """
    Upper bound on the probability of a collision with q items chosen with an upper bound of N
    """
    return float((q**2)/(2*N))
    
def ntimes(P,N):
    """
    Similar to coll - but the equation is solved for q, not the probability. 
    This is the lower bound of items needed to check for P probability of finding a collision from random numbers
    """
    return ceil(sqrt(2*N*P))