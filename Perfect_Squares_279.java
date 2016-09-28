public class Solution {
    
    private String __author__ = "tangjialiang" ;
    private String __V__ = "success_V" ;
    private String __tips__ = "dp"
    
    public int numSquares(int n) {
        int[] dp = new int[n+1] ;
        dp[1] = 1 ;
        
        for(int i=2; i<=n; i++) {
            
            int min_num = Integer.MAX_VALUE ;
            
            int j = 1 ;
            while(j*j <= i) {
                min_num = Math.min(min_num, dp[i - j*j]+1) ;
                j++ ;
            }
            dp[i] = min_num ;
        }
        
        return dp[n] ;
        
    }
}
