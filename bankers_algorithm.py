Available = [3, 3, 2]

Max = [[7,5,3],
       [3,2,2],
       [9,0,2],
       [2,2,2],
       [4,3,3]]

Allocation = [[0,1,0],
              [2,0,0],
              [3,0,2],
              [2,1,1],
              [0,0,2]]

Need = []
sequence = []

for i in range(5):
    Need.append([])
    for j in range(3):
        Need[i].append(Max[i][j]-Allocation[i][j])

finish = [False, False, False, False, False]

for i in range(5):
    process_to_run = -1
    for j in range(5):
        if finish[j]==False:
            need_less = True
            for k in range(3):
                if Need[j][k] > Available[k]:
                    need_less = False
            if need_less:
                process_to_run = j
                finish[j] = True
                sequence.append(j)
                break
    if process_to_run == -1:
        break
    else:
        for j in range(3):
            Available[j] += Allocation[process_to_run][j]

unsafe = False
for i in range(5):
    if finish[i] == False:
        unsafe = True

if unsafe:
    print("No safe sequence found, there is a deadlock")
else:
    print(sequence)
    print(Available)
        


