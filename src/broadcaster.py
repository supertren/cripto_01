from flask import Flask, jsonify

app = Flask(__name__)
blockchain = None

def set_blockchain(external_blockchain):
    global blockchain
    blockchain = external_blockchain

@app.route('/chain', methods=['GET'])
def get_chain():
    if blockchain is None:
        return jsonify({"error": "Blockchain not initialized"}), 500
    chain_data = [block.__dict__ for block in blockchain.chain]
    return jsonify({"chain": chain_data})

def run_app(port=5000):
    app.run(port=port)

if __name__ == "__main__":
    # For standalone testing only
    from blockchain import Blockchain
    blockchain = Blockchain()
    app.run(port=5000)