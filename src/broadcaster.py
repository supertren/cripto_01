from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.__dict__ for block in blockchain.chain]
    return jsonify({"chain": chain_data})

if __name__ == '__main__':
    app.run(port=5000)
