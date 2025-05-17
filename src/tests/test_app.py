import unittest
from src.app import main  # Ensure this matches your project structure

class TestApp(unittest.TestCase):

    def test_main(self):
        with self.assertLogs(level='INFO') as captured:
            main()
        self.assertIn("Hello, DevOps Engineer Dinesh!", captured.output[0])

if __name__ == '__main__':
    unittest.main()