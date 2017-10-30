# A module to find the path around a cube of a given width

def path(width):
    foo = []
    for i in range(width):
        foo.append([0,i])
    for i in range(1,width):
        foo.append([i,width-1])
    for i in range(width-2,-1,-1):
        foo.append([width-1,i])
    for i in range(width-2,0,-1):
        foo.append([i,0])
    if (width>2):
        foo.extend(smaller_cube(width-2))
    return foo

def smaller_cube(width):
    foo = []
    if (width == 0):
        return None
    if (width == 1):
        foo.append([1,1])
        return foo
    foo.extend(path(width))
    zz = list(map(inc,foo))
    return zz

def inc(a):
    a[0] = a[0]+1
    a[1] = a[1]+1
    return a

