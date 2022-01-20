from unittest import TestCase

import random

from .solution1 import group_names

class GroupTestCase(TestCase):

    def setUp(self) -> None:
        self.names = ['arun', 'vinod', 'karthik', 'sita', 'ramu', \
            'arvind', 'abinav',  'malu', 'prakash']
        self.result = {4: ['arun', 'sita', 'ramu', 'malu'],  5: ['vinod'], \
             6: ['arvind', 'abinav'], 7: ['karthik', 'prakash']}
    

    def test_1(self):
        grouped = group_names(self.names)
        self.assertEqual(grouped, self.result)