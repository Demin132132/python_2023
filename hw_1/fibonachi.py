def fibonachi(x: int):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibonachi(x-1) + fibonachi(x-2)
