def demo(ipt):
    if type(ipt) == type(1):
        # 整数
        result = int_first(ipt)
    elif type(ipt) == type(0.1):
        # 浮点数
        result = float_first(ipt)
    else:
        result = "null"
    print(result)


def int_first(ipt):
    n = ipt//1
    s = str(n)
    ln = len(s)
    m = n//(10**(ln-1))
    return m


def float_first(ipt):
    n = ipt//1
    s = str(n).split('.')[0]
    n = int(s)
    ln = len(s)
    m = n//(10**(ln-1))
    return m

demo(100)




