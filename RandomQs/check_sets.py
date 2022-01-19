'''

Suppose you are given two sets of integers,AandB.  Letn=|A|=|B|.You want to determine ifA=B, i.e., if the two sets contain exactly thesame elements.  Assume that a set is represented as an unordered arrayof distinct elements.  Write pseudocode for an algorithm that solves thisproblem inO(n)expectedtime.

'''

def check_sets(A,B):
    if len(A) == len(B):
        n = len(A)
    else:
        return False

    A = list(set(A))
    B = list(set(B))

    hash_struct_A = {}
    for i in range(n):
        hash_struct_A[A[i]] = i

    for i in range(n):
        if B[i] in hash_struct_A:
            n -= 1

    return bool(n)

A = [1,2,3,4]
B = [3,2,4,1]

print(check_sets(A,B))
