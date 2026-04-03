"""
区块链P2P节点模拟器 - 去中心化网络同步
模拟节点广播、区块同步、交易转发
"""
import json
import hashlib
from typing import List, Dict

class P2PNode:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.blockchain: List[Dict] = []
        self.peers: List[str] = []

    def add_peer(self, peer_id: str):
        if peer_id not in self.peers:
            self.peers.append(peer_id)

    def broadcast_block(self, block: Dict):
        """广播新区块到所有节点"""
        print(f"[{self.node_id}] 广播区块：{block['index']}")
        return True

    def sync_chain(self, external_chain: List[Dict]):
        """链同步：最长链规则"""
        if len(external_chain) > len(self.blockchain):
            self.blockchain = external_chain.copy()
            return True
        return False

# 测试
if __name__ == "__main__":
    node1 = P2PNode("node_east")
    node2 = P2PNode("node_west")
    node1.add_peer(node2.node_id)
    node1.blockchain.append({"index": 1, "data": "test"})
    node2.sync_chain(node1.blockchain)
    print("node2同步后区块数：", len(node2.blockchain))
