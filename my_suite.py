import unittest
from test.test_food import TestItem
from test.test_level import TestLevel
from test.test_timhortons import TestTimhortons
from test.test_character import TestCharacter
from test.test_alien import TestAlien
from test.test_player import TestPlayer
from test.test_sparkLance import TestSparkLance
def my_suite():
    
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    
    suite.addTest(unittest.makeSuite(TestItem))
    suite.addTest(unittest.makeSuite(TestLevel))
    suite.addTest(unittest.makeSuite(TestTimhortons))
    suite.addTest(unittest.makeSuite(TestCharacter))
    suite.addTest(unittest.makeSuite(TestAlien))
    suite.addTest(unittest.makeSuite(TestPlayer))
    suite.addTest(unittest.makeSuite(TestSparkLance))
    
    
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
