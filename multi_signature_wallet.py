"""
多签钱包 - 区块链安全钱包
N中M签名才能转账，提高资产安全性
"""
import hashlib
from typing import List

class MultiSigWallet:
    def __init__(self, owners: List[str], required: int):
        self.owners = owners
        self.required = required
        self.signatures = {}
        self.balance = 0

    def deposit(self, amount: int):
        self.balance += amount

    def add_signature(self, signer: str, tx_id: str):
        if signer not in self.owners:
            return False
        if tx_id not in self.signatures:
            self.signatures[tx_id] = []
        if signer not in self.signatures[tx_id]:
            self.signatures[tx_id].append(signer)
        return True

    def can_execute(self, tx_id: str) -> bool:
        return len(self.signatures.get(tx_id, [])) >= self.required

# 测试
if __name__ == "__main__":
    wallet = MultiSigWallet(["A", "B", "C"], 2)
    wallet.add_signature("A", "tx_1001")
    wallet.add_signature("B", "tx_1001")
    print("可执行交易：", wallet.can_execute("tx_1001"))
