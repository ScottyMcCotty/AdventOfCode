
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;
import java.util.List;
import java.lang.Math;

public class part2
{

    public static void main(String argv[]) throws Exception
    {
        String file = "input.in";

        if (argv.length == 0)
        {
            System.err.println("Using default file \"input.in\"");
        }
        else
        {
            file = argv[0];
        }

        ArrayList<String> contents = readAllContents(file);

        solve(contents);
    }

    public static ArrayList<String> readAllContents(String filename) throws Exception
    {
        ArrayList<String> contents = new ArrayList<>();

        if (filename.equals("-s"))
        {
            // use stdin somehow
            throw new Exception("Whoops, reading from stdin isn't supported yet");
        }
        else
        {
            // use the filename
            try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
                String line;
                while ((line = br.readLine()) != null) {
                   // process the line by just converting to integer and pushing into arraylist
                   contents.add(line);
                }
            }
        }

        return contents;
    }

    public static void solve(ArrayList<String> data)
    {
        String[] contents = data.get(0).split(",", 0);

        ArrayList<Integer> crabs = new ArrayList<Integer>();

        for (String content : contents)
        {
            crabs.add(Integer.parseInt(content));
        }

        // Collections.sort(crabs);

        // System.out.println(crabs);

        // ArrayList<Integer> costs = new ArrayList<Integer>(2000);
        Integer[] zeros = new Integer[2000];
        Arrays.fill(zeros,new Integer(0));
        List<Integer> costs = Arrays.asList(zeros);

        for (int crab : crabs)
        {
            for (int ii = 0; ii < costs.size(); ++ii)
            {
                costs.set(ii, costs.get(ii) + getCost(Math.abs(ii - crab)));
            }
        }

        System.out.println(costs);

        int index = 0;
        int value = Integer.MAX_VALUE;

        for (int ii = 0; ii < costs.size(); ++ii)
        {
            if (costs.get(ii) < value)
            {
                index = ii;
                value = costs.get(ii);
            }
        }

        System.out.println(index);
        System.out.println(value);

        // System.out.println(getCost(11));
        // System.out.println(getCost(4));
        // System.out.println(getCost(1));

        // int avg = crabs.get(crabs.size() / 2);

        // System.out.println(avg);

        // int sum = 0;

        // for (Integer val : crabs)
        // {
        //     sum += Math.abs(val - avg);
        // }

        // System.out.println(sum);

        // System.out.println(crabs.size());
        
        // System.out.println(sum / crabs.size());
    }

    public static int getCost(int distance)
    {
        int cost = 0;
        while (distance > 0)
        {
            cost += distance;
            distance--;
        }

        return cost;
    }
}