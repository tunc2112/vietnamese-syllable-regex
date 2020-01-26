# Documentation

## `split_vietnamese_syllable(s, keeping_tone=True)`

Return a tuple `(onset, rime)`.

Split a Vietnamese syllable into onset and rime.

With `keeping_tone`, tone will **not be removed** from the result.

For example:

```python
split_vietnamese_syllable("ngoéo", True)   # return ("ng", "oéo")
split_vietnamese_syllable("ngoéo", False)  # return ("ng", "oeo")
```
