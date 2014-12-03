

class BaseTest(object):

    def __init__(self, name, expected):
        self.expected = expected
        self.name = name
              
    def execute(self, result = None):
        if result == self.expected:
            print("test "+self.name+" succeeded")
        else:
            print("test "+self.name+" failed")
            print("expected: "+self.expected.__repr__())
            print("actual result: "+result.__repr__())
        
        