
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Part1
{

    public static void main(String argv[]) throws Exception
    {
        String file = "input.txt";

        if (argv.length == 0)
        {
            System.err.println("Using default file \"" + file + "\"");
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

        int count = 0;

        for (String line : data)
        {
            // ArrayList<String> output = Arrays.asList(line.split(" | ", 0)[1].split(" ", 0));
            // System.out.println(line);

            String[] splits = line.split(" \\| ", 0);
            
            // System.out.println(splits[0]);
            // System.out.println(splits[1]);
            // System.out.println(splits[1]);

            String[] output = splits[1].split(" ", 0);

            // System.out.println(output[0]);

            for (String str : output)
            {
                System.out.println("'" + str + "'");

                if (str.length() == 2 || str.length() == 3 || str.length() == 4 || str.length() == 7)
                {
                    ++count;
                    System.out.println("++count");
                }

            }
        }

        System.out.println(count);
    }
}