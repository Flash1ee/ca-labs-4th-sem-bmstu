import matplotlib.pyplot as plt


def get_label(n: int, m: int, md1: int, md2: int) -> str:
    f1s = "Gauss" if not md1 else "Simpson"
    f2s = "Gauss" if not md2 else "Simpson"

    return f"N = {n}, M = {m}, Methods = {f1s}-{f2s}"


def plot(fs, sc, ns, ms, md1s, md2s) -> None:
    plt.clf()

    plt.title("Integration - meansquare method")
    plt.xlabel("Tetta")
    plt.ylabel("Result")
    plt.grid()

    for i in range(len(fs)):
        x, y = [], []
        j = sc[0]
        while j < sc[2]:
            x.append(j)
            y.append(fs[i](j))
            j += sc[1]

        plt.plot(x, y, label=get_label(ns[i], ms[i], md1s[i], md2s[i]))
    plt.legend()
    plt.show()
