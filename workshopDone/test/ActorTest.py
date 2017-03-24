'''
Created on 23 mar. 2017

@author: ABoanca
'''
import unittest
from repository.ActorRepo import *
from domain.Actor import *
from controller.ActorController import *

class RepositoryTest(unittest.TestCase):
    '''
    Unit test case for repository and controller for class Actor
    '''
    def setUp(self):
        self._repo = ActorRepository()
        self._controller = ActorController(self._repo)
        
    def testActor(self):
        '''
        tests add, remove, getAll, len for actor in repository
        '''
        self.assertEqual(len(self._repo), 0)
        actor = Actor(1, "ex", "ex", "11/11/2011", "america", "america", "1.70", 34, "csd@yahoo.com", "0987654321")
        self._repo.add(actor)
        self.assertEqual(len(self._repo), 1)
        self.assertEqual(len(self._repo.getAll()), 1)
        self._repo.removeID(1)
        self.assertEqual(len(self._repo.getAll()), 0)
        '''
        tests add, remove, getAll, len, checkID for actor in controller
        '''
        self.assertEqual(len(self._controller.getAll()), 0)
        actor = Actor(1, "ex", "ex", "11/11/2011", "america", "america", "1.70", 34, "csd@yahoo.com", "0987654321")
        self._controller.add(actor)
        self.assertEqual(len(self._controller.getAll()), 1)
        '''
        if id doesn't exist, returns 1
        '''
        self.assertEqual(self._controller.checkID(0), 1)
        '''
        if id exists, returns 0
        '''
        self.assertEqual(self._controller.checkID(1), 0)
        self._controller.removeID(1)
        self.assertEqual(len(self._controller.getAll()), 0)
        self._controller.addActor(1, "ex", "ex", "11/11/2011", "america", "america", "1.70", 34, "csd@yahoo.com", "0987654321")
        self.assertEqual(self._controller.addActor(2, "ex", "ex", "11/11/2011", "america", "america", "1.70", 34, "csd@yahoo.com", "0987654321"), 1)
        self.assertEqual(len(self._controller.getAll()), 2)
        self._controller.addActor(-1, "ex", "ex", "11/11/2011", "america", "america", "1.70", 34, "csd@yahoo.com", "0987654321")
        self.assertEqual(self._controller.addActor(-1, "ex", "ex", "11/11/2011", "america", "america", "1.70", 34, "csd@yahoo.com", "0987654321"), -1)
        self.assertEqual(len(self._controller.getAll()), 2)
        
        '''
        test domain
        '''
        actor0 = Actor("a", "Andrew!", "Scott!", "10/22/1980", "!Irish", "Dub!lin", "175", -70, "a.scottgmail.com", "123456789")
        ok = ActorValidator()
        self.assertEqual(actor0.getID(),"a")
        self.assertEqual(ok.idValidator(actor0.getID()), False)
        self.assertEqual(actor0.getFirstName(), "Andrew!")
        self.assertEqual(ok.firstNameValidator(actor0.getFirstName()),True)
        self.assertEqual(actor0.getLastName(), "Scott!")
        self.assertEqual(ok.lastNameValidator(actor0.getLastName()), True)
        self.assertEqual(actor0.getBirthday(), "10/22/1980")
        self.assertEqual(ok.birthdayValidator(actor0.getBirthday()), False)
        self.assertEqual(actor0.getNationality(), "!Irish")
        self.assertEqual(ok.nationalityValidator(actor0.getNationality()), False)
        self.assertEqual(actor0.getResidence(), "Dub!lin")
        self.assertEqual(ok.residenceValidator(actor0.getResidence()), False)
        self.assertEqual(actor0.getHeight(), "175")
        self.assertEqual(ok.heightValidator(actor0.getHeight()), False)
        self.assertEqual(actor0.getWeight(), -70)
        self.assertEqual(ok.weightValidator(actor0.getWeight()), False)
        self.assertEqual(actor0.getEmail(), "a.scottgmail.com")
        self.assertEqual(ok.emailValidator(actor0.getEmail()), False)
        self.assertEqual(actor0.getPhone(), "123456789")
        self.assertEqual(ok.phoneValidator(actor0.getPhone()), False)
        self.assertEqual(ok.validate(actor0), False)
        
        actor1 = Actor(1, "Andrew", "Scott", "10/03/1980", "Irish", "Dublin", "1.75", 70, "a.scott@gmail.com", "0123456789")
        ok = ActorValidator()
        self.assertEqual(actor1.getID(), 1)
        self.assertEqual(ok.idValidator(actor1.getID()), True)
        self.assertEqual(actor1.getFirstName(), "Andrew")
        self.assertEqual(ok.firstNameValidator(actor1.getFirstName()), True)
        self.assertEqual(actor1.getLastName(), "Scott")
        self.assertEqual(ok.lastNameValidator(actor1.getLastName()), True)
        self.assertEqual(actor1.getBirthday(), "10/03/1980")
        self.assertEqual(ok.birthdayValidator(actor1.getBirthday()), True)
        self.assertEqual(actor1.getNationality(), "Irish")
        self.assertEqual(ok.nationalityValidator(actor1.getNationality()), True)
        self.assertEqual(actor1.getResidence(), "Dublin")
        self.assertEqual(ok.residenceValidator(actor1.getResidence()), True)
        self.assertEqual(actor1.getHeight(), "1.75")
        self.assertEqual(ok.heightValidator(actor1.getHeight()), True)
        self.assertEqual(actor1.getWeight(), 70)
        self.assertEqual(ok.weightValidator(actor1.getWeight()), True)
        self.assertEqual(actor1.getEmail(), "a.scott@gmail.com")
        self.assertEqual(ok.emailValidator(actor1.getEmail()), True)
        self.assertEqual(actor1.getPhone(), "0123456789")
        self.assertEqual(ok.phoneValidator(actor1.getPhone()), True)
        self.assertEqual(ok.validate(actor1), True)
        