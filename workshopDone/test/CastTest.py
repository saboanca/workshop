'''
Created on 24 mar. 2017

@author: ABoanca
'''
import unittest
from repository.CastRepo import CastRepository
from controller.CastController import CastController
from repository.ActorRepo import *

class RepositoryTest(unittest.TestCase):
    '''
    Unit test case for repository and controller
    '''
    def setUp(self):
        self._repo = CastRepository()
        self._actorRepo = ActorRepository()
        self._controller = CastController(self._repo, self._actorRepo)
        
    def testCast(self):
        '''
        tests addMovie, addActor, removeMovie, removeActor, getAll, len for current repository
        '''
        self.assertEqual(len(self._repo), 0)
        self._repo.addMovie(1)
        self.assertEqual(len(self._repo), 2)
        self.assertEqual(self._repo.lengthList(1), 0)
        self._repo.addActor(1, 2)
        self.assertEqual(self._repo.checkID(1,2), 1)
        self.assertEqual(self._repo.lengthList(1), 1)
        self.assertEqual(len(self._repo), 2)
        self._repo.removeActor(2)
        self.assertEqual(self._repo.checkID(1,2), 0)
        self.assertEqual(self._repo.lengthList(1), 0)
        self.assertEqual(len(self._repo), 2)
        self._repo.removeMovie(1)
        self.assertEqual(len(self._repo), 0)
        self.assertEqual(len(self._repo.getAll()), 0)
        self._repo.addMovie(1)
        self._repo.addActor(1,2)
        self._repo.addActor(1,3)
        self.assertEqual(self._repo.lengthList(1), 2)
        self._repo.removeActorFromMovie(1,2)
        self.assertEqual(self._repo.lengthList(1), 1)
        actor = Actor(2, "ex", "ex", "11/11/2011", "america", "america", "1.70", 34, "csd@yahoo.com", "0987654321")
        actor1 = Actor(11, "ex", "ex", "11/11/2011", "america", "america", "1.70", 34, "csd@yahoo.com", "0987654321")
        self._actorRepo.add(actor)
        '''
        tests addMovie, addActor, removeMovie, removeActor, getAll, checkID, len for current controller
        '''
        self.assertEqual(len(self._controller.getAll()), 2)
        self._controller.addMovie(1)
        self.assertEqual(len(self._controller.getAll()), 4)
        self.assertEqual(self._controller.lengthList(1), 1)
        self.assertEqual(self._controller.checkAddActor(1,18), -1)
        self._controller.checkAddActor(1,2)
        self.assertEqual(self._controller.lengthList(1), 2)
        self.assertEqual(self._controller.checkAddToCast(1,2), -1)
        self.assertEqual(self._controller.checkAddToCast(1,11), None)
        self.assertEqual(self._controller.checkID(1,2), 1)
        self._controller.removeActorFromMovie(1,2)
        self.assertEqual(self._controller.lengthList(1), 1)
        self._controller.checkAddActor(1,2)
        self.assertEqual(self._controller.lengthList(1), 2)
        self.assertEqual(self._controller.checkAddToCast(1,2), -1)
        self.assertEqual(self._controller.checkAddToCast(1,11), None)
        self.assertEqual(self._controller.checkID(1,2), 1)
        self._controller.removeActor(2)
        self.assertEqual(self._controller.checkID(1,2), 0)
        self.assertEqual(self._controller.lengthList(1), 1)

        