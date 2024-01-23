from collections import UserDict

from random import randint

class Card(UserDict):
    number_per_letter = 15
    limit_line = 5
    loto_field = ['B', 'I', 'N', 'G', 'O']
    
    
    
    def __init__ (self):
        super().__init__()
        self.min_num = 1
        self.max_num 
