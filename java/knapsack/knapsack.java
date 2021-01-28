import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.PrintWriter;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.StringTokenizer;

// If it exceeds time limit, try again
// Worked on the 4th try with no optimizations

public class knapsack {

    public static void main(String[] commandLineArguments) throws Exception 
    {
        BufferedReader myInputReader = 
            new BufferedReader(new InputStreamReader(System.in));
        PrintWriter myOutputWriter = 
            new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String aLine;
        while ((aLine = myInputReader.readLine()) != null) 
        {
            StringTokenizer myTokenizer = new StringTokenizer(aLine);
            int currentInteger = Integer.parseInt(myTokenizer.nextToken());
            int numberOfItems = Integer.parseInt(myTokenizer.nextToken());
            int[] weight = new int[numberOfItems];
            int[] value = new int[numberOfItems];
            for (int idx = 0; idx < numberOfItems; idx++) 
            {
                myTokenizer = new StringTokenizer(myInputReader.readLine());
                value[idx] = Integer.parseInt(myTokenizer.nextToken());
                weight[idx] = Integer.parseInt(myTokenizer.nextToken());
            }
            int[][] arrayItems = new int[numberOfItems + 1][currentInteger + 1];
            for (int idx = 0; idx < arrayItems.length; idx++) Arrays.fill(arrayItems[idx], -1);
            for (int idx = 0; idx <= numberOfItems; idx++) {
                for (int thisItem = 0; thisItem <= currentInteger; thisItem++) 
                {
                    if (idx == 0 || thisItem == 0) arrayItems[idx][thisItem] = 0;
                    else if (weight[idx - 1] <= thisItem) 
                    {
                        arrayItems[idx][thisItem] = 
                            (arrayItems[idx - 1][thisItem] > 
                            value[idx - 1] + arrayItems[idx - 1][thisItem - weight[idx - 1]]) ? 
                            arrayItems[idx - 1][thisItem] : value[idx - 1] + arrayItems[idx - 1][thisItem - weight[idx - 1]];
                    }
                    else arrayItems[idx][thisItem] = arrayItems[idx - 1][thisItem];
                }
            }
            int current = currentInteger;
            ArrayList<Integer> indices = new ArrayList<Integer>();
            for (int idx = numberOfItems; idx > 0; idx--) {
                if(arrayItems[idx][current] != arrayItems[idx - 1][current]) {
                    indices.add(idx - 1);
                    current -= weight[idx - 1];
                }
            }
            myOutputWriter.println(indices.size());
            for(int idx : indices) myOutputWriter.print(idx + " ");
            myOutputWriter.println();
        }
        myOutputWriter.close();
    }
}