def read_data(filename: str):
    x = []
    y = []
    data = []
    with open(filename, 'r') as file:
        x = [int(i) for i in file.readline().split()][1:]
        for line in file:
            line = [int(i) for i in line.split()]
            y.append(line[0])
            data.append(line[1:])
    return x, y, data


def input_data():
    x, y = map(float, input("Input x, y with space\n").split())
    nx, ny = map(int, input("Input nx, ny with space. Valid is [1:4]\n").split())
    if nx < 1 or nx > 4 or ny < 1 or ny > 4:
        raise ("Error input data")
    return x, y, nx, ny


def get_data_by_n(x_arr, y_arr, x: int, x_power: int):
    if x_arr[len(x_arr) - 1] < x or x_arr[0] > x:
        raise ("x out of table")
    left = right = -1
    for i in range(1, len(x_arr)):
        if x_arr[i - 1] <= x and x_arr[i] >= x:
            left, right = i - 1, i
    res_x = [x_arr[left], x_arr[right]]
    res_y = [y[left:right + 1] for y in y_arr]
    cnt = 2
    left -= 1
    right += 1
    while cnt < x_power + 1:
        if left >= 0:
            res_x.append(x_arr[left])
            res_y = [[y_arr[i][left]] + res_y[i] for i in range(len(res_y))]
            left -= 1
            cnt += 1
        if right < len(x_arr) and cnt < x_power + 1:
            res_x.append(x_arr[right])
            res_y = [res_y[i] + [y_arr[i][right]] for i in range(len(res_y))]
            right += 1
            cnt += 1
    if left == -1:
        left += 1
    return sorted(res_x), res_y


def get_data_by_ny(y_arr, newton, y, y_power):
    if y_arr[len(y_arr) - 1] < y or y_arr[0] > y:
        raise ("y out of table")
    left, right = -1, -1
    for i in range(1, len(y_arr)):
        if y_arr[i - 1] <= y and y_arr[i] >= y:
            left, right = i - 1, i
    res_y = [y_arr[left], y_arr[right]]
    res_newton = [newton[left], newton[right]]
    cnt = 2
    left -= 1
    right += 1
    while cnt < y_power + 1:
        if left >= 0:
            res_y.append(y_arr[left])
            res_newton.append(newton[left])
            left -= 1
            cnt += 1
        if right < len(res_y) and cnt < y_power + 1:
            res_y.append(y_arr[right])
            res_newton.append(newton[right])
            right += 1
            cnt += 1

    return res_y, res_newton


def NewtonInterp(x_arr, y_arr, data, x, y, nx, ny):
    inter_x = inter_y = 0
    try:
        inter_x, inter_y = get_data_by_n(x_arr, data, x, nx)
    except:
        print("x out of table")
    newton = []
    for i in range(nx + 1):
        res = NewtonPreFill(nx, inter_x, inter_y[i])
        print(res, "res")
        polinom, xOfPolinom = inter_y[i][0], 1.0
        for i in range(2, nx + 2, 1):
            for j in range(len(inter_x) - i + 1):
                res[j][i] = (res[j][i - 1] - res[j + 1][i - 1]) / (res[j][0] - res[j + i - 1][0])
                if j == 0:
                    xOfPolinom *= (x - res[i - 2][0])
                    polinom += (xOfPolinom * res[j][i])
        newton.append(polinom)
        print(newton, "jj")
    newton = [newton]
    try:
        inter_y, _ = get_data_by_n(y_arr, newton, y, ny)
    except:
        print("y out of table")
    res = NewtonPreFill(ny, inter_y, newton[0])
    print(res)
    polinom, xOfPolinom = newton[0][0], 1.0
    for i in range(2, ny + 2, 1):
        for j in range(len(inter_y) - i + 1):
            res[j][i] = (res[j][i - 1] - res[j + 1][i - 1]) / (res[j][0] - res[j + i - 1][0])
            if j == 0:
                xOfPolinom *= (y - res[i - 2][0])
                polinom += (xOfPolinom * res[j][i])
    return polinom


def NewtonPreFill(size, x_arr, y_arr):
    res = [[] for i in range(size + 1)]
    for i in range(len(res)):
        res[i] = [0 for i in range(size + 2)]
        if i >= len(y_arr):
            res[i][0], res[i][1] = x_arr[i], 0
        else:
            res[i][0], res[i][1] = x_arr[i], y_arr[i]

    return res
