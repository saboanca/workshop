'''
Created on 6 mar. 2017

@author: ABoanca
'''
'''
Created on 6 mar. 2017

@author: ABoanca
'''
import re
from domain.IDObject import IDObject
from domain.ValidatorException import ValidatorException

class Movie(IDObject):
    def __init__(self, objectID, name, year, website):
        '''
        Constructor method for building Actor object
        Parameters:
            name - Movie's name (string)
            year - Movie's apparition year (integer)
            website - Movie website (string)
        '''
        IDObject.__init__(self, objectID)
        self._name = name
        self._year = year
        self._website  = website
    
    
    '''
    Getting attribute methods
    '''
    def getName(self):
        return self._name
    
    def getYear(self):
        return self._year
    
    def getWebsite(self):
        return self._website
    
    '''
    Setting attribute methods
    '''
    def setName(self, newName):
        self._firstName = newName
        
    def setYear(self, newYear):
        self._lastName = newYear
        
    def setWebsite(self,newWebsite):
        self._website = newWebsite
    
    
    def __str__(self):
        '''
        Prints the object in a given format
        Returns a string containing info about the object
        '''
        s = ""
        s += "ID: " + str(self.getID()) + '\n'
        s += "Name: " + self._name + '\n';
        s += "Year: " + str(self._year) + '\n';
        s += "website: " + self._website + '\n';
        return s;
    
class MovieValidator:
    def __init__(self):
        '''
        Validator class for movie, using regex
        '''
        self._error = ""
        
    def yearValidator(self, year):
        regex = r"^\d{4}$"
        return re.match(regex, str(year)) != None
    
    def idValidator(self, id):
        regex = r"^[-+]?[0-9]+$"
        return re.match(regex, str(id)) != None

        
    def nameValidator(self, name):
        regex = r"[A-Za-z0-9 !,\?]+"
        return re.match(regex, str(name)) != None
    
    def websiteValidator(self, website):
        regex = r"^www.[a-zA-Z0-9_-]+\.[a-z]+$"
        return re.match(regex, website) != None
    
    def validate(self, movie):
        _errors = []
        if self.idValidator(movie.getID()) == False:
            return False
        if self.nameValidator(movie.getName()) == False:
            return False
        if self.yearValidator(movie.getYear()) == False:
            return False
        if self.websiteValidator(movie.getWebsite()) == False:
            return False
        return True
                 