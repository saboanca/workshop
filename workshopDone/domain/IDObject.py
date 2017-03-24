'''
Created on 6 mar. 2017

@author: ABoanca
'''
class IDObject():
    '''
    Base class for all objects havin a unique ID within the application
    '''
    def __init__(self, objectID):
        '''
        Constructor method for building IDObject
        objectID - the unique ID of the object in the application
        '''
        self._objectID = objectID
    
    def getID(self):
        '''
        Returns the object ID
        '''
        return self._objectID