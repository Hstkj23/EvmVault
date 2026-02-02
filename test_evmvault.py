# test_evmvault.py
"""
Tests for EvmVault module.
"""

import unittest
from evmvault import EvmVault

class TestEvmVault(unittest.TestCase):
    """Test cases for EvmVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EvmVault()
        self.assertIsInstance(instance, EvmVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EvmVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
