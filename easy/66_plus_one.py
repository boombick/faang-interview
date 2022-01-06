# https://leetcode.com/problems/plus-one/

def plusOne(digits: list[int]) -> list[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            if carry == 0:
                break
            n = digits[i] + carry
            carry = n//10
            n = n%10
            
            digits[i] = n
            
        if carry == 1:
            digits.insert(0,1)
            
        print(digits)
        

plusOne([2, 9, 9])