import unittest
import unittest
import testing_main


class TestMain(unittest.TestCase):
    def setUp(self):
        print("about to run a test!")

    def test_do_stuff(self):
        test_param = 10
        result = testing_main.do_stuff(test_param)
        self.assertEqual(result, 15)  # check if equal

    def test_do_stuff2(self):
        test_param = "akldfj"
        result = testing_main.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

    def test_do_stuff3(self):
        test_param = None
        result = testing_main.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_do_stuff4(self):
        test_param = ""
        result = testing_main.do_stuff(test_param)
        self.assertEqual(result, "please enter number")


# run this only if this file is called directly
if __name__ == "__main__":
    unittest.main()
