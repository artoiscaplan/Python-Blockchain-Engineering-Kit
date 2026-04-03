"""
类ERC20代币标准 - 区块链同质化代币
实现转账、授权、转账From、总额等核心接口
"""
class ERC20LikeToken:
    def __init__(self, name: str, symbol: str, total_supply: int):
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balances = {}
        self.allowance = {}
        self.balances["owner"] = total_supply

    def transfer(self, to: str, amount: int) -> bool:
        if self.balances.get("owner", 0) >= amount:
            self.balances["owner"] -= amount
            self.balances[to] = self.balances.get(to, 0) + amount
            return True
        return False

    def approve(self, spender: str, amount: int) -> bool:
        key = ("owner", spender)
        self.allowance[key] = amount
        return True

    def transfer_from(self, sender: str, recipient: str, amount: int) -> bool:
        key = (sender, recipient)
        if self.allowance.get(key, 0) >= amount and self.balances.get(sender, 0) >= amount:
            self.balances[sender] -= amount
            self.balances[recipient] = self.balances.get(recipient, 0) + amount
            self.allowance[key] -= amount
            return True
        return False

# 测试
if __name__ == "__main__":
    token = ERC20LikeToken("PythonChain", "PYC", 21000000)
    token.transfer("user01", 1000)
    print("user01余额：", token.balances.get("user01", 0))
