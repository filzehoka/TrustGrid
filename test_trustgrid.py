# test_trustgrid.py
"""
Tests for TrustGrid module.
"""

import unittest
from trustgrid import TrustGrid

class TestTrustGrid(unittest.TestCase):
    """Test cases for TrustGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrustGrid()
        self.assertIsInstance(instance, TrustGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrustGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
