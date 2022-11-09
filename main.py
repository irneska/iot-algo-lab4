from math import sqrt


def find_length_of_cable(distance: int, bolts: list):
    length: float = 0
    if len(bolts) <= 50:
        is_elements_in_limits: bool = True
        for bolt in bolts:
            if bolt < 1 or bolt > 100:
                is_elements_in_limits = False
                break
        if is_elements_in_limits:
            is_last_was_changed_to_one: bool = False
            index: int = 0
            for bolt in bolts:
                index += 1
                if index != len(bolts):
                    if is_last_was_changed_to_one:
                        if bolts[index] > 1:
                            length += sqrt((bolts[index] - 1)**2 + distance**2)
                        else:
                            length += distance
                        is_last_was_changed_to_one = False
                    else:
                        with_no_changes: float = sqrt((bolts[index] - bolt)**2 + distance**2)
                        with_changes: float = sqrt((1 - bolt)**2 + distance**2)
                        if with_changes > with_no_changes:
                            is_last_was_changed_to_one = True
                            length += with_changes
                        else:
                            length += with_no_changes
        else:
            print("Elements must be in limit between 1 to 100")
    else:
        print("List is longer than 50 elements")

    print(f'You need {round(length, 2)} m of cable')


def main():
    with open('input2.txt', 'r') as r:
        w: int = int(r.readline())
        list_of_height: list = list(map(int, r.readline().split()))
        find_length_of_cable(w, list_of_height)


if __name__ == '__main__':
    main()