string=input("enter the string: ")
first=string[0]
mode_str=first+string[1:].replace(first,"$")
print("modified string=",mode_str)
