import pulsar 
from conversion import conversion
from conversion import function

# Create a pulsar client by supplying ip address and port 
def pulsarConsumer():
  # Create a pulsar client by supplying ip address and port
  client = pulsar.Client('pulsar://localhost:6650') 
  # Subscribe to a topic and subscription  
  return client.subscribe('DEtopic', subscription_name='DE-sub') 
   
consumer = pulsarConsumer() 
merged_string = ""

while (True):
    try: 
        # Display message received from producer
        msg = consumer.receive()
        print("Received message : '%s'" % msg.data()) 

        upper_case_string = conversion(msg.data(), function)
        print("upper case string: ", upper_case_string)
        merged_string += upper_case_string
        # Acknowledge for receiving the message  
        consumer.acknowledge(msg) 
    except: 
        consumer.negative_acknowledge(msg) 

print(merged_string)
# Destroy pulsar client 
client.close() 
