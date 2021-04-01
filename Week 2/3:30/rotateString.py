def rotateString(A, B):
#set up a loop that runs the length of A
#Remove the first letter and add to the end
#compare to see if its same as B
#if same, true
#outside loop return False
  if A == "" and B == "":
    return True
  C = A
  for item in range(len(A)):
    C = C + A[item]
    C = C [1:len(C)]
    if C == B:
      return True
  return False
        
print(rotateString('abcde','cdeab'))