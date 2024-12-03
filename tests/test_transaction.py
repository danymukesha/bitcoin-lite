from bitcoin_lite import Transaction

def test():
    tx = Transaction("Alice", "Bob", 100.0)
    print(tx.details())

if __name__ == "__main__":
    test()
