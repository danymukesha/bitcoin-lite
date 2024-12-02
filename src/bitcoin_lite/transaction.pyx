cdef class Transaction:
    """
    A Cython-optimized transaction class for high-performance cryptocurrency operations.
    
    Attributes:
        sender (str): The transaction initiator
        receiver (str): The transaction recipient
        amount (float): The transaction amount
    
    Methods:
        details(): Returns a formatted transaction summary
    """
    cdef str sender
    cdef str receiver
    cdef float amount

    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def details(self):
        return f"Transaction from {self.sender} to {self.receiver} of amount {self.amount}"
