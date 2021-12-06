txt = open('input.txt', 'r')
input_num = txt.read().split('\n')
txt.close()

test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def count_increases(file):
    increases = 0
    first_num = 0
    sec_num = 1
    third_num = 2

    for x in file:

        while third_num <= len(file) - 1:
            # print(first_num)
            # print(sec_num)
            # print(third_num)
            # print(len(file))
            first_trio = int(file[first_num]) + int(file[sec_num]) + int(file[third_num])
            # print(first_trio)
            first_num += 1
            sec_num += 1
            third_num += 1
            second_trio = int(file[first_num]) + int(file[sec_num]) + int(file[third_num])
            if first_trio < second_trio:
                increases += 1
            print(increases)
    print(increases)


count_increases(input_num)

# WRONG ANSWERS
# Too low
# 1460
# 1461
txt.close()
