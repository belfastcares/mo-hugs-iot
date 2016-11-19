import time
import requests
import pyupm_grove as grove

# Create the button object using GPIO pin 0
button = grove.GroveButton(4)
light = grove.GroveLed(3)

# Read the input and print, waiting one second between readings
while 1:
    print button.name(), ' value is ', button.value()
    
    if button.value() == 1:
        light.on()
        # make request to api
        r = requests.put('http://demo6741759.mockable.io/test', data = {'key':'value'})
        print r.content
        time.sleep(1)
        light.off()
    time.sleep(0.5)

del light
# Delete the button object
del button

