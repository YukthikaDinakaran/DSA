class Solution {
    public boolean isMatch(String s, String p) {
        int n= s.length();
        int m = p.length();
        boolean[][] l = new boolean[n+1][m+1];
        l[0][0]= true;
        
        char[] chars = s.toCharArray();
        char[] pc = p.toCharArray();
        for(int j= 1;j<m+1;j++){
            if(pc[j-1]=='*'){
                l[0][j]= l[0][j-1];
            }
        }
        for(int i=1;i<n+1;i++){
            for( int j=1 ;j<m+1;j++){
                if (pc[j - 1] == chars[i - 1] || pc[j - 1] == '?'){
                    l[i][j] = l[i-1][j-1];
                }
                else if( pc[j-1]== '*'){
                        l[i][j]= l[i][j-1] || l[i-1][j];
                    }
                }

            }

          return l[n][m];  
        }
      
    }
