'''
Design a Key-Value Store with SetAll

Design a data structure that supports storing key-value pairs with the following operations.

Operations

Operation    Description
init()    Initializes the data structure.
set(index, value)    Sets the value at the given index.
get(index)    Returns the value at the given index, or -1 if it was never set.
setAll(value)    Sets all existing indices to the given value.


⸻

Constraint

All operations must run in O(1) time complexity.

⸻

Example

Input:
init()
set(0, 5)
set(3, 10)
get(0) -> returns 5
setAll(100)
set(0, 6) -> idx_val[0] = 6, idx_timestamp[4] = 6
get(0)        -> returns 100
get(3)        -> returns 100
set(0, 7)
get(0)        -> returns 7
get(3)        -> returns 100


⸻

Clarifications
• index and value are integers.
    •    An index that was never set should return -1 even after setAll.
    •    You may assume no integer overflow issues.

timestamp
value
global_timestamp -> -1
global_val -> -1
'''

'''
idx_val = {}, key = idx, val = num_val
idx_timestamp = {}, key = idx, val = timestamp


set(idx, val):
idx_val[idx] = val
idx_timestamp[idx] = curr_timestamp
curr_timestamp += 1

setAll(val):
global_timestamp = curr_timestamp
global_val = val
curr_timestamp += 1

get(idx):
if idx not in idx_val:
    return -1
else:
    this_idx_timestamp = idx_timestamp[idx]
    if this_idx_timestamp < global_timestamp:
        return global_val
    else:
        return idx_val[idx]
'''

