from test.interjector.InterjectorTests import *

def main():
    test = BasicInterjectionTest()
    test.execute()
    test = TwoInstancesInterjectionTest()
    test.execute()
    test = TwoInstancesInterjectionTestTwo()
    test.execute()
    test = InterjectionInterceptorTest()
    test.execute()
    test = InterjectionMethodReplacedTest()
    test.execute()
    test = InterjectionStaticCallerTest()
    test.execute()
    test = InterjectionStaticCalledTest()
    test.execute()
    
    
if __name__ == "__main__":
    main()