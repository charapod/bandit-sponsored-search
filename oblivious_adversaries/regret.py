############ 
# Implements the regret in the discretized case
############ 

import numpy as np

def regret(r_lst, alloc, bid_space, algo_util, T):
    # size of tmp: T x bid_space
    tmp = [[0 for _ in range(0,bid_space)] for _ in range(0,T+1)]

    for t in range(0,T+1):
        for b in range(0,bid_space):
            tmp[t][b] += r_lst[t][b]*alloc[t][b]


    util = []
    for b in range(0,bid_space):
        s = 0
        for t in range(0,T+1):
            s += tmp[t][b]
        util.append(s)
        

    max_util_hindsight = np.max(util)
    return (max_util_hindsight - sum(algo_util))



