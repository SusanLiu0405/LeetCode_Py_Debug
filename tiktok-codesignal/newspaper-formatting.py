def solutions(paragraphs, aligns, width):
    results = []
    results.append("*" * (width + 2))
    for paragraph, align in zip(paragraphs, aligns):
        if align == "LEFT":
            results.extend(left_align(paragraph, width)) 
        if align == "RIGHT":
            right_align(paragraph, width)
            results.extend(right_align(paragraph, width)) 
    results.append("*" * (width + 2))
    return results

def left_align(paragraph, width):
    lines = []
    current_line = []
    current_length = 0
    
    for word in paragraph:
        word_len = len(word)
        needed_length = current_length + (1 if current_line else 0) + word_len
        
        if needed_length <= width:
            current_line.append(word)
            current_length = needed_length
        else:
            # Flush current line
            line_text = " ".join(current_line).ljust(width)
            lines.append("*" + line_text + "*")
            current_line = [word]
            current_length = word_len
    
    # Flush last line
    if current_line:
        line_text = " ".join(current_line).ljust(width)
        lines.append("*" + line_text + "*")
    
    return lines
    

def right_align(paragraph, width):
    lines = []
    current_line = []
    current_length = 0
    
    for word in paragraph:
        word_len = len(word)
        needed_length = current_length + (1 if current_line else 0) + word_len
        
        if needed_length <= width:
            current_line.append(word)
            current_length = needed_length
        else:
            line_text = " ".join(current_line).rjust(width)
            lines.append("*" + line_text + "*")
            current_line = [word]
            current_length = word_len
    
    if current_line:
        line_text = " ".join(current_line).rjust(width)
        lines.append("*" + line_text + "*")
    
    return lines


paragraphs = [["hello", "world"], ["How", "areYou", "doing"], ["Please look", "and align", "to right"]]
aligns = ["LEFT", "RIGHT", "RIGHT"]
width = 16
print(solutions(paragraphs, aligns, width))