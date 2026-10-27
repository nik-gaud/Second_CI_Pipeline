import string


def is_pangram(text):
    letters = set()
    for ch in text.lower():
        if ch in string.ascii_lowercase:
            letters.add(ch)
    return len(letters) == 26


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Pangram:", is_pangram(sentence))
    