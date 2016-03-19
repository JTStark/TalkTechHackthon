def take(list, n):
    l = min(len(list), n)
    for _ in xrange(l):
        yield list[i]
