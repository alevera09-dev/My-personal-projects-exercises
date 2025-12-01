class RomanToInt(object):
    def __init__(self, number: int):
        self.number = number
        
    def roman_to_int(self):
        i = "I"
        v = "V"
       # x = "X"
       # l = "L"
       # c = "C"
        
        roman_number:str = ""
        
        
        for number in range(1, self.number+1):
            if number >= 1 and number <= 3:
                roman_number = roman_number + i
            
            if number == 4:
                roman_number = "IV"
                
                
            if number == 5:
                roman_number = v
            
            if number > 5 and number <= 8:
                roman_number = roman_number + i
                
            if number == 9:
                roman_number = "IX"
            
            if number == 10:
                roman_number = "X"        
        
        
        return roman_number                  
    
          
convert_roman = RomanToInt(11)

print(convert_roman.roman_to_int())                 