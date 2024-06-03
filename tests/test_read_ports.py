import unittest
from unittest.mock import patch, MagicMock, call
import pandas as pd
import glob
import os

from cioTest.read_ports import main, read_file

class TestPortsScript(unittest.TestCase):

    @patch('glob.glob')
    def test_no_ports_files(self, mock_glob):
        # Setup the mock to return an empty list
        mock_glob.return_value = []

        # Verify that FileNotFoundError is raised
        with self.assertRaises(FileNotFoundError):
            main(None)

if __name__ == '__main__':
    unittest.main()