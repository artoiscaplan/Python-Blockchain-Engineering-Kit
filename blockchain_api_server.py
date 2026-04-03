"""
区块链REST API服务 - 可直接对接前端/钱包
提供查询、交易、挖矿、状态接口
"""
from flask import Flask, jsonify, request
from blockchain_core_ledger import BlockchainLedger

app = Flask(__name__)
blockchain = BlockchainLedger()

@app.route('/api/chain', methods=['GET'])
def get_chain():
    return jsonify({
        "length": len(blockchain.chain),
        "chain": blockchain.chain
    })

@app.route('/api/transaction/new', methods=['POST'])
def new_transaction():
    data = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in data for k in required):
        return jsonify({"error": "参数缺失"}), 400
    index = blockchain.add_transaction(data['sender'], data['recipient'], data['amount'])
    return jsonify({"message": f"交易将加入区块 {index}"}), 201

@app.route('/api/mine', methods=['GET'])
def mine():
    block = blockchain.mine_block()
    return jsonify(block), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
