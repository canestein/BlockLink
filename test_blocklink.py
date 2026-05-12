# test_blocklink.py
"""
Tests for BlockLink module.
"""

import unittest
from blocklink import BlockLink

class TestBlockLink(unittest.TestCase):
    """Test cases for BlockLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockLink()
        self.assertIsInstance(instance, BlockLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
