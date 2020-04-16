"""
Read in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file.
The program finds these occurrences and prompt the user to replace them.
"""
import re, pyinputplus as pyip

# Find keywords & replace with new words
print("Find keywords & replace with new words")
txt = ""
textObj = open('mad_lib.txt', 'r')
txt = textObj.read()
print(f'Origin Text -> {txt}')
capital_regex = re.compile(r'\s+\b[A-Z]{2,}')
keyword_obj = capital_regex.findall(txt)

# Raise questions
for i in range(len(keyword_obj)):
    input_txt = pyip.inputStr(prompt='Enter a ' + str(keyword_obj[i]) + ': \n')
    txt = txt.replace(keyword_obj[i].strip(), input_txt, 1)
textObj.close()

# Re-write to the mad_lib.py
textObj = open('mad_lib.txt', 'w')
textObj.write(txt)
textObj.close()

# Print out to check the file content
txt_file = open('mad_lib.txt')
content = txt_file.read()
print(f'After replacement text -> {content}')
txt_file.close()