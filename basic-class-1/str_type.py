# Strings of class str are created with quotes

print ('sample quote_1, quote_2\n')
quote_1 = 'single quoted'
quote_2 = "double quoted"
print (quote_1, quote_2)

print ('\nsample why_1, why_2')
why_1 = 'She said, "Hello!"'
why_2 = "It's mine!"
print (why_1, why_2)

print ('\nsample why_not_1, why_not_2')
why_not_1 = "She said, \"Hello!\""
why_not_2 = 'It\'s mine!'
print (why_not_1, why_not_2)

# Special escape sequences exists
print ('\nSpecial escape sequences\n')
print ('new line sample')
new_line = 'line1\nline2\nline3\n'
print (new_line)
print ('new TAB sample')
tab_char = 'col1\tcol2\tcol3\t\n'
print (tab_char)
print ('backslash escaping')
backslash = 'the backslash: \\'
print (backslash)

# Raw strings prevent escape sequences interpretation
print ('\nRaw strings\n')
print ('new line sample')
raw_new_line = r'line1\nline2\nline3\n'
print (raw_new_line)
print ('new TAB sample')
raw_tab_char = r'col1\tcol2\tcol3\t\n'
print (raw_tab_char)
print ('backslash escaping')
raw_backslash = r'the backslash: \\'
print (raw_backslash)
print ('\n')

# Sequence objects can use several operators and functions:
print ('Sequence objects can use operators and functions\n')
sub_text = 'double'
print ('sub_text =', sub_text)
print (sub_text + sub_text)  #concatinate
print ('__' *40)             # repetition
print ('len(sub_text) returns', len(sub_text))
print ('min(sub_text) returns', min(sub_text))
print ('max(sub_text) returns', max(sub_text))
print ('sub_text not in quote_1 returns', sub_text not in quote_1)
print ('sub_text in quote_2 returns', sub_text in quote_2)


# String objects have many available methods like:
print ('why_1.count("e") returns', why_1.count('e'))
print ('why_1.index("e") returns', why_1.index('e'))
       # zero based indexing! e is on position three , index returns 2
print ('why_1.index("e", 3, 18) returns', why_1.index('e', 3, 18))
       # search at a particular starting position, 3 till 18
print ('why_1.find("x") returns', why_1.find('X'))
       # returns -1 if  not found. takes the complete string
print ('why_1.startswith("She")  returns', why_1.startswith("She"))
print ('why_1.endswith("!\\"")  returns', why_1.endswith("!\""))
print ('why_1.upper() returns', why_1.upper())
print ('why_1.lower() returns', why_1.lower())
csv = 'a,b,c'
print('csv.split(",") returns', csv.split(","))
print ('",".join(["a", "b", "c"]) returns', ",".join(["a", "b", "c"]))
print ('sub_text.isalpha() returns', sub_text.isalpha())
print ('sub_text.isdigit() returns', sub_text.isdigit())
