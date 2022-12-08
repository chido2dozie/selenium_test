from unittest import TestLoader, TestSuite, TextTestRunner
from Tests.Scripts.test_calendar import TestCalendar
from Tests.Scripts.test_valid_login import TestValidLogin
from Tests.Scripts.test_invalid_login import TestInvalidLogin

if __name__ == '__main__':

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(TestValidLogin),
        loader.loadTestsFromTestCase(TestInvalidLogin),
        loader.loadTestsFromTestCase(TestCalendar)
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

