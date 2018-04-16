# coding:utf-8
# python2.7
from copy import deepcopy


class Create():
    sudoku_map = []
    temp = [[0 for i in range(9)]for j in range(9)]
    count = 0
    table = [[0 for i in range(9)]for j in range(9)]

    def __init__(self, num):
        sudo_num = [1, 2, 3, 4, 6, 7, 8, 9]
        while not self.make(num, sudo_num):
            # 找到下一个全排列
            i = len(sudo_num)-2
            while i >= 0 and sudo_num[i] >= sudo_num[i+1]:
                i -= 1
            j = i + 1
            k = len(sudo_num) - 1
            while sudo_num[i] >= sudo_num[k]:
                k -= 1
            (sudo_num[i], sudo_num[k]) = (sudo_num[k], sudo_num[i])
            sudo_num[j:] = sudo_num[:j-1:-1]
        with open("sudoku.txt", "w") as f:
            length = len(self.sudoku_map)
            for i in range(length):
                for j in range(9):
                    for k in range(8):
                        f.write("%s " % self.sudoku_map[i][j][k])
                    f.write("%s" % self.sudoku_map[i][j][8])
                    if (i != (length-1)) | (j != 8):
                        f.write("\n")
                if i != (length-1):
                    f.write("\n")

    def make(self, num, sudo_num):#数独种子
        self.table[0][4] = self.table[1][1] = self.table[2][7] = self.table[3][3] = self.table[4][0] = self.table[5][6] = self.table[6][5] = self.table[7][2] = self.table[8][8] = sudo_num[0]
        self.table[0][5] = self.table[1][2] = self.table[2][8] = self.table[3][4] = self.table[4][1] = self.table[5][7] = self.table[6][3] = self.table[7][0] = self.table[8][6] = sudo_num[1]
        self.table[0][3] = self.table[1][0] = self.table[2][6] = self.table[3][5] = self.table[4][2] = self.table[5][8] = self.table[6][4] = self.table[7][1] = self.table[8][7] = sudo_num[2]
        self.table[0][7] = self.table[1][4] = self.table[2][1] = self.table[3][6] = self.table[4][3] = self.table[5][0] = self.table[6][8] = self.table[7][5] = self.table[8][2] = sudo_num[3]
        self.table[0][8] = self.table[1][5] = self.table[2][2] = self.table[3][7] = self.table[4][4] = self.table[5][1] = self.table[6][6] = self.table[7][3] = self.table[8][0] = sudo_num[4]
        self.table[0][6] = self.table[1][3] = self.table[2][0] = self.table[3][8] = self.table[4][5] = self.table[5][2] = self.table[6][7] = self.table[7][4] = self.table[8][1] = sudo_num[5]
        self.table[0][1] = self.table[1][7] = self.table[2][4] = self.table[3][0] = self.table[4][6] = self.table[5][3] = self.table[6][2] = self.table[7][8] = self.table[8][5] = sudo_num[6]
        self.table[0][2] = self.table[1][8] = self.table[2][5] = self.table[3][1] = self.table[4][7] = self.table[5][4] = self.table[6][0] = self.table[7][6] = self.table[8][3] = sudo_num[7]
        self.table[0][0] = self.table[1][6] = self.table[2][3] = self.table[3][2] = self.table[4][8] = self.table[5][5] = self.table[6][1] = self.table[7][7] = self.table[8][4] = 5
        self.temp = deepcopy(self.table)
        for c1 in range(2):
            for c2 in range(6):
                for c3 in range(6):
                    for r1 in range(2):
                        for r2 in range(6):
                            for r3 in range(6):
                                if self.count == num:
                                    return True
                                self.combine(c1, c2, c3, r1, r2, r3)
                                self.count = self.count+1
        return False
        #行列变换
    def combine(self, c1, c2, c3, r1, r2, r3):
        self.table = deepcopy(self.temp)
        if (c1 == 1):
            self.colExchange(1, 2)
        if (c2 == 1):
            self.colExchange(4, 5)
        if (c2 == 2):
            self.colExchange(3, 4)
        if (c2 == 3):
            self.colExchange(3, 4)
            self.colExchange(4, 5)
        if (c2 == 4):
            self.colExchange(3, 5)
            self.colExchange(4, 5)
        if (c2 == 5):
            self.colExchange(3, 5)
        if (c3 == 1):
            self.colExchange(7, 8)
        if (c3 == 2):
            self.colExchange(6, 7)
        if (c3 == 3):
            self.colExchange(6, 7)
            self.colExchange(7, 8)
        if (c3 == 4):
            self.colExchange(6, 8)
            self.colExchange(7, 8)
        if (c3 == 5):
            self.colExchange(6, 8)
        if (r1 == 1):
            self.rowExchange(1, 2)
        if (r2 == 1):
            self.rowExchange(4, 5)
        if (r2 == 2):
            self.rowExchange(3, 4)
        if (r2 == 3):
            self.rowExchange(3, 4)
            self.rowExchange(4, 5)
        if (r2 == 4):
            self.rowExchange(3, 5)
            self.rowExchange(4, 5)
        if (r2 == 5):
            self.rowExchange(3, 5)
        if (r3 == 1):
            self.rowExchange(7, 8)
        if (r3 == 2):
            self.rowExchange(6, 7)
        if (r3 == 3):
            self.rowExchange(6, 7)
            self.rowExchange(7, 8)
        if (r3 == 4):
            self.rowExchange(6, 8)
            self.rowExchange(7, 8)
        if (r3 == 5):
            self.rowExchange(6, 8)
        self.sudoku_map.append(deepcopy(self.table))

    def rowExchange(self, r1, r2):
        for i in range(9):
            t = self.table[r1][i]
            self.table[r1][i] = self.table[r2][i]
            self.table[r2][i] = t

    def colExchange(self, c1, c2):
        for i in range(9):
            t = self.table[i][c1]
            self.table[i][c1] = self.table[i][c2]
            self.table[i][c2] = t
