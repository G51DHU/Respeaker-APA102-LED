

from mycroft_bus_client import MessageBusClient, Message
import apa102_pi


"""
Get the current LED config for each state.

    class getLedConfig():

"""
class getLedConfig():
    def inactive(self):
        pass
    
    def woken(self):
        pass

    def prosessing(self):
        pass

    def processed(self):
        pass


"""
Change the current LED config.

    class changeLedConfig():

"""
class changeLedConfig():
    def brightness(self):
        pass

    def inactive(self):
        pass

    def wake(self):
        pass

    def processing(self):
        pass

    def processed(self):
        pass


"""
Wait for events within the message bus, 
and then act upon them.

    class onMessagebusEvent():

"""
class onMessagebusEvent():
    def inactive(self):
        pass

    def wake(self):
        pass

    def processing(self):
        pass

    def processed(self):
        pass


"""
When user says or inputs a command to control the LED,
or query the state. It handles it and initiates the appropriate
action.

    class userSays():

"""
class userSays():
    def stop(self):
        pass
    
    def start(self):
        pass

    def change_colour(self):
        pass
    
    def change_brightness(self):
        pass

    def what_is_brightness(self):
        pass