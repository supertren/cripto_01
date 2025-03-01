from blockchain import Blockchain, Block
from transaction import Transaction
from create_transaction import create_tx  # Your new file
import time

def main():
    grokcoin = Blockchain()
    
    # Use your create_transaction function
    tx1 = create_tx("Alice", "Bob", 50)
    block1 = Block(1, "", time.time(), [tx1.__dict__])
    grokcoin.add_block(block1)
    
    tx2 = create_tx("Bob", "Charlie", 20)
    block2 = Block(2, "", time.time(), [tx2.__dict__])
    grokcoin.add_block(block2)
    
    print("Blockchain contents:")
    for block in grokcoin.chain:
        print(f"Block {block.index}: {block.hash}")

if __name__ == "__main__":
    main()