text="python is awesome"
word= text.split()
print("Words:", word)

# string Sprit

text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

# Substring
text = "python is dynamically typed language"
substring="is"
if substring in text:
    print(substring, "found in the text")
  
