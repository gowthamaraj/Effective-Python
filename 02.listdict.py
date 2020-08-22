a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:] = [1, 2, 3]
print(a)

# Item 12: Avoid Striding and Slicing in a Single Expression
x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(x[::2])
print(x[1::2])

w = 'abc'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')
print(x, z)

# Prefer Catch-All Unpacking Over Slicing
# starred expression
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

# Sort by Complex Criteria Using the key Parameter
class Tool:
    def __init__(self, name, weight):
            self.name = name
            self.weight = weight

    def __repr__(self):
        return f"Tool{self.name!r}, {self.weight!r}"


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25)
]
tools.sort(key=lambda x: len(x.name))
print(tools)
#tuple special behaviour
saw = (5, 'circular saw')
jackhammer = (5, 'jackhammer')
print(saw<jackhammer)

# Prefer get Over in and KeyError to Handle
# Missing Dictionary Keys
counters = {
 'pumpernickel': 2,
 'sourdough': 1,
}
count = counters.get(key, 0)
counters[key] = count + 1

data = {}
key = 'foo'
value = []
data.setdefault(key, value)
print('Before:', data)
value.append('hello')
print('After: ', data)

#defaultdict() over setdefault()
from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)
    def add(self, country, city):
        self.data[country].add(city)

        
visits = Visits()
visits.add('England', 'Bath')
visits.add('England', 'London')
print(visits.data)