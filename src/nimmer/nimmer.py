import sys

STOP_WORDS = {"of", "the", "and"}


def nim(sentence: str) -> str:
    words = sentence.split()
    letters = [word[0] for word in words if word and word.lower() not in STOP_WORDS]
    return "".join(letter.upper() for letter in letters)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nimmer.py 'Your sentence here'")
        sys.exit(1)

    sentence = sys.argv[1]
    result = nim(sentence)
    print(result)
