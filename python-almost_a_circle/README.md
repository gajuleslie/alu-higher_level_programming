# Python - Almost a circle

This project reviews classes, inheritance, unit testing, serialization, and
JSON file handling in Python.

## Models

- `models/base.py` defines `Base`, which manages ids and JSON serialization.
- `models/rectangle.py` defines `Rectangle`, with validated attributes, area,
  display, update, and dictionary conversion.
- `models/square.py` defines `Square`, a `Rectangle` subclass with a `size`
  property and square-specific string, update, and dictionary methods.

## Tests

All tests live under `tests/` and follow the project layout:

```bash
python3 -m unittest discover tests
```

They cover every model, method, validation path, and serialization feature.
