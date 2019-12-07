import math


def main():
    sum = 0
    fuelsum = 0

    with open("input1.txt", "r") as f:
            for lines in f:
                if lines != "\n":
                    fuel = (math.floor(int(lines) / 3) - 2)
                    sum += fuel
                    while fuel >= 0:
                        temp = (math.floor(fuel / 3) - 2)
                        if temp > 0:
                            fuelsum += temp
                        fuel = temp
    print(sum + fuelsum)


if __name__ == '__main__':
    main()
