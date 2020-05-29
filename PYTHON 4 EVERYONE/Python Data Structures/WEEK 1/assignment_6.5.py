"""
    6.5 Write code using find() and string slicing(see section 6.10)
    to extract the number at the end of the line below.
    Convert the extracted value to a floating point number and print it out.
"""
text = "X-DSPAM-Confidence: 0.8475"

# Use the find method to locate the position of a character and extract the number by string slicing
text_pos = text.find(':')

# the string number is converted to float and printed out
numb_extract = float(text[text_pos+2:])
print(numb_extract)
