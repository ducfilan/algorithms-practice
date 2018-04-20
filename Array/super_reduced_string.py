# Steve has a string, , consisting of  lowercase English alphabetic letters. 
# In one operation, he can delete any pair of adjacent letters with same value. For example, string "aabcc" would become either "aab" or "bcc" after  operation.
#
# Steve wants to reduce  as much as possible. 
# To do this, he will repeat the above operation as many times as it can be performed. 
# Help Steve out by finding and printing 's non-reducible form!
#
# Note: If the final string is empty, print Empty String .


def super_reduced_string(s, prev_len=''):
  output = ''
  base_char = s[0]
  count_char = 1
  
  for c in s[1:] + ' ':
    if c == base_char:
      count_char = count_char + 1
    else:
      if count_char % 2:
        output = output + base_char
      
      count_char = 1
      base_char = c
        
  if not output:
    return 'Empty String'

  return output if len(output) == prev_len else super_reduced_string(output, len(output))
