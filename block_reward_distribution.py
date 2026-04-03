"""
区块奖励分发算法 - 矿工/节点激励机制
支持基础奖励、手续费、质押分红
"""
class BlockReward:
    def __init__(self, base_reward: float = 10.0):
        self.base_reward = base_reward

    def calculate_reward(self, fee_total: float, stake_ratio: float = 1.0) -> float:
        """计算总出块奖励"""
        reward = self.base_reward + fee_total * 0.1
        return reward * stake_ratio

    def distribute(self, validator: str, reward: float, distribution: dict):
        distribution[validator] = distribution.get(validator, 0) + reward
        return distribution

# 测试
if __name__ == "__main__":
    br = BlockReward()
    total = br.calculate_reward(fee_total=5.0)
    print("区块奖励：", total)
