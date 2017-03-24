'''
Created on 7 mar. 2017

@author: ABoanca
'''
class ValidatorException(Exception):
    def __init__(self, messageList = ["Validation error!"]):
        self._messageList = messageList
        
    def getMessage(self):
        return self._message
    
    def __str__(self):
        s = ""
        for message in self.getMessage():
            s += str(message)
            s += '\n'
        return s
    