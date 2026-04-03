"""
多节点链一致性校验 - 跨节点数据一致性检查
用于联盟链/私有链节点状态同步
"""
import hashlib
import json
from typing import List

class ChainConsistencyCheck:
    def __init__(self, chains: List[List[dict]]):
        self.chains = chains

    @staticmethod
    def chain_hash(chain: List[dict]) -> str:
        return hashlib.sha256(json.dumps(chain, sort_keys=True).encode()).hexdigest()

    def all_consistent(self) -> bool:
        if not self.chains:
            return True
        first_hash = self.chain_hash(self.chains[0])
        for chain in self.chains[1:]:
            if self.chain_hash(chain) != first_hash:
                return False
        return True

# 测试
if __name__ == "__main__":
    c1 = [{"b": 1}, {"b": 2}]
    c2 = [{"b": 1}, {"b": 2}]
    c3 = [{"b": 1}, {"b": 3}]
    check = ChainConsistencyCheck([c1, c2, c3])
    print("节点一致：", check.all_consistent())
