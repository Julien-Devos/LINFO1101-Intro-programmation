def matrix_for_traces(l, theta_1, theta_2):
    mat = []
    for i in l:
        row = []
        for j in l:
            if cross(i, j, theta_1, theta_2):
                row.append(1)
            else:
                row.append(0)
        mat.append(row)
    return mat


def cross(trace_1, trace_2, theta_1, theta_2):
    for i in trace_1:
        for j in trace_2:
            t1, t2 = i[0], j[0]
            if t1 - t2 <= theta_1 and euclidian_distance(i[1], j[1]) < theta_2:
                return True
