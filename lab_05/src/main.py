from math import pi

import view
import integral


def main() -> None:
    tetta = [0.05, 0.05, 10.0]

    ns, ms = [], []
    md1s, md2s = [], []
    ints = []

    terminate = '0'
    while terminate == '0':
        try:
            ns.append(int(input("Input N: ")))
            ms.append(int(input("Input M: ")))
            param = float(input("Enter parameter: "))
            print("Entry integration mode (0 - Gauss, 1 - Simpson)")
            md1s.append(int(input("Outer integration mode: ")))
            md2s.append(int(input("Inner integration mode: ")))
        except ValueError:
            print("Invalid input data. Program is terminated.")
            return

        lm = [[0, pi / 2], [0, pi / 2]]

        ints.append(integral.Integrate(lm, [ns[-1], ms[-1]], [md1s[-1], md2s[-1]]))

        print("Result with {:.2f} as a parameter is {:.5f}".format(tetta, ints[-1](tetta)))

        end = input("If you want stop execution, entry not 0?: ")
    view.plot(ints, tetta, ns, ms, md1s, md2s)


if __name__ == '__main__':
    main()
