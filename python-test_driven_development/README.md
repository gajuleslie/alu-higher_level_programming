# Python - Test-driven development

This project practices writing documentation and tests before implementation.

## Tasks

### 0. Integers addition
`0-add_integer.py` adds two integers or floats after casting them to integers.
Tests: `tests/0-add_integer.txt`.

### 1. Divide a matrix
`2-matrix_divided.py` divides every matrix element by a number and returns a
new matrix rounded to two decimal places. Tests: `tests/2-matrix_divided.txt`.

### 2. Say my name
`3-say_my_name.py` prints a formatted full name. Tests:
`tests/3-say_my_name.txt`.

### 3. Print square
`4-print_square.py` prints a square of hash characters. Tests:
`tests/4-print_square.txt`.

### 4. Text indentation
`5-text_indentation.py` prints text with two new lines after `.`, `?`, and `:`.
Tests: `tests/5-text_indentation.txt`.

### 5. Max integer - Unittest
`tests/6-max_integer_test.py` contains unittests for `max_integer`.

## Running the tests

```bash
python3 -m doctest ./tests/*
python3 -m unittest tests.6-max_integer_test
```
