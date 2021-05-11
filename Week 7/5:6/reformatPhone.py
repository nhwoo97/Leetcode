class Solution:
    def reformatNumber(number):
        number = number.replace(' ','')
        number = number.replace('-','')
        number =list(number)
        ans = []

        l = len(number)
    
        while l > 4:
            ans.append(number[0:3])
            del number[0:3]
            l = len(number)

        
        if l == 3:
            ans.append(number)
            tempArr = []
            for a in ans:
                temp = ''.join(a)
                tempArr.append(temp)
            return '-'.join(tempArr)
        
        elif l == 4:
            temp1 = number[0:2]  
            temp2 = number[2:4]
            ans.append(temp1)
            ans.append(temp2)
            tempArr = []
            for a in ans:
                temp = ''.join(a)
                tempArr.append(temp)
            return '-'.join(tempArr)
        elif l == 2:
            ans.append(number)
            tempArr = []
            for a in ans:
                temp = ''.join(a)
                tempArr.append(temp)
            return '-'.join(tempArr)
            
    
    
    
    
    input = '123 4-5678'
    print(reformatNumber(input))