def take(list, n):
    l = min(len(list), n)
    for i in xrange(l):
        yield list[i]
