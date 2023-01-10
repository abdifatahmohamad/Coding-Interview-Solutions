def lengthOfLastWord(s) -> int:
  length = 0
  for i in range(len(s)-1,-1,-1):
      if s[i] == " " and length:
          return length
      elif s[i] != " ":
          length += 1
  return length
