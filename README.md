# Specific Ways to Write Better Python

1. Pythonic Thinking
> The Python community has come to use the adjective Pythonic to
describe code that follows a particular style. The idioms of Python
have emerged over time through experience using the language and
working with others. 

  - Know Which Version of Python You’re Using
  - Follow the PEP 8 Style Guide
  - Know the Differences Between bytes and str
  - Prefer Interpolated F-Strings Over C-style Format Strings and str.format
  - Write Helper Functions Instead of Complex Expressions
  - Prefer Multiple Assignment Unpacking Over Indexing
  - Prefer enumerate Over range
  - Use zip to Process Iterators in Parallel
  - Avoid else Blocks After for and while Loops
  - Prevent Repetition with Assignment Expressions

2. Lists and Dictionaries
> In Python, the most common way to organize information is in a sequence of values stored in a list. A list’s natural complement is the dict that stores lookup keys mapped to corresponding values.

  - Know How to Slice Sequences
  - Avoid Striding and Slicing in a Single Expression
  - Prefer Catch-All Unpacking Over Slicing
  - Sort by Complex Criteria Using the key Parameter
  - Be Cautious When Relying on dict Insertion Ordering
  - Prefer get Over in and KeyError to Handle Missing Dictionary Keys
  - Prefer defaultdict Over setdefault to Handle Missing Items in Internal State
  - Know How to Construct Key-Dependent Default Values with '__missing__'