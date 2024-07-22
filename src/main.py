# 从标准输入读入一个扭结的 PD_CODE，假设它是合法的 PD_CODE
# 向标准输出输出消除 R1-move 以及 nugatory crossing 后的扭结的 PD_CODE

import sys

from de_r1 import de_r1
from de_k8 import de_k8

def de_r1_k8(pd_code0: list) -> list: # 消除 R1-move 以及 nugatory crossing
    pd_code1 = de_r1(pd_code0)
    pd_code2 = de_k8(pd_code1)
    return pd_code2

# 在这里，我们假定 pd_code 是合法的扭结 pd_code
def main():
    pd_code = eval(sys.stdin.read())
    print(de_r1_k8(pd_code))

if __name__ == "__main__":
    main()