from copy import deepcopy

class Set:
    def __init__(self, V):
        self._elements = V

    def Elements(self):
        return selection_sort(self._elements)




S = Set([(0, 3),(0, 1),(1, 3),(1, 0)])
print(S._elements)

print(S.Elements())
#S.Elements()
















def lexik_ordnung(a,b):
    if a[0] < b[0] or (a[0] == b[0] and a[1] <= b[1]):
        return True

def selection_sort(A):
    B = []
    
    for x in A:
        B.append(list(x))
    n = len(A)
    for i in range(0, n-1):
        for j in range(i+1,n):
            if not lexik_ordnung(B[i],B[j]):
                B[i],B[j] = B[j],B[i]
    C = []
    for x in B:
        C.append(tuple(x))
    return C
