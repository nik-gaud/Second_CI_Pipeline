def rotate_string(text, k):
    n = len(text)
    if n == 0:
        return ""
    k = k % n
    if k == 0:
        return text
    return text[-k:] + text[:-k]


if __name__ == "__main__":
    word = input("Enter a string: ")
    k = int(input("Enter k: "))
    print("Rotated string:", rotate_string(word, k))