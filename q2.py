name = input("Larry: What's ye name, Hunter?\n")
is_valid_length = False
is_valid_start = False
is_one_word = False
is_valid_name = False

# length of name
if 1 <= len(name) <= 9:
  is_valid_length = True
else:
  is_valid_length = False

# check if first index is an alphabet
if name[0].isalpha():
  is_valid_start = True
else:
  is_valid_start = False

# if name is one word
if len(name.split(" ")) == 1:
  is_one_word = True
else:
  is_one_word = False

if is_valid_length and is_valid_start and is_one_word:
  is_valid_name = True
else:
  is_valid_name = False

if is_valid_name == True:
  print(f"Larry: Is '{name}' a name I can pronounce?")
  print(f'It has a length of {len(name)} which is between 1 to 9 characters? {is_valid_length}!')
  print(f'It starts with an alphabet? {is_valid_start}')
  print(f'It is a single word? {is_one_word}')
  print(f'Larry: I can pronounce this name --- {is_valid_name}')
elif is_valid_name == False:
  print(f"Larry: Is '{name}' a name I can pronounce?")
  print(f'It has a length of {len(name)} which is between 1 to 9 characters? {is_valid_length}!')
  print(f'It starts with an alphabet? {is_valid_start}')
  print(f'It is a single word? {is_one_word}')
  print(f'Larry: I can pronounce this name --- {is_valid_name}')