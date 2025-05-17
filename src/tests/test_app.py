import unittest
from src.app import main  # Ensure this matches your project structure

class TestApp(unittest.TestCase):

    def test_main(self):
        # Capture the output of the main function
        with self.assertLogs() as captured:
            main()
        self.assertIn("Hello, DevOps Engineer Dinesh!", captured.output[0])

if __name__ == '__main__':
    unittest.main()