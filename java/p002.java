public class p002{

    static int[] nums = new int[]{1,1};

    static void updateNums(int newNum){
        nums = new int[]{nums[1], newNum};
    }

    static int nextNum = 0;

    public static void main(String args[]){
        int sum = 0;
        while(nextNum < 4000000){
            nextNum = nums[0] + nums[1];
            updateNums(nextNum);
            if(nextNum % 2 == 0){
                sum += nextNum;
            }
        }
        System.out.println(sum);
    }
}
