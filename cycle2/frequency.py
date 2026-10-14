input_str=input("enter the string: ")
char_frequency={}
for char in input_str:
   char_frequency[char]=char_frequency.get(char,0)+1
print(f"character string in '{input_str}':")
for char,count in char_frequency.items():
   print(f"{char} occurs {count} times.")
