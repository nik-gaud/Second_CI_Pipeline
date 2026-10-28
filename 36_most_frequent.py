def most_frequent(items):
    if len(items) == 0:
        return None
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    best = items[0]
    for item in items:
        if counts[item] > counts[best]:
            best = item
    return best


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Most frequent element:", most_frequent(nums))