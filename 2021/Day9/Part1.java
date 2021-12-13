
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

        for (int ii = 0; ii < data.size(); ++ii)
        {
            for (int jj = 0; jj < data.get(ii).length(); ++jj)
            {
                if (isSmallest(data, ii, jj))
                {
                    // System.out.println("It's a minimum!");

                    count += 1 + Integer.parseInt(Character.toString(data.get(ii).charAt(jj)));

                    System.out.format("%c is a minima at %d %d\n", data.get(ii).charAt(jj), ii, jj);
                }
            }
        }

        System.out.format("count: %d\n", count);
    }

    public static boolean isSmallest(ArrayList<String> data, int ii, int jj)
    {
        // System.out.format("ii = %d, jj = %d\n", ii, jj);
        // System.out.format("max x = %d, max y = %d\n", data.get(0).length(), data.size());

        int val = Integer.parseInt(Character.toString(data.get(ii).charAt(jj)));

        for (int dx = -1; dx <= 1; ++dx)
        {
            for (int dy = -1; dy <= 1; ++dy)
            {
                if (dx == 0 && dy == 0) continue;
                if (dx * dy != 0) continue;

                int x = jj + dx;
                int y = ii + dy;

                if (x < 0 || x >= data.get(0).length()) continue;
                if (y < 0 || y >= data.size()) continue;

                // System.out.format("%d, %d\n", x, y);
                // System.out.format("comparing %c and %d\n", data.get(y).charAt(x), val);

                if (Integer.parseInt(Character.toString(data.get(y).charAt(x))) <= val)
                {
                    // System.out.format("position %d %d isn't a minimum\n", ii, jj);
                    return false;
                }
            }
        }


        return true;
    }
}