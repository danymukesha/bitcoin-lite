from bitcoin_lite import Transaction

def test_transaction():
    tx = Transaction("Alice", "Bob", 100.0)
    assert "Alice" in tx.details()
    assert "Bob" in tx.details()
    assert "100.0" in tx.details()

if __name__ == "__main__":
    test_transaction()
    print("Tests passed!")
