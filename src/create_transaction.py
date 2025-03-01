tx2 = Transaction("Bob", "Charlie", 20)
blockchain.add_block(Block(2, "", time.time(), [tx2.__dict__]))
