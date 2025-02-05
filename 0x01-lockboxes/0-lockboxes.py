def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    :param boxes: List of lists, where each sublist contains keys to other boxes.
    :return: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = set([0])  # Start with the first box unlocked
    keys = set(boxes[0])  # Collect initial keys from the first box

    while keys:
        key = keys.pop()  # Take a key
        if key < n and key not in opened:  # If key corresponds to a valid and unopened box
            opened.add(key)  # Mark the box as opened
            keys.update(boxes[key])  # Add new keys from the newly opened box
        
        if len(opened) == n:  # If all boxes are opened, return True
            return True
    
    return len(opened) == n  # Check if all boxes were opened
