Here’s the Python program to rotate a list to the right by `k` steps:

```python
def rotate_list(lst, k):
    # Handle cases where k is greater than the list length
    k = k % len(lst)
    # Rotate the list
    rotated_list = lst[-k:] + lst[:-k]
    return rotated_list

# Input
lst = [1, 2, 3, 4, 5]
k = 2

# Output
result = rotate_list(lst, k)
print("Rotated List:", result)
```

### **Explanation**:
1. **`k = k % len(lst)`**:
   - This ensures that if `k` is larger than the length of the list, it wraps around.
   - For example, if `k = 7` and `len(lst) = 5`, `k` becomes `7 % 5 = 2`.

2. **Rotation**:
   - `lst[-k:]` gets the last `k` elements of the list.
   - `lst[:-k]` gets the elements of the list excluding the last `k`.
   - Concatenating these two parts (`lst[-k:] + lst[:-k]`) gives the rotated list.

### **Output**:
```
Rotated List: [4, 5, 1, 2, 3]
```