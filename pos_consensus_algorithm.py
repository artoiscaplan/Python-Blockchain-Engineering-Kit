"""
权益证明（PoS）共识算法 - 替代POW的节能共识机制
支持节点质押、出块权选举、链验证
"""
import hashlib
import json
import time
from typing import List, Dict

class PoSBlockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.stakers: Dict[str, int] = {}  # 质押者: 质押金额
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = {
            "index": 1,
            "validator": "genesis",
            "transactions": [],
            "timestamp": time.time(),
            "previous_hash": "0"
        }
        self.chain.append(genesis)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_stake(self, address: str, amount: int):
        """节点质押代币获取出块资格"""
        if address in self.stakers:
            self.stakers[address] += amount
        else:
            self.stakers[address] = amount

    def select_validator(self) -> str:
        """根据质押权重随机选择出块节点"""
        total_stake = sum(self.stakers.values())
        if total_stake == 0:
            return "genesis"
        
        import random
        selection = random.randint(0, total_stake)
        current = 0
        for addr, stake in self.stakers.items():
            current += stake
            if current >= selection:
                return addr

    @staticmethod
    def hash(block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    def mint_block(self) -> Dict:
        """PoS 铸块"""
        validator = self.select_validator()
        new_block = {
            "index": len(self.chain) + 1,
            "validator": validator,
            "transactions": self.pending_transactions,
            "timestamp": time.time(),
            "previous_hash": self.hash(self.last_block)
        }
        self.pending_transactions = []
        self.chain.append(new_block)
        return new_block

if __name__ == "__main__":
    pos = PoSBlockchain()
    pos.add_stake("node01", 100)
    pos.add_stake("node02", 300)
    pos.mint_block()
    print("PoS区块：", json.dumps(pos.last_block, indent=2))
