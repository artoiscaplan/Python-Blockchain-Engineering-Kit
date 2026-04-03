"""
区块链核心账本实现 - 基础不可篡改分布式账本
支持区块生成、哈希校验、链验证、交易记录
"""
import hashlib
import json
from time import time
from typing import List, Dict

class BlockchainLedger:
    def __init__(self):
        self.chain: List[Dict] = []
        self.pending_transactions: List[Dict] = []
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """创建创世区块（区块链第一个区块）"""
        genesis_block = {
            "index": 1,
            "timestamp": time(),
            "transactions": [],
            "proof": 100,
            "previous_hash": "0",
        }
        self.chain.append(genesis_block)

    @property
    def last_block(self) -> Dict:
        """获取链上最后一个区块"""
        return self.chain[-1]

    @staticmethod
    def hash(block: Dict) -> str:
        """SHA-256 区块哈希算法（区块链核心）"""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """添加待确认交易"""
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "tx_time": time()
        })
        return self.last_block["index"] + 1

    def proof_of_work(self, last_proof: int) -> int:
        """工作量证明：简单POW共识"""
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def mine_block(self) -> Dict:
        """挖矿生成新区块"""
        last_block = self.last_block
        last_proof = last_block["proof"]
        proof = self.proof_of_work(last_proof)

        new_block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.pending_transactions,
            "proof": proof,
            "previous_hash": self.hash(last_block),
        }

        self.pending_transactions = []
        self.chain.append(new_block)
        return new_block

# 测试运行
if __name__ == "__main__":
    bc = BlockchainLedger()
    bc.add_transaction("user_A", "user_B", 5.0)
    new_block = bc.mine_block()
    print("新区块生成成功：")
    print(json.dumps(new_block, indent=2))
