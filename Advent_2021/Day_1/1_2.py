txt = open('input.txt', 'r')
input_num = txt.read().split('\n')
txt.close()


def count_increases(file):
    increases = 0
    first_num = 0
    sec_num = 1
    third_num = 2

    for x in file:

        while third_num <= len(file) - 2:
            first_trio = int(file[first_num]) + int(file[sec_num]) + int(file[third_num])
            first_num += 1
            sec_num += 1
            third_num += 1
            second_trio = int(file[first_num]) + int(file[sec_num]) + int(file[third_num])
            if first_trio < second_trio:
                increases += 1

    print(increases)


count_increases(input_num)

txt.close()
