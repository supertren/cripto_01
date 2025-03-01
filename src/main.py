from blockchain import Blockchain, Block
from create_transaction import create_tx
from broadcaster import run_app
import time
from threading import Thread

def main():
    grokcoin = Blockchain()
    
    # Start Flask with the blockchain instance
    flask_thread = Thread(target=run_app, args=(grokcoin, 5000))
    flask_thread.daemon = True
    flask_thread.start()
    
    # Wait for Flask to initialize
    time.sleep(2)
    
    # Add transactions
    tx1 = create_tx("Alice", "Bob", 50)
    block1 = Block(1, "", time.time(), [tx1.__dict__])
    grokcoin.add_block(block1)
    
    tx2 = create_tx("Bob", "Charlie", 20)
    block2 = Block(2, "", time.time(), [tx2.__dict__])
    grokcoin.add_block(block2)
    
    print("Blockchain contents (local):")
    for block in grokcoin.chain:
        print(f"Block {block.index}: {block.hash}")
    
    print("Visit http://localhost:5000/chain to see the blockchain via network")
    
    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()