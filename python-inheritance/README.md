# Python - Inheritance

This project explores inheritance in Python: looking up an object's attributes,
subclassing built-in types, checking exact and inherited classes, and building a
small geometry hierarchy with `BaseGeometry`, `Rectangle` and `Square`.

## Tasks

### 0. Lookup
`0-lookup.py` defines `lookup(obj)`, which returns the list of attributes and
methods available on an object.

### 1. My list
`1-my_list.py` defines `MyList`, which inherits from `list` and adds
`print_sorted()` to print itself in ascending order.

### 2. Exact same object
`2-is_same_class.py` defines `is_same_class(obj, a_class)`, which is true only
when `obj` is exactly an instance of `a_class`.

### 3. Same class or inherit from
`3-is_kind_of_class.py` defines `is_kind_of_class(obj, a_class)`, which also
accepts instances of subclasses.

### 4. Only sub class of
`4-inherits_from.py` defines `inherits_from(obj, a_class)`, true only when the
class of `obj` inherited from `a_class` (directly or indirectly), not when it is
`a_class` itself.

### 5. Geometry module
`5-base_geometry.py` defines an empty `BaseGeometry` class.

### 6. Improve Geometry
`6-base_geometry.py` adds `area()`, which raises `Exception("area() is not
implemented")`.

### 7. Integer validator
`7-base_geometry.py` adds `integer_validator(name, value)`, raising `TypeError`
for non-integers and `ValueError` for values that are zero or negative.

### 8. Rectangle
`8-rectangle.py` defines `Rectangle(BaseGeometry)` with private, validated
`width` and `height`.

### 9. Full rectangle
`9-rectangle.py` adds `area()` and the `[Rectangle] width/height` string
representation.

### 10. Square #1
`10-square.py` defines `Square(Rectangle)` with a private, validated `size` and
its own `area()`.

### 11. Square #2
`11-square.py` adds the `[Square] width/height` string representation.

## Tests

Doctest files for the tasks that require them:

- `tests/1-my_list.txt`
- `tests/7-base_geometry.txt`
