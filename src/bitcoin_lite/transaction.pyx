cdef class Transaction:
    cdef str sender
    cdef str receiver
    cdef float amount

    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def details(self):
        return f"Transaction from {self.sender} to {self.receiver} of amount {self.amount}"
