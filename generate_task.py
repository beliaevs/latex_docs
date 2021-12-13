import random
import numpy as np

def generate_task():
    operations = ['+', '-']
    MaxResult = 100
    a = random.randrange(1, 99)
    sign = random.choice(operations)
    if sign == '-':
        b = random.randrange(0, a)
    else:
        b = random.randrange(0, MaxResult - a)
    return (a, sign, b)

def task2equation(task):
    return str(task[0]) + str(task[1]) + str(task[2]) + '&='

def generate_multiplication_tasks(rows, columns):
    num = rows*columns
    pairs = [(i, j) for i in range(2, 10) for j in range(2, 10)]
    m = (num // len(pairs))
    rem = num % len(pairs)
    q = (m if rem == 0 else (m+1))
    pairs = pairs * q
    selected = random.sample(pairs, num)
    return np.array_split([(a, r'\times ', b) for (a, b) in selected], rows)

def generate_shuffled_multiplication():
    res = []
    for i in range(2, 10):
        for j in range(i, 10):
            res.append((i, r'\cdot', j))
    random.shuffle(res) 
    return np.array_split(res, 9)

def generate_shuffled_division():
    res = []
    for i in range(2, 10):
        for j in range(i, 10):
            res.append((i*j, ':', i))
    random.shuffle(res)
    return np.array_split(res, 9)

def main():
    myseed = '4uuu645ye70ja'
    random.seed(myseed)

    generator_mark = '%% generated by generate_task.py. Seed: ' + myseed
    headers = [generator_mark, r'\documentclass[12pt, a4paper]{article}', r'\usepackage{amsmath}',  r'\pagestyle{empty}', r'\begin{document}', r'\begin{align*}']
    footers = [r'\end{align*}', r'\end{document}']
    
    equations = []
    #samples = generate_shuffled_multiplication()
    samples = generate_shuffled_division()

    for row in samples:
        equation_row = ' & '.join([task2equation(p) for p in row])
        equations.append(equation_row)

    equations_string = '\\\\\n'.join(equations)
    complete_text = '\n'.join(headers) + '\n' + equations_string + '\n' + '\n'.join(footers)
    print(complete_text)

if __name__=='__main__':
    main()