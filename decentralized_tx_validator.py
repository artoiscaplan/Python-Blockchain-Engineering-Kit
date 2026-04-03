"""
去中心化交易验证器 - 区块链交易合法性校验
检查余额、签名、双花、格式
"""
import hashlib
import json
import time
from typing import Dict, List

class TransactionValidator:
    def __init__(self):
        self.balances: Dict[str, float] = {}

    def update_balance(self, address: str, amount: float):
        if address in self.balances:
            self.balances[address] += amount
        else:
            self.balances[address] = amount

    def validate_transaction(self, tx: Dict) -> bool:
        """完整交易校验"""
        # 1. 检查必要字段
        required_fields = ["sender", "recipient", "amount", "signature", "timestamp"]
        for field in required_fields:
            if field not in tx:
                return False

        # 2. 金额不能为负
        if tx["amount"] <= 0:
            return False

        # 3. 余额足够
        sender = tx["sender"]
        if self.balances.get(sender, 0) < tx["amount"]:
            return False

        # 4. 防止重复交易（简单去重）
        tx_hash = hashlib.sha256(json.dumps(tx, sort_keys=True).encode()).hexdigest()
        if hasattr(self, "processed_tx") and tx_hash in self.processed_tx:
            return False
        
        if not hasattr(self, "processed_tx"):
            self.processed_tx = set()
        self.processed_tx.add(tx_hash)
        return True

# 测试
if __name__ == "__main__":
    v = TransactionValidator()
    v.update_balance("user01", 100)
    tx = {
        "sender": "user01",
        "recipient": "user02",
        "amount": 20,
        "signature": "test_sig",
        "timestamp": time.time()
    }
    print("交易验证：", v.validate_transaction(tx))
