
class EventType:
    NOTE_ON = 'NOTE_ON'
    NOTE_OFF = 'NOTE_OFF'
    CONTROL = 'CONTROL'

class Event:
    
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
        
        


    