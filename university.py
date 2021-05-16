n = int(input('Enter the number of avaible spots for the deparments.'))
departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

applicant_list = []

with open('applicant_list.txt') as file:
    for line in file:
        applicant_list.append(line.strip('\n').split())
def physics():
    for i in applicant_list:
        mean = (int(i[2]) + int(i[4])) / 2
        i.append(str(max(float(i[6]), mean)))
def biotech():
    for i in applicant_list:
        mean = (int(i[2]) + int(i[3])) / 2
        i.append(str(max(float(i[6]), mean)))
def engeniring():
    for i in applicant_list:
        mean = (int(i[4]) + int(i[5])) / 2
        i.append(str(max(float(i[6]), mean)))
def chemistry():
    for i in applicant_list:
        i.append(str(max(float(i[6]), float(i[3]))))
def math():
    for i in applicant_list:
        i.append(str(max(float(i[6]), float(i[4]))))

chemistry()
math()
physics()
biotech()
engeniring()

def sorting(m):
    global applicant_list
    physics_sorted = sorted(applicant_list, key = lambda x: (-float(x[-3]), x[0], x[1]))
    chemistry_sorted = sorted(applicant_list, key = lambda x: (-float(x[-5]), x[0], x[1]))
    math_sorted = sorted(applicant_list, key = lambda x: (-float(x[-4]), x[0], x[1]))
    cs_sorted = sorted(applicant_list, key = lambda x: (-float(x[-1]), x[0], x[1]))
    biotech_sorted = sorted(applicant_list, key = lambda x: (-float(x[-2]), x[0], x[1]))
    for i in biotech_sorted:
        if i[m] == 'Biotech':
            if len(departments['Biotech']) >= n:
                pass
            else:
                departments['Biotech'].append([i[0], i[1], i[-2]])
                applicant_list.remove(i)

    for i in chemistry_sorted:
        if i[m] == 'Chemistry':
            if len(departments['Chemistry']) >= n:
                pass
            else:
                departments['Chemistry'].append([i[0], i[1], i[-5]])
                applicant_list.remove(i)


    for i in cs_sorted:
        if i[m] == 'Engineering':
            if len(departments['Engineering']) >= n:
                pass
            else:
                departments['Engineering'].append([i[0], i[1], i[-1]])
                applicant_list.remove(i)


    for i in math_sorted:
        if i[m] == 'Mathematics':
            if len(departments['Mathematics']) >= n:
                pass
            else:
                departments['Mathematics'].append([i[0], i[1], i[-4]])
                applicant_list.remove(i)


    for i in physics_sorted:
        if i[m] == 'Physics':
            if len(departments['Physics']) >= n:
                pass
            else:
                departments['Physics'].append([i[0], i[1], i[-3]])
                applicant_list.remove(i)

for i in range(7, 9):
    sorting(i)

for k,v in departments.items():
    v = sorted(v, key = lambda x: (-float(x[-1]), x[-3], x[-2]))
    with open(f'{k}.txt', 'w') as file:
        for student in v:
            file.write(' '.join(student) + '\n')
