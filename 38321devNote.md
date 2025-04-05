## Style

- Stream editor execution flow
  - **read, execute, print, repeat**

![image](https://images0.cnblogs.com/blog/446804/201303/26120808-66e6f260b7e849e593b4c9ddd649f6c0.png)

- `p` command for priting, can be used to specifically print which line; used together with -n to suppress the printing comes natively with sed command
  - `sed -n '2,$ p' employee.txt` priting with range from line 2 to the end of the file
    - `n`: line n
    - `n,m`: matchs line n to m
    - `n,+m`：line n and the subsequent m lines
    - `n~m`：starting from line n, every m line
  - pattern matching
    - `/REGEX/p`
    - `sed -n '/Raj/,/Jane/ p' employee.txt`, print the lines which Raj apprears to the line which Jane apprears
- `d` command, delete line
  - `sed '2,4 d' employee.txt ` remove the 2-4 line
  - `sed '/^$/ d' employee.txt` removes empty line
  - `sed '/^#/ d' employee.txt` removes comment line
- `w `command, write pattern space to file

### resources
[[1]](https://marslo.github.io/ibook/cheatsheet/text-processing/sed.html) sed ibook

[[2]](https://www.cnblogs.com/yangfengtao/archive/2013/03/26/2982228.html) chinese blog

[[3]](https://www.grymoire.com/Unix/Sed.html) sed, an introductory tutorial

## Image insert

- The key value of `dict` should be unique in python; if want to support one to multiple mapping, use `multidict` under `collections`
- `strip()` method of a string will remove, by default the `\s\n\t` before the after the line
- `lstrip()` only remove the empty symbol on the left of the string and vice versa for `rstring()`
- `f-string` is a new method introduced in Python 3.6+. add f before the string and allow to add variables within the string

```python
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}") #>>> Name: Alice, Age: 25
pi = 3.1415926
print(f"Pi: {pi:.2f}") # keep two digits after the decimal point
text = "hello"
print(f"Uppercase: {text.upper()}")  # invoke methods of string, >>> Uppercase: HELLO
```
* regular exrepssions
  * `re.search(a,b)`: `a` should be pattern and `b` should be a string. return `None` when no match is found; return `Match` obj when found. It has the following methods
    * `math.group()` returns the matched string
    * `match.span()` returns the starting and ending index for the match
  * special char should be escapted by `re.escape()`
```python
import re
text = "File: example.txt"
pattern = "example.txt"  # . is a special char in regex
safe_pattern = re.escape("example.txt")
print(re.findall(safe_pattern, text))  # >>> ['example.txt']
```

- dict
  - dictionary add should be done by `.update()` method or directly used `dict[key] = value` to add or update key and value
  - dict supports only unique key values
- json
  - write and read

```python
import json
data = {"name": "Alice", "age": 25, "city": "New York"}
# write
with open("data.json", "w", encoding="utf-8") as f: # data.json is the file to which data writes 
    json.dump(data, f, indent=4)  # indent for better readability

# read
with open("data.json", "r", encoding="utf-8") as f: # read data from data.json
    loaded_data = json.load(f)

print(loaded_data)  # >>> {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

- list
  - `list.index(x)` returns the index of the first elememt within the list that matchs `x`
  - can also use `enumerate()` to get all the elements within the list
```python
fruits = ["apple", "banana", "cherry", "banana"]

# obtain all the indices of "banana"
indices = [i for i, x in enumerate(fruits) if x == "banana"]
print(indices)  # >>> [1, 3]
```
* python as stream editor

|Scenarios| method| applicable for |
|:---|:---|:---|
| tunnel| `sys.stdin()`| `echo "text" \| python script.py`|
| interative| `input()`| mannually input data|
| simulated string strream| `io.String()`| test memory|
| file stream| `open()`| read data from file|
|initite stream| `generator + input()`| log and network stream|