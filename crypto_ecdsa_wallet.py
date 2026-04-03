"""
区块链ECDSA加密钱包 - 生成公私钥、签名、验签
适用于比特币/以太坊类钱包核心逻辑
"""
import hashlib
import ecdsa
import binascii
from typing import Tuple

class ECDSAWallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.wallet_address = None

    def generate_key_pair(self) -> Tuple[str, str]:
        """生成ECDSA非对称密钥对"""
        sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        vk = sk.get_verifying_key()

        self.private_key = sk.to_string().hex()
        self.public_key = vk.to_string().hex()
        self.wallet_address = self._generate_address()
        return self.private_key, self.public_key

    def _generate_address(self) -> str:
        """通过公钥生成钱包地址"""
        pub_key_bytes = bytes.fromhex(self.public_key)
        sha256 = hashlib.sha256(pub_key_bytes).digest()
        ripemd160 = hashlib.new('ripemd160', sha256).digest()
        return binascii.hexlify(ripemd160).decode()

    def sign_message(self, message: str) -> str:
        """使用私钥签名消息"""
        sk = ecdsa.SigningKey.from_string(bytes.fromhex(self.private_key), curve=ecdsa.SECP256k1)
        message_hash = hashlib.sha256(message.encode()).digest()
        signature = sk.sign(message_hash)
        return binascii.hexlify(signature).decode()

    def verify_signature(self, message: str, signature: str) -> bool:
        """验证签名合法性"""
        vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(self.public_key), curve=ecdsa.SECP256k1)
        message_hash = hashlib.sha256(message.encode()).digest()
        try:
            return vk.verify(bytes.fromhex(signature), message_hash)
        except:
            return False

# 测试
if __name__ == "__main__":
    wallet = ECDSAWallet()
    priv, pub = wallet.generate_key_pair()
    print(f"钱包地址：{wallet.wallet_address}")
    msg = "blockchain transaction 100"
    sig = wallet.sign_message(msg)
    print(f"验签结果：{wallet.verify_signature(msg, sig)}")
