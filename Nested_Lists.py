if __name__ == '__main__':

    all_studs = []
    num = (int(input()))
    dif_score = []
    chosen_ones = []

    if num < 2 or num > 5:
        print("no")
    else:
        for _ in range(num):
            name = input()
            score = float(input())
            temp = [name, score]
            all_studs.append(temp)

        for i, j in all_studs:
            dif_score.append(j)

        dif_score1 = list((set(dif_score)))
        dif_score1.sort()

        for i, j in all_studs:
            if j == dif_score1[1]:
                chosen_ones.append(i)

        chosen_ones.sort()

        for k in chosen_ones:
            print(k)
