import pyperclip
string1,string2 = input("Enter replacer first then the replacee seperated by a space: ").split()
text = pyperclip.paste()
pyperclip.copy(text.replace(string1,string2))
print("Done >> Copied to clipboard")
