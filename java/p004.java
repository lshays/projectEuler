public class p004{
    
    public boolean isPalindrome(int num){
        String forward = Integer.toString(num);
        String backward = new StringBuilder(forward).reverse().toString();
        return forward.equals(backward);
    }

    public static void main(String[] args){
        p004 myInstance = new p004();
        int answer = 0;
        for(int a = 100; a < 1000; a++){
            for(int b = 100; b < 1000; b++){
                int temp = a*b;
                if(myInstance.isPalindrome(a*b)){
                    if(a*b > answer){
                        answer = a*b;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
