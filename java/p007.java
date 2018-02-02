import utils.primeGen;

public class p007{

    public static void main(String[] args){
        for(int i=0; i<10000; i++){
            primeGen.getNextPrime();
        }
        System.out.println(primeGen.getNextPrime());
    }

}
