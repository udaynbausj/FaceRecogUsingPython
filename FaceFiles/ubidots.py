from ubidots import ApiClient
import math
import time

# Create an ApiClient object

api = ApiClient(token='yLSlucaRSbQeYSRcUHikpY2ApHFmaA')

# Get a Ubidots Variable

loginfo = api.get_variable('58cffcd67625427aeab98911')

# Here is where you usually put the code to capture the data, either through your GPIO pins or as a calculation. We'll simply put an artificial signal here:

while(1):

    # Write the value to your variable in Ubidots
    response = loginfo.save_value({"value": 'hi' })
    print (response)
    time.sleep(1)