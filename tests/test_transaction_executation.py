import pytest
from bitcoin_lite import Transaction
import os

def test_transaction_execution():
    # initialize with test database
    tx1 = Transaction("Alice", "Bob", 50.0)
    tx2 = Transaction("Bob", "Charlie", 25.0)
    
    # execute transactions
    tx1_id = tx1.execute()
    assert tx1_id is not None
    
    # check balances
    assert tx1.get_sender_balance() == -50.0
    assert tx1.get_receiver_balance() == 50.0
    
    # execute second transaction
    tx2_id = tx2.execute()
    assert tx2_id is not None
    
    # check the final balances
    assert tx1.get_sender_balance() == -50.0  # Alice
    assert tx2.get_sender_balance() == 25.0   # Bob
    assert tx2.get_receiver_balance() == 25.0  # Charlie

if __name__ == "__main__":
    pytest.main([__file__])
