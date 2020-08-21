# checking the python version
import sys
print(sys.version_info)
print(sys.version)

# use of multiline statement
string_info = 'PEP 8 provides a wealth of details about how to write clear Python code. It continues to be updated as the Python language evolves.\
It’s worth reading the whole guide online (https://www.python.org/dev/peps/pep-0008/).\
Here are a few rules you should be sure tofollow.'
print(string_info)

# Don’t check for empty containers or sequences (like [] or '') by comparing the length to zero (if len(somelist) == 0). 
# Use if not somelist and assume that empty values will implicitly evaluate to False.
data_list = [1,2,3,4]
if data_list:
    print(data_list)

# byte vs string
string_byte = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-16')
print(string_byte)

# Prefer Multiple Assignment Unpacking Over Indexing
favorite_snacks = {
'salty': ('pretzels', 100),
'sweet': ('cookies', 180),
'veggie': ('carrots', 20),
}
((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items()

# enumeration
snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for i,(snack,calories) in enumerate(snacks):
    print(f"{i} {snack} {calories}")

#  walrus operator only after pythonV3.8
# list_money = [1,2,3,4]
# if (test := list_money[0])%2:
#     print('odd',test)
# else:
#     print('even',test)
