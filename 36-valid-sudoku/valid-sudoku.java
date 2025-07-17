class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character>[] row = new HashSet[9];
        HashSet<Character>[] col = new HashSet[9];
        HashSet<Character>[] box = new HashSet[9];

        for(int i=0; i<9;i++){
            row[i] = new HashSet<>();
            col[i] = new HashSet<>();
            box[i] = new HashSet<>();
        }

        for(int i=0; i<9;i++){
            for(int j=0; j<9; j++){
                char n = board[i][j];


                if(n == '.'){
                    continue;
                }
                if(row[i].contains(n)){
                    return false;
                }else{
                    row[i].add(n);}

                if(col[j].contains(n)){
                    return false;
                }else{
                col[j].add(n);}

                int bind = (i/3)*3+(j/3);
                if(box[bind].contains(n)){
                    return false;
                }else{
                box[bind].add(n);}
            }
        }
        return true;
    }
}