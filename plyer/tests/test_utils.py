'''
TestFacade
==========

Tested platforms:

* Android
* iOS
* Windows
* MacOS
* Linux
'''

import unittest
from mock import patch


class TestUtils(unittest.TestCase):
    '''
    TestCase for plyer.utils.
    '''

    def cutter(self, part, string):
        '''
        Cut off a part of a string if it contains a substring,
        otherwise raise an error.
        '''
        self.assertIn(part, string)
        return string[len(part):]

    def test_deprecated_function(self):
        '''
        Test printed out warning with @deprecated decorator
        on a function without any arguments.
        '''

        from plyer.utils import deprecated

        @deprecated
        def function():
            return 1

        with patch(target='sys.stderr.write') as stderr:
            self.assertEqual(function(), 1)

            args, _ = stderr.call_args_list[0]
            args = args[0]
            args = self.cutter('[WARNING] ', args)
            args = self.cutter('deprecated function function', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('Called from', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('by test_deprecated_function().\n', args)

            args, _ = stderr.call_args_list[1]
            self.assertEqual(args, ('\n',))

    def test_deprecated_function_arg(self):
        '''
        Test printed out warning with @deprecated decorator
        on a function without any arguments.
        '''

        from plyer.utils import deprecated

        @deprecated
        def function_with_arg(arg):
            return arg

        with patch(target='sys.stderr.write') as stderr:
            self.assertEqual(function_with_arg(1), 1)

            args, _ = stderr.call_args_list[0]
            args = args[0]
            args = self.cutter('[WARNING] ', args)
            args = self.cutter('deprecated function function_with_arg', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('Called from', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('by test_deprecated_function_arg().\n', args)

            args, _ = stderr.call_args_list[1]
            self.assertEqual(args, ('\n',))

    def test_deprecated_function_kwarg(self):
        '''
        Test printed out warning with @deprecated decorator
        on a function without any arguments.
        '''

        from plyer.utils import deprecated

        @deprecated
        def function_with_kwarg(kwarg):
            return kwarg

        with patch(target='sys.stderr.write') as stderr:
            self.assertEqual(function_with_kwarg(kwarg=1), 1)

            args, _ = stderr.call_args_list[0]
            args = args[0]
            args = self.cutter('[WARNING] ', args)
            args = self.cutter('deprecated function function_with_kwarg', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('Called from', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('by test_deprecated_function_kwarg().\n', args)

            args, _ = stderr.call_args_list[1]
            self.assertEqual(args, ('\n',))

    def test_deprecated_class_method(self):
        '''
        Test printed out warning with @deprecated decorator
        on a function without any arguments.
        '''

        from plyer.utils import deprecated

        class Class(object):  # pylint: disable=useless-object-inheritance
            '''
            Dummy class with deprecated method method.
            '''
            # pylint: disable=too-few-public-methods
            def __init__(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs

            @deprecated
            def method(self):
                '''
                Dummy deprecated method.
                '''
                return (self.args, self.kwargs)

        with patch(target='sys.stderr.write') as stderr:
            args = (1, 2, 3)
            kwargs = dict(x=1, y=2)

            cls = Class(*args, **kwargs)
            self.assertEqual(cls.method(), (args, kwargs))

            args, kwargs = stderr.call_args_list[0]
            args = args[0]
            args = self.cutter('[WARNING] ', args)
            args = self.cutter('deprecated function method', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('Called from', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('by test_deprecated_class_method().\n', args)

            args, kwargs = stderr.call_args_list[1]
            self.assertEqual(args, ('\n',))

    def test_deprecated_class_static(self):
        '''
        Test printed out warning with @deprecated decorator
        on a function without any arguments.
        '''

        from plyer.utils import deprecated

        class Class(object):  # pylint: disable=useless-object-inheritance
            '''
            Dummy class with deprecated static method.
            '''
            # pylint: disable=too-few-public-methods
            args = None
            kwargs = None

            def __init__(self, *args, **kwargs):
                Class.args = args
                Class.kwargs = kwargs

            @staticmethod
            @deprecated
            def static():
                '''
                Dummy deprecated static method.
                '''
                return (Class.args, Class.kwargs)

        with patch(target='sys.stderr.write') as stderr:
            args = (1, 2, 3)
            kwargs = dict(x=1, y=2)

            self.assertEqual(Class.static(), (None, None))

            args, kwargs = stderr.call_args_list[0]
            args = args[0]
            args = self.cutter('[WARNING] ', args)
            args = self.cutter('deprecated function static', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('Called from', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('by test_deprecated_class_static().\n', args)

            args, kwargs = stderr.call_args_list[1]
            self.assertEqual(args, ('\n',))

            cls = Class(*args, **kwargs)
            self.assertEqual(cls.static(), (args, kwargs))

            args, kwargs = stderr.call_args_list[2]
            self.assertEqual(args, (
                '''
                Dummy deprecated static method.
                ''',
            ))

            args, kwargs = stderr.call_args_list[3]
            self.assertEqual(args, ('\n',))

    def test_deprecated_class_clsmethod(self):
        '''
        Test printed out warning with @deprecated decorator
        on a function without any arguments.
        '''

        from plyer.utils import deprecated

        class Class(object):  # pylint: disable=useless-object-inheritance
            '''
            Dummy class with deprecated class method.
            '''
            # pylint: disable=too-few-public-methods
            args = None
            kwargs = None

            @classmethod
            @deprecated
            def clsmethod(cls):
                '''
                Dummy deprecated class method.
                '''
                return (cls.args, cls.kwargs)

        with patch(target='sys.stderr.write') as stderr:
            self.assertEqual(Class.clsmethod(), (None, None))

            args, _ = stderr.call_args_list[0]
            args = args[0]
            args = self.cutter('[WARNING] ', args)
            args = self.cutter('deprecated function clsmethod', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('Called from', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('by test_deprecated_class_clsmethod().\n', args)

            args, _ = stderr.call_args_list[1]
            self.assertEqual(args, ('\n',))

    def test_deprecated_class(self):
        '''
        Test printed out warning with @deprecated decorator
        on a function without any arguments.
        '''

        from plyer.utils import deprecated

        @deprecated  # pylint: disable=useless-object-inheritance
        class Class(object):
            '''
            Dummy deprecated class.
            '''
            # pylint: disable=too-few-public-methods
            def __init__(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs

        with patch(target='sys.stderr.write') as stderr:
            args = (1, 2, 3)
            kwargs = dict(x=1, y=2)

            cls = Class(*args, **kwargs)
            self.assertIsInstance(cls, Class)
            self.assertEqual(cls.args, args)
            self.assertEqual(cls.kwargs, kwargs)

            args, _ = stderr.call_args_list[0]
            args = args[0]
            args = self.cutter('[WARNING] ', args)
            args = self.cutter('Creating an instance', args)
            args = self.cutter('deprecated class Class in', args)
            args = self.cutter(__name__, args)
            args = self.cutter('Called from', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('by test_deprecated_class().\n', args)

            args, kwargs = stderr.call_args_list[1]
            self.assertEqual(args, ('\n',))

    def test_deprecated_class_inherited(self):
        '''
        Test printed out warning with @deprecated decorator
        on a function without any arguments.
        '''

        from plyer.utils import deprecated

        @deprecated  # pylint: disable=useless-object-inheritance
        class Class(object):
            '''
            Dummy deprecated class.
            '''
            # pylint: disable=too-few-public-methods
            def __init__(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs

        class Inherited(Class):
            '''
            Dummy class inheriting from a dummy deprecated class.
            '''
            # pylint: disable=too-few-public-methods
            def __init__(self, *args, **kwargs):
                super(Inherited, self).__init__(*args, **kwargs)
                self.args = args
                self.kwargs = kwargs

        with patch(target='sys.stderr.write') as stderr:
            args = (1, 2, 3)
            kwargs = dict(x=1, y=2)

            cls = Inherited(*args, **kwargs)
            self.assertIsInstance(cls, Class)
            self.assertIsInstance(cls, Inherited)
            self.assertEqual(cls.args, args)
            self.assertEqual(cls.kwargs, kwargs)

            args, _ = stderr.call_args_list[0]
            args = args[0]
            args = self.cutter('[WARNING] ', args)
            args = self.cutter('Creating an instance', args)
            args = self.cutter('deprecated class Class in', args)
            args = self.cutter(__name__, args)
            args = self.cutter('Called from', args)
            args = self.cutter('test_utils.py', args)
            args = self.cutter('by test_deprecated_class_inherited().\n', args)

            args, kwargs = stderr.call_args_list[1]
            self.assertEqual(args, ('\n',))


if __name__ == '__main__':
    unittest.main()
