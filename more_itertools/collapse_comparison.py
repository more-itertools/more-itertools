from recipes import flatten
from recipes import flatten_2
from recipes import flatten_3
from recipes import flatten_4
from recipes import collapse
from recipes import collapse2
from recipes import collapse3
import timeit
if __name__ == "__main__":
    num_repeat = 5
    number = 1000
    setup = """
from recipes import flatten, flatten_2, flatten_3, flatten_4
from recipes import collapse, collapse2, collapse3
f0 = [[0, 1, 2], [3, 4, 5]]
f1 = [[0, [1, 2]], [[3, 4], 5]]
    """
    fs = []
    fs.append([[0, 1, 2], [3, 4, 5]])
    fs.append([[0, [1, 2]], [[3, 4], 5]])
    for i in range(len(fs)):
        test_iterable = "f" + str(i)
        print '\n===Functional results: f' + str(i) + ' ==='
        print fs[i]
        # print "EXPECTED: ", "[1,2,3,4,5]"
        print "flatten:    ", list(flatten(fs[i]))
        print "flatten_2:  ", list(flatten_2(fs[i]))
        print "flatten_3:  ", list(flatten_3(fs[i]))
        print "flatten_4:  ", list(flatten_4(fs[i]))
        print "collapse:   ", list(collapse(fs[i]))
        print "collapse2:  ", list(collapse2(fs[i]))
        print "collapse3:  ", list(collapse3(fs[i]))
        print '\n===Create generator (1000 times, in nanoseconds)==='
        print "flatten:  ",
        print min(timeit.repeat(
            stmt='flatten(' + test_iterable + ')',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "flatten 2:",
        print min(timeit.repeat(
            stmt='flatten_2(' + test_iterable + ')',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "flatten_3:",
        print min(timeit.repeat(
            stmt='flatten_3(' + test_iterable + ')',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "flatten_4:",
        print min(timeit.repeat(
            stmt='flatten_4(' + test_iterable + ')',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "collapse: ",
        print min(timeit.repeat(
            stmt='collapse(' + test_iterable + ')',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "collapse2: ",
        print min(timeit.repeat(
            stmt='collapse2(' + test_iterable + ')',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000

        print "collapse3: ",
        print min(timeit.repeat(
            stmt='collapse3(' + test_iterable + ')',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000

        print '\n===Use generator to create a list (1000 times, in nanoseconds)==='
        print "flatten:  ",
        print min(timeit.repeat(
            stmt='list(flatten(' + test_iterable + '))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "flatten 2:",
        print min(timeit.repeat(
            stmt='list(flatten_2(' + test_iterable + '))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "flatten_3:",
        print min(timeit.repeat(
            stmt='list(flatten_3(' + test_iterable + '))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "flatten_4:",
        print min(timeit.repeat(
            stmt='list(flatten_4(' + test_iterable + '))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "collapse: ",
        print min(timeit.repeat(
            stmt='list(collapse(' + test_iterable + '))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "collapse2:",
        print min(timeit.repeat(
            stmt='list(collapse2(' + test_iterable + '))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "collapse3:",
        print min(timeit.repeat(
            stmt='list(collapse3(' + test_iterable + '))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "collapse2 w/ levels = 0:",
        print min(timeit.repeat(
            stmt='list(collapse2(' + test_iterable + ', levels=0))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "collapse3 w/ levels = 0:",
        print min(timeit.repeat(
            stmt='list(collapse3(' + test_iterable + ', levels=0))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "collapse2 w/ levels = 1:",
        print min(timeit.repeat(
            stmt='list(collapse2(' + test_iterable + ', levels=1))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
        print "collapse3 w/ levels = 1:",
        print min(timeit.repeat(
            stmt='list(collapse3(' + test_iterable + ', levels=1))',
            setup=setup,
            number=number,
            repeat=num_repeat
        )) * 1000
