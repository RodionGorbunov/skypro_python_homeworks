PROCENT = 0.1


def bank(dep, year):

    for i in range(year):
        dep = dep + (dep * PROCENT)
    return dep
    

print (bank(1000, 3))
