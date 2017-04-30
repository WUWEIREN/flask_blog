#!/usr/bin/python
# _*_ coding:utf-8 _*_

import unittest


# class SimplisticTest(unittest.TestCase):
#
#     def test(self):
#         self.failUnless(True, 'failure message goes here')


# class OutcomesTest(unittest.TestCase):
#     def testPass(self):
#         return
#
#     def testFail(self):
#         self.failIf(True)
#
#     def testError(self):
#         raise RuntimeError('Test error')

#
# class TruthTest(unittest.TestCase):
#     def testFailUnless(self):
#         self.failUnless(True)
#
#     def testAssertTrue(self):
#         self.assertTrue(True)
#
#     def testFailIf(self):
#         self.failIf(False)
#
#     def testAssertFalse(self):
#         self.assertFalse(False)

#
# class EqualityTest(unittest.TestCase):
#     def testExpectEqual(self):
#         self.failUnlessEqual(1, 3-2)
#
#     def testExpectEqualFails(self):
#         self.failUnlessEqual(2, 3-2)
#
#     def testExpectNotEqual(self):
#         self.failIfEqual(2, 3-2)
#
#     def testExpectNotEqualFails(self):
#         self.failIfEqual(1, 3-2)


# class AlmostEqualTest(unittest.TestCase):
#     def testEqual(self):
#         self.failUnlessEqual(1.1, 3.3-2.2)
#
#     def testAlmostEqual(self):
#         self.failUnlessAlmostEqual(1.1, 3.3-2.2, places=1)
#
#     def testNotAlmostEqual(self):
#         self.failIfAlmostEqual(1.1, 3.3-2.0, places=1)

#
# def raises_error(*args, **kwargs):
#     raise  ValueError('Invalid value:' + str(args) + str(kwargs))
#
#
# class ExceptionTest(unittest.TestCase):
#
#     def testTrapLocally(self):
#         try:
#             raises_error('a', b='c')
#         except ValueError:
#             print 'aaaa'
#         else:
#             self.fail('Did not see ValueError')
#
#     def testFailUnlessRaise(self):
#         self.failUnlessRaises(ValueError, raises_error, 'a', b='c')

#
# class FixturesTest(unittest.TestCase):
#     def setUp(self):
#         print 'In setUP()'
#         self.fixtue = range(1, 10)
#
#     def tearDown(self):
#         print 'In tearDown()'
#         del self.fixtue
#
#     def test(self):
#         print 'In test()'
#         self.failUnlessEqual(self.fixtue, range(1, 10))
#
# if __name__ == '__main__':
#     unittest.main()


import traceback
import sys


def profuce_exception(recursion_level=2):
    sys.stdout.flush()
    if recursion_level:
        profuce_exception(recursion_level=1)
    else:
        raise RuntimeError()


def call_function(f, recurision_level=2):
    if recurision_level:
        return call_function(f, recurision_level=1)
    else:
        return f()

print 'print_exx() with no exception:'
traceback.print_exc(file=sys.stdout)
print
try:
    profuce_exception()
except Exception, err:
    print 'print_exc():'
    traceback.print_exc(file=sys.stdout)
    print
    print 'print _exc()'
    traceback.print_exc(limit=1, file=sys.stdout)