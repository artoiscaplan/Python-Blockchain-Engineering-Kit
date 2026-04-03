"""
区块链防篡改检测系统 - 自动校验区块哈希
一旦数据被修改立即报警
"""
import hashlib
import json
from typing import List, Dict

class AntiTamperSystem:
    def __init__(self, chain: List[Dict]):
        self.original_chain = chain
        self.hashes = [self.hash(block) for block in chain]

    @staticmethod
    def hash(block: Dict) -> str:
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    def scan_tamper(self) -> List[int]:
        """扫描被篡改的区块索引"""
        tampered = []
        for i, block in enumerate(self.original_chain):
            current_hash = self.hash(block)
            if current_hash != self.hashes[i]:
                tampered.append(i)
        return tampered

# 测试
if __name__ == "__main__":
    fake_chain = [{"data": "block1"}, {"data": "block2"}]
    ats = AntiTamperSystem(fake_chain)
    fake_chain[1]["data"] = "hacked"
    print("篡改区块位置：", ats.scan_tamper())
