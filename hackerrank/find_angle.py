# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def find_angle(ab, bc):
    top_angle = math.degrees(math.atan(bc/ab))
    low_angle = 180 - 90 - top_angle

    ac2 = math.sqrt(pow(ab, 2) + pow(bc, 2)) / 2

    h2b = math.sqrt(
        pow(ac2, 2) + pow(bc, 2) -
        (2*ac2*bc * math.cos(math.radians(low_angle)))
    )

    new_angle = (pow(h2b, 2) + pow(bc, 2) - pow(ac2, 2)) / (2 * h2b * bc)

    new_angle = math.acos(new_angle)
    result = round(math.degrees(new_angle))
    print(str(result) + "°")


if __name__ == '__main__':
    ab, bc = int(input()), int(input())
    find_angle(ab, bc)
