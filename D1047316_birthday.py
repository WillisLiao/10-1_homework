import math
import numpy as np
import pandas as pd
import matplotlib as plt
import random as rand
date_choice= list(range(1,366))
times=0
while True:
    times+=1
    date_list=np.random.choice(date_choice, times)
    frequencies = [ sum(date_list==x)/times for x in range(1, 366)]
    if  0.8 in frequencies:
        print(times)
        break
        

