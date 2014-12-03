import types

class testObject(object):   
        
    def A(self):
        self.value = 'A'
        print(self.value)
        
    @staticmethod
    def static():
        testObject.value = 'B'
        print(testObject.value)    
        
    def __setattr__(self, name, other):
        print('insetattr')
        print(other)
        print(name)
        object.__setattr__(self, name, other)    
        
class Wrappy(object):
    
    @staticmethod
    def __createWrapper__(component, method):
        if(isinstance(getattr(component, "__init__"), types.FunctionType)):
            def wrapper(self, *args, **kwargs):
                result = method(self, *args, **kwargs)
                'Inform interjector to wrap the new instance here'
                Wrappy.interceptInvocation(self)
                return result
            return wrapper
        else:
            def __init__(self):
                'Inform Interjector to wrap the new instance here'
                Wrappy.interceptInvocation(self)
                return
            return __init__;
    
    def interceptInvocation(self):
        print(self)
    
            

if __name__ == '__main__':
    wrapper = Wrappy.__createWrapper__(testObject, testObject.__init__)
    print(wrapper)
    setattr(testObject, "__init__", wrapper)     
    print(getattr(testObject, "__init__"))
    
    testA = testObject()
    testB = testObject()
    print('test1.')
    testA.A()
    testB.A()
    testB.static()
    testObject.static()
    
    pass