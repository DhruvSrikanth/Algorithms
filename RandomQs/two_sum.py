'''

Given anunsortedarrayA[1..n] ofndistinct integers and another integerx,  give  an  algorithm  that  determines  whether  or  not  there  exists  twoelements inAwhose sum is exactlyx.  Your algorithm should run inO(n) expectedtime.

'''

def two_sum(A, sum_):
    hash_struct = {}
    for i in range(len(A)):
        if sum_ - A[i] in hash_struct:
            return True
        hash_struct[A[i]] = i
    return False
