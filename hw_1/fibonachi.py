def fibonachi(x: int):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibonachi(x-1) + fibonachi(x-2)


def main():
    res_1 = fibonachi(20)
    res_2 = fibonachi(22)
    assert res_1 == 6765 and res_2 == 17711

    with open('./artifacts/res.txt', 'w') as f:
        f.write(f'{res_1}, {res_2}')


if __name__ == '__main__':
    main()
