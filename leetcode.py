import time

k = 2

winner = 0
win_cout = 0

my_list = [99, 11, 22, 33, 44, 55, 66, 77, 88, 100]

while True:
    if my_list[0] < my_list[1]:
        winner = my_list[0]
        my_list.append(my_list[0])
        my_list.pop(0)
        if winner == my_list[0]:
            win_cout += 1
        if win_cout == k:
            print(my_list[0])
            break

    elif my_list[0] > my_list[1]:
        winner = my_list[0]
        my_list.append(my_list[1])
        my_list.pop(1)
        if winner == my_list[0]:
            win_cout += 1

        if win_cout == k:
            print(my_list[0])
            break
