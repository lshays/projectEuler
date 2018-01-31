public class p005{
    static int[] divisors = new int[]{20, 19, 18, 17, 16, 15, 14, 13, 12, 11};
    public static void main(String[] args){
        int answer = 20;
        boolean found = false;
        while(!found){
            answer += 20;
            found = true;
            for(int x : divisors){
                if(answer % x != 0){
                    found = false;
                }
            }
        }
        System.out.println(answer);
    }
}
