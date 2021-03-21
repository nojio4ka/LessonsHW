subj = {}
with open('6.txt', 'r') as f:
    for line in f:
        subject, stats = line.split(':')
        subj_sum = sum(map(int, ''.join([i for i in stats if i == '' or (i >='0' and i <='9')]).split()))
        subj[subject] = subj_sum
    print(f'Общее количество часов по предмету - \n {subj}')