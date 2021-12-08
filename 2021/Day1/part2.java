
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;

public class part2
{

    public static void main(String argv[]) throws Exception
    {
        if (argv.length == 0)
        {
            System.err.println("I need a file! Or use \"-s\" for stdin");
            
            return;
        }

        ArrayList<Integer> contents = readAllContents(argv[0]);

        solve(contents);
    }

    public static ArrayList<Integer> readAllContents(String filename) throws Exception
    {
        ArrayList<Integer> contents = new ArrayList<>();

        if (filename.equals("-s"))
        {
            // use stdin somehow
            throw new Exception("Whoops, reading from stdin isn't actually supported yet");
        }
        else
        {
            // use the filename
            try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
                String line;
                while ((line = br.readLine()) != null) {
                   // process the line by just converting to integer and pushing into arraylist
                   contents.add(Integer.valueOf(line));
                }
            }
        }

        return contents;
    }

    public static void solve(ArrayList<Integer> data)
    {
        int count = 0;
        int previous1 = Integer.MAX_VALUE / 10;
        int previous2 = Integer.MAX_VALUE / 10;
        int previous3 = Integer.MAX_VALUE / 10;

        for (int depth : data)
        {
            // if (depth > previous) ++count;

            if (depth + previous1 + previous2 > previous1 + previous2 + previous3) ++count;

            previous3 = previous2;
            previous2 = previous1;
            previous1 = depth;
        }

        System.out.println(count);
    }
}