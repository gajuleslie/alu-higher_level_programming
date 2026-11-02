# Python - Exceptions

This project covers Python exceptions: catching them, raising them, and using
`try` / `except` / `finally`.

## Tasks

### 0. Safe list printing
`0-safe_print_list.py` has a function `safe_print_list(my_list=[], x=0)` that
prints `x` elements of a list on one line and returns the number of elements
actually printed.

### 1. Safe printing of an integers list
`1-safe_print_integer.py` has a function `safe_print_integer(value)` that
prints an integer using `"{:d}".format()`, returning `True` on success and
`False` otherwise.

### 2. Print and count integers
`2-safe_print_list_integers.py` has a function
`safe_print_list_integers(my_list=[], x=0)` that prints the first `x`
integers of a list on one line, skipping other types, and returns how many
integers were printed.

### 3. Integers division with debug
`3-safe_print_division.py` has a function `safe_print_division(a, b)` that
divides two integers, prints `Inside result: <result>` in the `finally`
section, and returns the result or `None` on failure.

### 4. Divide a list
`4-list_division.py` has a function
`list_division(my_list_1, my_list_2, list_length)` that divides two lists
element by element and reports wrong types, division by 0, and out-of-range
indexes.

### 5. Raise exception
`5-raise_exception.py` has a function `raise_exception()` that raises a
`TypeError`.

### 6. Raise a message
`6-raise_exception_msg.py` has a function `raise_exception_msg(message="")`
that raises a `NameError` with the given message.
