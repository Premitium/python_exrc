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

def tag_real(name, **kwargs):
    result = '<' + name
    for key, value in kwargs.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result

""">>> tag_real('img', src="monet.jpg", alt="Sunrise by Claude Monet", border=1)"""
