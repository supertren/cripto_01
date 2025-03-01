from flask import Flask, jsonify

def create_app(blockchain):
    app = Flask(__name__)
    app.config['BLOCKCHAIN'] = blockchain

    @app.route('/chain', methods=['GET'])
    def get_chain():
        blockchain = app.config.get('BLOCKCHAIN')
        if blockchain is None:
            return jsonify({"error": "Blockchain not initialized"}), 500
        chain_data = [block.__dict__ for block in blockchain.chain]
        return jsonify({"chain": chain_data})

    return app

def run_app(blockchain, port=5000):
    app = create_app(blockchain)
    app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == "__main__":
    from blockchain import Blockchain
    blockchain = Blockchain()
    run_app(blockchain, 5000)