#!/bin/python3

import os
from datetime import datetime

def time_delta(t1, t2):
    df = '%a %d %b %Y %H:%M:%S %z'
    res = datetime.strptime(t1, df) - datetime.strptime(t2, df)
    return str(abs(int(res.total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
