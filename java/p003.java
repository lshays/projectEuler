import java.util.ArrayList;
import java.util.Collections;

public class p003{
    
    public int getNextPrime(int num){
        while(true){
            boolean composite = false;
            for(int i = 2; i < num; i++){
                if(num % i == 0){
                    composite = true;
                    break;
                }
            }
            if(!composite){
                return num;
            }
            num += 1;
        }
    }

    public ArrayList<Integer> primeFactors(long num){
        ArrayList<Integer> factors = new ArrayList<Integer>();
        if(num == 1){
            return factors;
        }
        int prime = getNextPrime(2);
        while(num % prime != 0){
            prime = getNextPrime(prime + 1);
        }
        factors.add(prime);
        factors.addAll(primeFactors(num/prime));
        return factors; 
    }

    public static void main(String args[]){
        long num = 600851475143L;
        p003 myInstance = new p003();
        ArrayList<Integer> primes = myInstance.primeFactors(num); 
        System.out.println(primes);
        System.out.println(Collections.max(primes));
    }
}
