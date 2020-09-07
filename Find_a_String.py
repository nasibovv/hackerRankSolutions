
def count_substring(string, sub_string):
    k, count = 0, 0
    for _ in range(0, len(string)):
        if string[k:(len(sub_string)+k)] == sub_string:
            count += 1
        k += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)