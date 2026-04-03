"""
极简智能合约 - 链上自动执行逻辑
实现代币转账、余额查询、权限控制
"""
class SimpleSmartContract:
    def __init__(self, owner: str):
        self.owner = owner
        self.balances = {owner: 1000000}  # 发行总量
        self.contract_address = "CONTRACT_PY_001"

    def transfer(self, sender: str, to: str, amount: int) -> bool:
        """链上转账"""
        if self.balances.get(sender, 0) >= amount and amount > 0:
            self.balances[sender] -= amount
            self.balances[to] = self.balances.get(to, 0) + amount
            return True
        return False

    def balance_of(self, address: str) -> int:
        """查询余额"""
        return self.balances.get(address, 0)

    def mint(self, to: str, amount: int, caller: str) -> bool:
        """仅所有者可增发"""
        if caller != self.owner:
            return False
        self.balances[to] = self.balances.get(to, 0) + amount
        return True

# 测试
if __name__ == "__main__":
    contract = SimpleSmartContract("admin")
    contract.transfer("admin", "user01", 500)
    print("user01余额：", contract.balance_of("user01"))
