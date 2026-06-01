# AI Preemptive Bug Fixing

## Files
- vulnerable_code.c → Original buggy implementation
- fixed_code.c → Corrected safe implementation

## AI Tool Used
ChatGPT (Senior C Developer role)

## Issues Found

### 1. Logical Error
The loop moves `current` until it becomes NULL, so assigning `current = new_node` does not link the node into the list. It only changes a local pointer.

### 2. Memory Safety Error
The function does not check if `malloc` returns NULL. This can cause segmentation faults when dereferencing `new_node`.

## Fix Summary
- Proper traversal using `current->next`
- Correct linking using `current->next = new_node`
- Added malloc NULL check
