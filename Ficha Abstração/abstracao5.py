def vec(x, y):
    return (x, y)

def vecx(vec):
    return vec[0]

def vecy(vec):
    return vec[1]

def is_vec(vec):
    if type(vec) != tuple or len(vec) != 2:
        return False
    return True

def is_vec_nul(vec):
    if not is_vec(vec) or vecx(vec) != 0 or vecy(vec) != 0:
        return False
    return True

def is_vec_equal(vec1, vec2):
    if not is_vec(vec1) or not is_vec(vec2) or vecx(vec1) != vecx(vec2) or vecy(vec1) != vecy(vec2): 
        return False
    return True

def vec_dot(vec1, vec2):
    return vecx(vec1) * vecx(vec2) + vecy(vec1) * vecy(vec2)

print(vec_dot(vec(1,2),vec(2,3)))