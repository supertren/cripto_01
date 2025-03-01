class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

# Example usage
blockchain = Blockchain()

# Add a transaction
tx1 = Transaction("Alice", "Bob", 50)
blockchain.add_block(Block(1, "", time.time(), [tx1.__dict__]))

# Print the chain
for block in blockchain.chain:
    print(f"Block {block.index}: {block.hash}")
