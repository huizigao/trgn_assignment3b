import re
with open('/home/huizigao/assignments/trgn_assignment3b/scripts/mytextfile.txt') as f:
    content = f.read()
    for number in re.findall(r"[+]{0,1}[0-9]{2,3}[-][0-9]{2,4}[-][0-9]*[-]{0,1}[0-9]*", content):
        # for number in ("num1", "num2"):
        #       1st: number -> num1
        #       2nd: number -> nums
        alist= re.split("-", number)
        stringA = "("+alist[-3]+")"+alist[-2]+alist[-1]

        if alist[0][0] == "+":
            stringA = alist[0]+stringA

        # g[0]
        # alist[0] = "+44"
        # string[0] -> first character
        # list[0]  
        # 
        # 
        # 
        # 
        # alist[1]
        # (425)      922        5683 -> if has "+"?
        print(stringA)
        #   1. split by '-'
        #   2. str.join() -> 44-20-7183-8750

    

        

 


  
     
