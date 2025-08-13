class Solution {
    public int minAddToMakeValid(String s) {
        int n = s.length();
        int ans = 0;
        int bal = 0;
        for(int i=0; i<n;i++){
            char ch = s.charAt(i);
            if(ch == '('){
                bal = bal+1;
            }
            else{
                bal = bal-1;
            }
            if(bal == -1){
            
            ans = ans+1;
            bal = bal +1;
        }
        
        }
        
        return ans+bal;   
    }
}