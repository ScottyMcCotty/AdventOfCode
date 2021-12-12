
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.lang.Math;

public class part1
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

        Collections.sort(crabs);

        System.out.println(crabs);

        int avg = crabs.get(crabs.size() / 2);

        System.out.println(avg);

        int sum = 0;

        for (Integer val : crabs)
        {
            sum += Math.abs(val - avg);
        }

        System.out.println(sum);

        // System.out.println(crabs.size());
        
        // System.out.println(sum / crabs.size());
    }
}