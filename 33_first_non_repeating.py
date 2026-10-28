def first_non_repeating(text):
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in text:
        if counts[ch] == 1:
            return ch
    return None


if __name__ == "__main__":
    word = input("Enter a string: ")
    print("First non-repeating character:", first_non_repeating(word))