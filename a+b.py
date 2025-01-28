while True:
    try:
        input_ls = list(map(int,input().split()))
        print(sum(input_ls[1:]),"\n")
    except EOFError:
        break