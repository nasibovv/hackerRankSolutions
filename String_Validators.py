if __name__ == '__main__':
    s = input()

    line1 = any(ch.isalnum() for ch in s)
    line2 = any(ch.isalpha() for ch in s)
    line3 = any(ch.isdigit() for ch in s)
    line4 = any(ch.islower() for ch in s)
    line5 = any(ch.isupper() for ch in s)

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
