"""The *args only collects positional arguments"""

def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

"""Fix problem when no arguments are passed"""

def hypervolume_accepts_zero_args(length, *lengths):
    v = length
    for item in lengths
        v *= item
    return v

"""The *kwargs collects key word arguments"""

def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))
