'''
Created on 6 mar. 2017

@author: ABoanca
'''
import re
from domain.IDObject import IDObject
from domain.ValidatorException import ValidatorException

class Actor(IDObject):
    def __init__(self, objectID, firstName, lastName, birthday, nationality, residence, height, weight, email, phone):
        '''
        Constructor method for building Actor object
        Parameters:
            firstName - Actor's first name (string)
            lastName - Actor's last name (string)
            birthday - Actor's birthday (string)
            nationality - Actor's nationality (string)
            residence - Actor's city of residence (string)
            height - Actor's height in meters (string)
            weigth - Actor's weight in kg (integer number)
            email - Actor's email adderss (string)
            phone - Actor's phone number (string)
        '''
        IDObject.__init__(self, objectID)
        self._firstName = firstName
        self._lastName = lastName
        self._birthday  = birthday
        self._nationality = nationality
        self._residence = residence
        self._height = height
        self._weight = weight
        self._email = email
        self._phone = phone
    
    
    '''
    Getting attribute methods
    '''
    def getFirstName(self):
        return self._firstName
    
    def getLastName(self):
        return self._lastName
    
    def getBirthday(self):
        return self._birthday
    
    def getNationality(self):
        return self._nationality
    
    def getResidence(self):
        return self._residence
    
    def getHeight(self):
        return self._height
    
    def getWeight(self):
        return self._weight
    
    def getEmail(self):
        return self._email
    
    def getPhone(self):
        return self._phone
    
    
    '''
    Setting attribute methods
    '''
    def setFirstName(self, newFirstName):
        self._firstName = newFirstName
        
    def setLastName(self, newLastName):
        self._lastName = newLastName
        
    def setBirthday(self,newBirthday):
        self._birthday = newBirthday
    
    def setNationality(self, newNationality):
        self._nationality = newNationality
    
    def setResidence(self, newResidence):
        self._residence = newResidence
    
    def setHeight(self, newHeight):
        self._height = newHeight
    
    def setWeight(self, newWeight):
        self._weight = newWeight
    
    def setEmail(self, newEmail):
        self._email = newEmail
    
    def setPhone(self, newPhone):
        self._phone = newPhone
    
    def __str__(self):
        '''
        Prints the object in a given format
        Returns a string containing info about the object
        '''
        s = ""
        s += "ID: " + str(self.getID()) + '\n'
        s += "First Name: " + self._firstName + '\n';
        s += "Last Name: " + self._lastName + '\n';
        s += "Birthday: " + self._birthday + '\n';
        s += "Nationality: " + self._nationality + '\n';
        s += "Residence: " + self._residence + '\n';
        s += "Height: " + self._height + '\n';
        s += "Weight: " + str(self._weight) + '\n';
        s += "Email: " + self._email + '\n';
        s += "Phone: " + self._phone + '\n';
        return s;
    
class ActorValidator:
    def __init__(self):
        '''
        Validator class for actor, using regex
        '''
        self._error = ""
        
    def idValidator(self, id):
        regex = r"^[-+]?[0-9]+$"
        return re.match(regex, str(id)) != None
        
    def firstNameValidator(self, firstName):
        regex = r"[A-Za-z -]+"
        return re.match(regex, firstName) != None
    
    def lastNameValidator(self, lastName):
        regex = r"[A-Za-z -]+"
        return re.match(regex, lastName) != None
        
    def birthdayValidator(self, birthday):
        regex = r"^(((((0[1-9])|(1\d)|(2[0-8]))\/((0[1-9])|(1[0-2])))|((31\/((0[13578])|(1[02])))|((29|30)\/((0[1,3-9])|(1[0-2])))))\/((20[0-9][0-9])|(19[0-9][0-9])))|((29\/02\/(19|20)(([02468][048])|([13579][26]))))$"
        return re.match(regex, birthday) != None
    
    def nationalityValidator(self, nationality):
        regex = r"[A-Za-z -]+"
        return re.match(regex, nationality) != None
    
    def residenceValidator(self, residence):
        regex = r"^[a-zA-Z]+(?:[\\s-][a-zA-Z]+)*$"
        return re.match(regex, residence) != None 
    
    def heightValidator(self, height):
        regex = r"^[0-9]+\.[ ]?[0-9]{1,2}[\"]?$"
        return re.match(regex, height) != None
    
    def weightValidator(self, weight):
        regex = r"^[0-9]+$"
        return re.match(regex, str(weight)) != None
    
    def emailValidator(self, email):
        regex = r"\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+"
        return re.match(regex, email) != None
    
    def phoneValidator(self, phone):
        regex = r"^[0]+[0-9]+"
        return re.match(regex, phone) != None
    
    def validate(self, actor):
        _errors = []
        if self.idValidator(actor.getID()) == False:
            return False
        if self.firstNameValidator(actor.getFirstName()) == False:
            return False
        if self.lastNameValidator(actor.getLastName()) == False:
            return False
        if self.birthdayValidator(actor.getBirthday()) == False:
            return False
        if self.nationalityValidator(actor.getNationality()) == False:
            return False
        if self.residenceValidator(actor.getResidence()) == False:
            return False
        if self.heightValidator(actor.getHeight()) == False:
            return False
        if self.weightValidator(actor.getWeight()) == False:
            return False
        if self.emailValidator(actor.getEmail()) == False:
            return False
        if self.phoneValidator(actor.getPhone()) == False:
            return False
        return True