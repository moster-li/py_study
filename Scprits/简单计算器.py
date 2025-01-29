
"""     13+2     """
import operator
def apply_operation(i, a, b):
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    if i in operations:
        return operations[i](a,b)
    else:
        raise ValueError(f"未知操作符：{i}")
while True:
    try:
        ls_input = input()
        for i in ls_input:
            if i in ["+","-","*","/"]:
                p = ls_input.index(i) #index函数可以返回该元素在列表中的位置
                #提取操作数
                a = float(ls_input[0:p])
                b = float(ls_input[p+1::])
                break
        if b == 0 and i == '/':
            print("被除数不能为0")
            continue
        print(apply_operation(i,a,b))
    except EOFError:
        print("程序停止")
        break