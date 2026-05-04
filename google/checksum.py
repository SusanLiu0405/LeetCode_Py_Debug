def checksum(original_str, validation_str, k):
    for i in range(0, len(original_str), k):
        curr_part = original_str[i: i + k]
        checksum = 0
        for ch in curr_part:
            checksum += ord(ch)
            
