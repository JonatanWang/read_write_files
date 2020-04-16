"""
A program that opens all .txt files in a folder
and searches for any line that matches a user-supplied
regular expression, and print to the screen.
"""
import os, glob, re, pyinputplus as pyip

current_folder = os.getcwd()
os.chdir(current_folder)
for file in glob.glob("*.txt"):
    txt_obj = open(file, 'r')
    txt = txt_obj.read()
    user_supplied_regex_pattern = pyip.inputRegexStr(prompt=f'For file {file}: input the search regex pattern: ')
    regex = re.compile(user_supplied_regex_pattern)
    search_result = regex.findall(txt)

    # Print out result
    if search_result is not None:
        print(f"In file {file}: Found match(es): ")
        for i in range(len(search_result)):
            print(search_result[i] + " ")
    else:
        print("Not match found.")
    txt_obj.close()