
def count_world(ls_input):
    frequency = {}
    for i in ls_input:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency
while True:
    try:

        ls_input = input().split()
        print(count_world(ls_input))

    except EOFError:
        print("程序结束！")
        break