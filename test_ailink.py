# test_ailink.py
"""
Tests for AILink module.
"""

import unittest
from ailink import AILink

class TestAILink(unittest.TestCase):
    """Test cases for AILink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AILink()
        self.assertIsInstance(instance, AILink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AILink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
