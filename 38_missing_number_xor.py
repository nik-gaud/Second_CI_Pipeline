def find_missing_number(numbers, n):
    result = 0
    for i in range(1, n + 1):
        result ^= i
    for num in numbers:
        result ^= num
    return result


if __name__ == "__main__":
    n = int(input("Enter n (numbers from 1 to n): "))
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Missing number:", find_missing_number(nums, n))