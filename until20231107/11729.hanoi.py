count = 0
process = []


def move_disk(disk_num, start_peg, end_peg):
    global count
    process.append([start_peg, end_peg])
    count += 1


def hanoi(num_disks, start_peg=1, end_peg=3):
    if num_disks == 0:
        return
    other_peg = 6 - start_peg - end_peg
    hanoi(num_disks - 1, start_peg, other_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, other_peg, end_peg)


hanoi(int(input()))
print(count)
for t in process:
    print(*t)
