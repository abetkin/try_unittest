import unittest

class MyTest(unittest.TestCase):

    def runTest(self):
        self.assertEqual(1, 2)

test = MyTest()



from testrunners import IPdbTestRunner

runner = IPdbTestRunner()

result = runner.run(test)


'''
if self.catchbreak:
    installHandler()
if self.testRunner is None:
    self.testRunner = runner.TextTestRunner
if isinstance(self.testRunner, type):
    try:
        testRunner = self.testRunner(verbosity=self.verbosity,
                                     failfast=self.failfast,
                                     buffer=self.buffer,
                                     warnings=self.warnings)
    except TypeError:
        # didn't accept the verbosity, buffer or failfast arguments
        testRunner = self.testRunner()
else:
    # it is assumed to be a TestRunner instance
    testRunner = self.testRunner
self.result = testRunner.run(self.test)
if self.exit:
    sys.exit(not self.result.wasSuccessful())

'''
