def lengthOfLastWord(s):
  if s[0] == " " and len(s) == 1:
    return 0
  if s[0] == " " and s[len(s)-1] == " ":
    return 0
  if s[0] != " " and len(s) == 2:
    return 1

  counter = 0
  for l in s:
    if l == " ":
      counter = 0
    else:
      counter += 1
  return counter
  


input = " a"
print(lengthOfLastWord(input))
