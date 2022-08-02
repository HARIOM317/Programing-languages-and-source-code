import re

# Row String
print(r"\n")

Mystr = '''Python has wide range of libraries and frameworks widely used in various fields such as machine learning,
artificial intelligence, web applications, etc. We define some popular frameworks and libraries of Python
as follows.
1. Web development (Server-side) - Django Flask, Pyramid, CherryPy
2. GUIs based applications - Tk, PyGTK, PyQt, PyJs, etc.
3. Machine Learning - TensorFlow, PyTorch, Scikit-learn, Matplotlib, Scipy, etc.
4. Mathematics - Numpy, Pandas, etc.
now number is: 12398-873
now number is: 20098-233
contact numbers : 
+919876012765
+919876876765
+919765012765
+919876019886
+918897612765
+919980007665
'''

# m = re.compile(r'applications')
# m = re.compile(r'.')        # Iterate any charecter
# m = re.compile(r'^Python')        # Start with python
# m = re.compile(r'tc.$')        # Ends with tc
# m = re.compile(r'm*a*')        # Zero or more occurrence
# m = re.compile(r'ma+')        # One or more occurrence
# m = re.compile(r'ap{2}')        # Exact number
# m = re.compile(r'ap{1}|py')        # Either or

# special sequences
# m = re.compile(r'\APython')     # start with python
# m = re.compile(r'\bapp')     # start with app
# m = re.compile(r'ment\b')     # end with ment
# m = re.compile(r'\d{5}-\d{3}')

m = re.compile(r'\b91\d{10}')

matches = m.finditer(Mystr)
for match in matches:
    print(match)
