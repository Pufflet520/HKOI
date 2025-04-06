import re

def convert_to_tex_quotes(text):
    # Split the text into paragraphs
    paragraphs = re.split(r'(\s*\n\s*\n|\s*\\par\s*)', text)
    new_text = ""
    for paragraph in paragraphs:
        # Reset quote flag at the start of each paragraph
        replace_with_open = True
        converted_paragraph = ""
        
        for index in range(len(paragraph)):
            if paragraph[index] == '"' and not (index > 0 and paragraph[index-1] == '\\'):
                # Replace double-quote with correct TEX representation
                converted_paragraph += '``' if replace_with_open else "''"
                replace_with_open = not replace_with_open
            else:
                # Otherwise, just keep the current character
                converted_paragraph += paragraph[index]
        
        # Reset unclosed opening quotes at end of a paragraph
        if not replace_with_open:
            converted_paragraph = converted_paragraph[::-1].replace("``"[::-1], "", 1)[::-1]
        
        new_text += converted_paragraph
    return new_text

source_text = ""
try:
    while True:  # read until \endinput command
        line = input()
        if line.strip() == '\\endinput':
            source_text += line + '\n'
            break
        else:
            source_text += line + '\n'
except EOFError:
    pass  # Handle EOF if input does not contain '\endinput'

converted_text = convert_to_tex_quotes(source_text)

# Output the converted text
print(converted_text, end="")
# https://judge.hkoi.org/submission/1164108/details?sharing=2NShKeTWKpW0FaXGSjCFYGvT1w
# 評測結果
# 子任務	測試	結果	執行時間	記憶體	分數
# 1	1	正確	0.062 s	12.172 MB	100.000
# 1	2	正確	0.062 s	12.234 MB	100.000
# 1	3	正確	0.063 s	12.156 MB	100.000
# 1	4	正確	0.064 s	12.246 MB	100.000
# 1	5	正確	0.064 s	12.199 MB	100.000
# 1	6	正確	0.061 s	12.172 MB	100.000
# 1	7	正確	0.060 s	12.184 MB	100.000
# 1	8	正確	0.061 s	12.168 MB	100.000
# 1	9	正確	0.065 s	12.227 MB	100.000
# 1	10	正確	0.064 s	12.250 MB	100.000
# 2024-05-12 10:05:18
