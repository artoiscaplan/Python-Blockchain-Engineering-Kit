"""
默克尔树（Merkle Tree）- 区块链交易高效校验
用于区块交易完整性验证、轻节点证明
"""
import hashlib
from typing import List

class MerkleTree:
    def __init__(self, transactions: List[str]):
        self.transactions = [self.hash_data(tx) for tx in transactions]
        self.root = self.build_merkle_root()

    @staticmethod
    def hash_data(data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def build_merkle_root(self) -> str:
        """构建默克尔树根"""
        nodes = self.transactions.copy()
        while len(nodes) > 1:
            temp = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i+1] if i+1 < len(nodes) else left
                combined = left + right
                temp.append(self.hash_data(combined))
            nodes = temp
        return nodes[0] if nodes else ""

    def get_root(self) -> str:
        return self.root

# 测试
if __name__ == "__main__":
    tx_list = [
        "tx1: A->B 10",
        "tx2: B->C 5",
        "tx3: C->D 3",
        "tx4: D->A 1"
    ]
    mt = MerkleTree(tx_list)
    print(f"默克尔根：{mt.get_root()}")
