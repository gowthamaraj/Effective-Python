# Item 19: Never Unpack More Than Three Variables When Functions Return Multiple Values
def get_stats(numbers: list)-> tuple:
    return min(numbers), max(numbers)
lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
min, max = get_stats(lengths)
print(f'Min: {min}, Max: {max}')

# Prefer Raising Exceptions to Returning None
def careful_divide(a: float, b: float) -> float:
    """Divides a by b.
    Raises:
    ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')
x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)

# Item 21: Know How Closures Interact with Variable Scope
# Reduce Visual Noise with Variable Positional
# Arguments

# def safe_division_e(numerator, denominator, /,ndigits=10, *, ignore_overflow=False, ignore_zero_division=False):
#     try:
#         fraction = numerator / denominator # Changed
#         return round(fraction, ndigits) # Changed
#     except OverflowError:
#         if ignore_overflow:
#             return 0
#         else:
#             raise
#     except ZeroDivisionError:
#         if ignore_zero_division:
#             return float('inf')
#         else:
#             raise

from functools import wraps
def trace(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        print("wrapper")
        return fun(*args, **kwargs)
    return wrapper

@trace
def makehi(msg: str) -> str:
    """
    concat string
    """
    return 'hi' + ' ' + msg

print(makehi('gowtham'))
print(help(makehi))

