# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

txt = open('input.txt', 'r')
input_num = txt.read().split('\n')
txt.close()


def count_increases(file):
    # print(file)
    increases = 0
    last_num = -1
    cur_num = 0
    for x in file:

        if file[last_num] < file[cur_num]:
            increases += 1
        last_num += 1
        cur_num += 1
    print(increases)


count_increases(input_num)

txt.close()
