class solution:
    def trap( self, height:list[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        for i in range(n):
            j = -i - 1
            max_left[i] = l_wall
            max_right[j]= r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
            
        ans = [0] * n 
        for i in range(n):
            potential = min(max_left[i], max_right[i])
            ans[i] = max(0, potential-height[i])
        
        return sum(ans)
            
        