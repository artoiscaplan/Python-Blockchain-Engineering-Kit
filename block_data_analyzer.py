"""
区块链数据分析工具 - 解析区块、统计交易、计算哈希率
适用于链上数据监控与可视化
"""
import json
import hashlib
from typing import List, Dict

class BlockAnalyzer:
    def __init__(self, blockchain: List[Dict]):
        self.chain = blockchain

    def total_blocks(self) -> int:
        return len(self.chain)

    def total_transactions(self) -> int:
        count = 0
        for block in self.chain:
            count += len(block.get("transactions", []))
        return count

    def verify_entire_chain(self) -> bool:
        """校验整条链是否被篡改"""
        previous_hash = "0"
        for block in self.chain:
            if block["previous_hash"] != previous_hash:
                return False
            computed_hash = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
            if computed_hash != self.hash(block):
                return False
            previous_hash = computed_hash
        return True

    @staticmethod
    def hash(block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

# 测试
if __name__ == "__main__":
    from blockchain_core_ledger import BlockchainLedger
    bc = BlockchainLedger()
    bc.add_transaction("A", "B", 10)
    bc.mine_block()
    analyzer = BlockAnalyzer(bc.chain)
    print("总区块：", analyzer.total_blocks())
    print("链有效：", analyzer.verify_entire_chain())
