"""
NFT元数据生成器 - 链上NFT属性生成
支持图片哈希、属性、唯一ID
"""
import hashlib
import json
import time

class NFTMetadataGenerator:
    @staticmethod
    def generate(token_id: int, creator: str, name: str, image_url: str) -> dict:
        metadata = {
            "token_id": token_id,
            "name": name,
            "image": image_url,
            "creator": creator,
            "timestamp": time.time(),
            "attributes": [
                {"trait": "chain", "value": "Python-Blockchain"},
                {"trait": "standard", "value": "PY721"}
            ]
        }
        metadata["hash"] = hashlib.sha256(json.dumps(metadata, sort_keys=True).encode()).hexdigest()
        return metadata

# 测试
if __name__ == "__main__":
    meta = NFTMetadataGenerator.generate(1, "artist", "Python NFT", "ipfs://test")
    print(json.dumps(meta, indent=2))
