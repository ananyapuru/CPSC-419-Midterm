#!/usr/bin/env python

#-----------------------------------------------------------------------
# book.py
# Author: Bob Dondero, modified by Ananya Purushottam
#-----------------------------------------------------------------------

class Object:

    def __init__(self, id, label, date, agent):
        self._id = id
        self._label = label
        self._date = date
        self._agent = agent

    def get_id(self):
        return self._id
    
    def get_label(self):
        return self._label
    
    def get_date(self):
        return self._date
    
    def get_agent(self):
        return self._agent


    def to_tuple(self):
        return (self._id, self._label, self._date, self._agent)

    def to_dict(self):
            return {'id': self._id, 'label': self._label,
                'date': self._date, 'agent': self._agent}

#-----------------------------------------------------------------------

def _test():
    obj = Object(1912, 'FakePainting', '18th century BC fake date', "Ananya is the agent")
    print()
    print(obj.to_tuple())
    print()
    print(obj.to_dict())

if __name__ == '__main__':
    _test()
