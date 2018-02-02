package utils;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class primeGen{

    public static int currentNum = 2;
    public static Map<Integer, ArrayList<Integer>> composites = new HashMap<Integer, ArrayList<Integer>>();

    public static int getNextPrime(){
        while(true){
            if(!composites.containsKey(currentNum)){
                // currentNum is prime
                ArrayList<Integer> factors = new ArrayList<Integer>();
                factors.add(currentNum);
                composites.put(currentNum*currentNum, factors); 
                currentNum++;
                return currentNum-1; 
            }
            else{
                // currentNum is composite
                for(int num : composites.get(currentNum)){
                    ArrayList<Integer> temp = new ArrayList<Integer>(); 
                    temp = composites.getOrDefault(currentNum+num, temp);
                    temp.add(num);
                    composites.put(currentNum+num, temp);
                } 
                composites.remove(currentNum);
                currentNum += 1; 
            }
        }
    }   
}
