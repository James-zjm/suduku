# coding:utf-8
# python2.7
import create_sudoku
import solve_sudoku
import sys
from copy import deepcopy

try:
    # command=raw_input("please input command\n")
    type = sys.argv[1]
    if type[1] == 'c':
        num = int(sys.argv[2])
        create_sudoku.Create(num)
    elif type[1] == 's':
        path = sys.argv[2]
        sudoku_str = []
        sudoku = [[0 for i in range(9)]for j in range(9)]
        sudoku_rec = []
        print path
        with open(path, "r") as f:
            line = f.readline()
            flag = 0
            while line:
                if line[0] != '\n':
                    sudoku_str.append(deepcopy(line))
                    line = f.readline()
                else:
                    for i in range(9):
                        sudoku[flag][i] = int(sudoku_str[flag][2*i])
                    sudo = solve_sudoku.Solve(sudoku)
                    sudo.calc()
                    sudoku_rec.append(deepcopy(sudo.value))
                    sudoku_str[:] = []
                    sudoku = [[0 for i in range(9)]for j in range(9)]
                    line = f.readline()
        for i in range(9):
            sudoku[flag][i] = int(sudoku_str[flag][2*i])
        sudo = solve_sudoku.Solve(sudoku)
        sudo.calc()
        sudoku_rec.append(deepcopy(sudo.value))
        with open("sudoku.txt", "w") as f:
            length = len(sudoku_rec)
            for i in range(length):
                for j in range(9):
                    for k in range(8):
                        f.write("%s " % sudoku_rec[i][j][k])
                    f.write("%s" % sudoku_rec[i][j][8])
                    f.write("\n")
                if i != (length-1):
                    f.write("\n")


except ValueError:
        print "please input correct number"
except IOError:
    print "Error: 没有找到文件或读取文件失败"
