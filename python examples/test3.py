args = [ 3 , 4 , 5 ]

print(list(args))

args = [3,6]
print(list((range(*args)))) # arguments in args are inputed as start and stop for range


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
