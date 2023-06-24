
First element to occur k times

#User function Template for python3


class Solution:
    def firstElementKTime(self,  arr, n, k):
        # code here
        
        i = 0
        
        hashmap = {}
        
        while i != n:
            
            if arr[i] in  hashmap:
                hashmap[arr[i]] = hashmap[arr[i]] + 1
                
                if hashmap[arr[i]] == k:
                    return arr[i]
                
                #print(hashmap)
            else:
                
                hashmap[arr[i]] = 1
                
                if k == 1:
                    return arr[i]
            
            i = i + 1
        
        return -1 
            
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
