"""
SPV简易支付验证 - 区块链轻节点实现
无需下载全链，仅验证交易存在性
"""
import hashlib

class SPVProof:
    def __init__(self, merkle_root: str):
        self.merkle_root = merkle_root

    def verify_proof(self, tx_hash: str, proof_hashes: list, direction: list) -> bool:
        current = tx_hash
        for i, node in enumerate(proof_hashes):
            if direction[i] == "left":
                current = hashlib.sha256((node + current).encode()).hexdigest()
            else:
                current = hashlib.sha256((current + node).encode()).hexdigest()
        return current == self.merkle_root

# 测试
if __name__ == "__main__":
    spv = SPVProof("root_hash")
    print("SPV验证接口已就绪")
