class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        if (s.isEmpty()) {
            return false;
        }
        
        int n = s.length();
        boolean[] dp = new boolean[n + 1];  // dp[i] = can s[0..i-1] be segmented?
        dp[0] = true; // empty string is always valid
        
        // Put words in a HashSet for O(1) lookup
        java.util.Set<String> wordSet = new java.util.HashSet<>(wordDict);
        
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;  // no need to check further splits for this i
                }
            }
        }
        
        return dp[n];
    }
}
