public class p006{
    public static void main(String[] args){
        long sumOfsquares = 0;
        long squareOfSums = 0;
        for(int i = 1; i <= 100; i++){
            sumOfsquares += i*i;
            squareOfSums += i;
        }
        squareOfSums = squareOfSums * squareOfSums;
        System.out.println(squareOfSums + " - " + sumOfsquares + " = " + (squareOfSums-sumOfsquares));
    }
}
