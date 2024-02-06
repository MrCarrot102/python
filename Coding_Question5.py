class solution:
    def lenghOfLastWord(self, s:str)->int:
        n = len(s)
        i = n -1 
        while s[i] == ' ': i -= 1
        
        letter_count = 0
        for i in range(i+1):
            if s[i] != ' ':
                letter_count += 1 
            else:
                letter_count = 0
        
        return letter_count