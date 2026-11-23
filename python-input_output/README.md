# Python - Input and Output

This project covers file I/O (UTF-8 text and JSON), object serialization, and
Pascal's triangle.

## Tasks

### 0. Read file
`0-read_file.py` has `read_file(filename="")`, which prints the contents of a
UTF-8 text file to stdout using a `with` statement.

### 1. Write to a file
`1-write_file.py` has `write_file(filename="", text="")`, which writes text to
a file (creating or overwriting it) and returns the number of characters
written.

### 2. Append to a file
`2-append_write.py` has `append_write(filename="", text="")`, which appends
text to a file and returns the number of characters added.

### 3. To JSON string
`3-to_json_string.py` has `to_json_string(my_obj)`, which returns the JSON
representation of an object as a string.

### 4. From JSON string to object
`4-from_json_string.py` has `from_json_string(my_str)`, which returns the
Python object represented by a JSON string.

### 5. Save object to a file
`5-save_to_json_file.py` has `save_to_json_file(my_obj, filename)`, which
writes an object to a file as JSON using a `with` statement.

### 6. Create object from a JSON file
`6-load_from_json_file.py` has `load_from_json_file(filename)`, which reads a
JSON file and returns the represented object using a `with` statement.

### 7. Load, add, save
`7-add_item.py` loads `add_item.json` (using task 6's function), appends all
command-line arguments to the list, and saves it back (using task 5's
function).

### 8. Class to JSON
`8-class_to_json.py` has `class_to_json(obj)`, which returns the instance's
`__dict__` for JSON serialization.

### 9. Student to JSON
`9-student.py` defines `Student` with `first_name`, `last_name` and `age`, plus
a `to_json()` method.

### 10. Student to JSON with filter
`10-student.py` extends `to_json(attrs=None)` so a list of attribute names can
restrict which attributes are returned.

### 11. Student to disk and reload
`11-student.py` adds `reload_from_json(json)`, which replaces the student's
attributes with values from a dictionary.

### 12. Pascal's Triangle
`12-pascal_triangle.py` has `pascal_triangle(n)`, which returns the first `n`
rows of Pascal's triangle, or an empty list when `n <= 0`.
