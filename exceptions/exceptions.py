import sys
from math import log


def convert(s):
    """Convert to int."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)),
            file=sys.stderr)
        raise


def string_log(s):
    v = convert(s)
    return log(v)
