from transaction import Transaction

def create_tx(sender, receiver, amount):
    return Transaction(sender, receiver, amount)

if __name__ == "__main__":
    tx = create_tx("Alice", "Bob", 50)
    print(tx.__dict__)