# Them cac thu vien neu can
from dataclasses import dataclass

from typing import List


@dataclass
class Point:
    x: int
    y: int


def euclid_distance(point1, point2):
    return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** (1 / 2)


def total_distance(point, *args):
    if args is None:
        return 0
    total = euclid_distance(point, args[0])
    for i, _ in enumerate(args[:-1]):
        total += euclid_distance(args[i], args[i + 1])
    return total


def cost(distance):
    return distance * 20 / 40 + 10


@dataclass
class Order:
    location: Point
    volume: int
    weight: int

    def income(self):
        return 5 + self.volume + self.weight * 2


@dataclass
class Shipper:
    w_location: Point
    orders: List[Order]

    def cost(self):
        locations = [_.location for _ in self.orders]
        incomes = sum([_.income() for _ in self.orders])
        # print(locations)
        distance = total_distance(self.w_location, *locations)
        return incomes - distance


def evaluate_function(li: List[Shipper]):
    f = [shipper.cost() for shipper in li]
    print(f)
    return sum([abs(x - y) for y in f for x in f])


def euler_candies(n, k):
    res = [0 for _ in range(k)]
    index = 0
    while n > 0:
        res[index % k] += min(n, index + 1)
        n -= (index + 1)
        index += 1
    return res


@dataclass
class Problem:
    location: Point
    n_orders: int
    n_shipper: int
    orders: List[Order]


def assign(file_input, file_output):
    # read input
    orders = []
    with open(file_input) as reader:
        w = Point(*[int(_) for _ in reader.readline().split()])
        n, m = [int(_) for _ in reader.readline().split()]
        for line in reader:
            line = [int(_) for _ in line.split()]
            orders.append(Order(Point(line[0], line[1]), line[2], line[3]))
    a = Shipper(w, [orders[0], orders[3]])
    b = Shipper(w, [orders[2]])
    c = Shipper(w, [orders[4], orders[1]])
    # print(Problem(w, n, m, orders))
    print(evaluate_function([a, b, c]))
    print(euler_candies(n, m))
    # run algorithm

    # write output
    return None


assign('input.txt', 'output.txt')
