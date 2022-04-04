#!/usr/bin/env python3
import time
import pulsar

"""
    The implementation is used to demonstrate an intensive "conversion" function on elements
"""

# Fill in your author information
___author___ = "Lovisa Hedman"
___email____ = ""

# Input string
INPUT_STRING = "I want to be capatilized"

# Iteration represents the operation applied to each word in the string 
# e.g., 1 represents that operation is applied to first word in the string
ITERATION = 5



if __name__ == "__main__":

    # Check for correct input
    if ITERATION > len(INPUT_STRING.split()):
        print ("Iteration cannot be greater than the number of words in a string")
        print ("Terminating the benchmark")
        exit()

    print ("Original String: {}".format(INPUT_STRING))
    resultant_string = ""
    
    # Create a pulsar client by supplying ip address and port 
    client = pulsar.Client('pulsar://localhost:6650') 
    # Create a producer on the topic that consumer can subscribe to 
    producer = client.create_producer('DEtopic') 
  

    split_string = INPUT_STRING.split(" ")


    for i in range(0,ITERATION):

        #upper_case_string = conversion(split_string[i], function)
        
        what_is_this = producer.send((split_string[i]).encode('utf-8'))
        print("what is this: ", what_is_this)  

    client.close()

    #print ("Resultant String: {}".format(resultant_string))
