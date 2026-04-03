"""
时间锁智能合约 - 延迟提现/定时释放资产
典型应用：质押、空投、线性解锁
"""
import time

class TimeLockContract:
    def __init__(self, beneficiary: str, lock_seconds: int):
        self.beneficiary = beneficiary
        self.lock_seconds = lock_seconds
        self.release_time = time.time() + lock_seconds
        self.balance = 0

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, to: str) -> int:
        if to != self.beneficiary:
            return 0
        if time.time() < self.release_time:
            return 0
        amount = self.balance
        self.balance = 0
        return amount

# 测试
if __name__ == "__main__":
    lock = TimeLockContract("user01", 2)
    lock.deposit(1000)
    print("立即提现：", lock.withdraw("user01"))
    time.sleep(2)
    print("到期提现：", lock.withdraw("user01"))
