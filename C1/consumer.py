import pulsar 

# Create a pulsar client by supplying ip address and port 
def pulsarConsumer():
  # Create a pulsar client by supplying ip address and port
  client = pulsar.Client('pulsar://localhost:6650') 
  # Subscribe to a topic and subscription  
  return client.subscribe('DEtopic', subscription_name='DE-sub') 
   

def conversion(substring, operation):
    """A conversion function which takes a string as an input and outputs a converted string

    Args:
        substring (String)
        operation (function): This is an operation on the given input

    Returns:
        [String]: Converted String
    """
    # returns the conversion applied to input
    return function(substring)

def function(string):
    """ A function that performs some operation on a string. You can change the operation accordingly

    Args:
        string (String): input string on which some operation is applied

    Returns:
        [String]: string in upper case
    """
    return string.upper()


consumer = pulsarConsumer() 
merged_string = ""

try:
    while (True):
        msg = consumer.receive()
        msgDecoded = msg.data().decode()

        # Display message received from producer
        print("Received message : '%s'" % msgDecoded) 

        upper_case_string = conversion(msgDecoded, function)
        print("upper case string: ", upper_case_string)

        merged_string += upper_case_string + " "
        print("merged_string: ", merged_string)

        # Acknowledge for receiving the message
        consumer.acknowledge(msg) 
except Exception as e:
    print("ERROR : "+str(e))
    consumer.negative_acknowledge(msg) 

print(merged_string)
# Destroy pulsar client 
consumer.close() 
