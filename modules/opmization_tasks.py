basketball_players = [
    {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
    {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
    {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
]

football_players = [
    {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
    {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
    {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
    {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"},
]


def plays_both(fst_lst: list, scnd_lst: list) -> list:
    fst_map = {}
    plays_both = []
    for i in range(0, len(fst_lst)):
        fst_map[fst_lst[i]["first_name"] + " " + fst_lst[i]["last_name"]] = True

    for j in range(0, len(scnd_lst)):
        if scnd_lst[j]["first_name"] + " " + scnd_lst[j]["last_name"] in fst_map:
            plays_both.append(
                scnd_lst[j]["first_name"] + " " + scnd_lst[j]["last_name"]
            )

    return plays_both


def find_missing_int(nums: list) -> int:
    # given a list of ints, find the one that is missing
    sorted_nums = sorted(nums)
    for i in range(0, len(sorted_nums) - 1):
        if sorted_nums[i + 1] - sorted_nums[i] > 1:
            return sorted_nums[i] + 1
    return "list complete"


numbers = [1, 5, 4, 2, 6, 10, 9, 8, 7]


def stock_trader(nums: list) -> int:
    # from a list of stock prices find the greatest profit that can be made from a single buy and sell
    current_low = float("inf")
    profit = 0
    for i in nums:
        if i < current_low:
            current_low = i
        if i - current_low > profit:
            profit = i - current_low
    return profit


prices = [10, 7, 5, 8, 11, 2, 6]


def highest_product(nums: list) -> int:
    # find the highest product from a list of ints
    lowest = 0
    second_lowest = 0
    highest = 0
    second_highest = 0
    for i in nums:
        if i < lowest:
            second_lowest = lowest
            lowest = i
        elif i < second_lowest:
            second_lowest = i
        elif i > highest:
            second_highest = highest
            highest = i
        elif i > second_highest:
            second_highest = i
    if highest * second_highest > lowest * second_lowest:
        return highest * second_highest
    return lowest * second_lowest


ints = [5, -10, -6, 9, 4]
more_ints = [3, 6, 10, -7, 12, -3]

if __name__ == "__main__":
    print(plays_both(basketball_players, football_players))
    print(find_missing_int(numbers))
    print(stock_trader(prices))
    print(highest_product(ints))
    print(highest_product(more_ints))
