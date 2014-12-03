from test.interceptor.InterceptorTests import *
from test.interceptor.OperandTests import *
from test.interceptor.GuardTests import *

def main():
    test = BasicTest()
    test.execute()
    test = BasicTestTwo()
    test.execute()
    test = TwoInstancesOfComponentTest()
    test.execute()
    test = TwoInstancesOfComponentTestTwo()
    test.execute()
    test = StaticMethodInterceptionTest()
    test.execute()
    test = StaticMethodInterceptionTestTwo()
    test.execute()
    test = TwoRUMTest()
    test.execute()
    test = FieldVariableOperandTest()
    test.execute()
    test = FunctionValueOperandTest()
    test.execute()
    test = InvokedServiceGuardTest()
    test.execute()    
    test = AndGuardTest()
    test.execute()    
    test = OrGuardTest()
    test.execute()
    test = GuardTest()
    test.execute()

    
    
if __name__ == "__main__":
    main()