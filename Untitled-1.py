char_count = {}
name =  "aabcd"    
for c in name:
   if not c in char_count:
      char_count[c] = 0
   else:
      char_count[c] += 1
print(char_count)