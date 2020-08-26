# Generators can improve performance, reduce memory usage, and
# increase readability.

# Use Comprehensions Instead of map and filter
even = [e for e in range(0,100) if e%2==0]
print(even)

even_squares_dict = {x: x**2 for x in list(range(0,100)) if x % 2 == 0}
print(even_squares_dict)

# Avoid More Than Two Control Subexpressions in Comprehensions
for i in range(0,10):
    pass
print(i)

# Consider Generators Instead of Returning Lists
class ReadVisits:
 def __init__(self, data_path):
    self.data_path = data_path
 def __iter__(self):
    with open(self.data_path) as f:
        for line in f:
            yield int(line)

it = (len(x) for x in open('file.txt'))
print(it)
print(next(it))