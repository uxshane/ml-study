def zero_mat(n, p):
    Z = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            row.append(0)
        Z.append(row)
    return Z

def deepcopy(A):
    if type(A[0]) == list:
        n = len(A)
        p = len(A[0])
        res = zero_mat(n, p)
        for i in range(0, n):
            for j in range(0, p):
                res[i][j] = A[i][j]
        return res
    else:
        n = len(A)
        res = []
        for i in range(0, n):
            res.append(A[i])
        return res

def v_add(u,v):
    n = len(u)
    w = []

    for i in range(0, n):
        val = u[i] + v[i]
        w.append(val)
    return w

def v_subtract(u,v):
    n = len(u)
    w = []
    for i in range(0, n):
        val = u[i] + v[i]
        w.append(val)
    return w