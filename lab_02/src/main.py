import src.interp as interp


def main():
    x_arr, y_arr, data = interp.read_data("./data/points.txt")
    x = y = nx = ny = 0
    try:
        x, y, nx, ny = interp.input_data()
    except:
        print("Error input data")

    res = interp.NewtonInterp(x_arr, y_arr, data, x, y, nx, ny)
    print(res)


if __name__ == "__main__":
    main()
