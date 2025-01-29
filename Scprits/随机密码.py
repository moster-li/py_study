import random

def password(n):
    pwd = ""
    ls = "qwertyuiopasdfghjklzxcvbnm,./';[]1234567890"
    for i in range(n):
        pwd += random.choice(ls)
    return pwd
if __name__ == "__main__":
    print("清输入密码长度：")
    number_input = int(input())
    print(f"生成的密码为{password(number_input)}")
