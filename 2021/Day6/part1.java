
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;

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

        ArrayList<Integer> fish = new ArrayList<Integer>();

        for (String content : contents)
        {
            fish.add(Integer.parseInt(content));
        }

        int days = 80;

        while (days > 0)
        {
            // System.out.println(fish);
    
            int size = fish.size();

            for (int ii = 0; ii < size; ++ii)
            {
                if (fish.get(ii) == 0)
                {
                    fish.add(8);
                    fish.set(ii, 6);
                }
                else
                {
                    fish.set(ii, fish.get(ii)-1);
                }
            }

            days--;
        }

        // System.out.println("\n");
        // System.out.println(fish);
        System.out.println(fish.size());
    }
}