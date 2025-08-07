def testNumbers(n):
    result=[]
    if n > 0 :
#   result.append("The given number is postive: ", n) 
     result.append(f"The given number is positive: {n}")
  
    elif n==0 :
       
        result.append(f"The given number is Zero: {n}")
    else:
        result.append(f"The given number is negative: {n}")
        

    if n!=0: 
        if   n%2==0:
         result.append(f"Even: {n}")
        else:
         result.append(f"Odd: {n}")
    return result     
test_cases = [
    (10, ["The given number is positive: 10", "Even: 10"]),
    (-3, ["The given number is negative: -3", "Odd: -3"]),
    (0, ["The given number is Zero: 0"]),
    (7, ["The given number is positive: 7", "Odd: 7"]),
    (-6, ["The given number is negative: -6", "Even: -6"])
]
for i,(inp,expected) in enumerate(test_cases):
   output=testNumbers(inp)
   result="pass" if output== expected else f"fail : {output}"
   print(f"test {i+1}:input={inp} | expected={expected}->{result}")
