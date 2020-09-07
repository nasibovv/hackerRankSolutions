
if __name__ == '__main__':
    n = int(input())

    _list = []
    for j in range(n):
        user_input = input().split()
        command = user_input.pop(0)

        if command == "append":
            _list.append(int(user_input[0]))
        elif command == "insert":
            _list.insert(int(user_input[0]), int(user_input[1]))
        elif command == "remove":
            _list.remove(int(user_input[0]))
        elif command == "sort":
            _list.sort()
        elif command == "pop":
            _list.pop()
        elif command == "reverse":
            _list.reverse()
        elif command == "print":
            print(_list)
