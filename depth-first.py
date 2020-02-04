import numpy as np


def main():
    f = open("input-text/initial.txt", "r")
    newArr = []
    if f.mode == 'r':
        contents = f.readlines()
        for x in contents:
            y = x.split(" ")
            arr_size = int(y[0])
            max_d = y[1]
            for z in y[3]:
                newArr.append(int(z))
            #print(newArr)
            chunks(newArr, arr_size)
           # print(newArr)
            newArr2 = np.array_split(newArr, arr_size)
           # print(newArr2[0][0])
            for i in range(len(newArr2)):
                for j in range(len(newArr2[i])):
                    print(newArr2[i][j], end='')
                print()

            # a = np.array(newArr)
            # a.reshape((arr_size, arr_size))
            # print(a[1][1])



def chunks(l, n):
    n = max(1, n)
    return (l[i:i + n] for i in range(0, len(l), n))

main()

# 1 0 1
# 1 1 1
# 0 0 0

