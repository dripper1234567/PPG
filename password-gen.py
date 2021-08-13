import random


def generate(length=8):
    passw = ""
    for char in range(0, length+1):
        passw += random.randint(21, 126)
    return passw


if __name__ == "__main__":
    print(generate())
