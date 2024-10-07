#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    
    # A set to keep track of unlocked boxes
    unlocked = set([0])
    
    # A list to act as a stack for boxes to check
    keys = [0]  # Start by checking the keys in box 0
    
    # Process boxes until there are no more keys to check
    while keys:
        current_box = keys.pop()
        
        # Get all keys in the current box
        for key in boxes[current_box]:
            if key not in unlocked and key < n:  # Only consider valid keys
                unlocked.add(key)  # Unlock the box
                keys.append(key)   # Add its keys for future exploration
    
    # Return True if all boxes are unlocked, otherwise False
    return len(unlocked) == n
