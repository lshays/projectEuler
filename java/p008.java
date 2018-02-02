import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;

public class p008{
    public static void main(String[] args){
        File file = new File("p008.txt");
        ArrayList<Integer> intarray = new ArrayList<Integer>(); 
        try{
            BufferedReader reader = new BufferedReader(new FileReader(file));
            Integer y = null;
            while((y = reader.read()) != -1){
                y = Character.getNumericValue(y);
                if(y >= 0){
                    intarray.add(y);
                }
            }
            long answer = 0;
            for(int end = 13; end <= 1000; end++){
                int start = end-13;
                ArrayList<Integer> temp = new ArrayList<Integer>(intarray.subList(start, end));
                long product = 1;
                for(int x : temp){
                    product*=x;
                }
                if(product > answer){
                    answer = product;
                }
            }
            System.out.println(answer);
        }
        catch(Exception e){
            System.out.println("Error: " + e.getMessage());    
        }

    }
}
