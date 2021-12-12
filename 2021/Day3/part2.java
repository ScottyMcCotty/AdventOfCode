
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
        // String gamma = "";
        // String epsilon = "";

        // for (int ii = 0; ii < data.get(0).length(); ++ii)
        // {
        //     int count = 0;

        //     for (int jj = 0; jj < data.size(); ++jj)
        //     {
        //         count += Integer.parseInt(Character.toString(data.get(jj).charAt(ii)));
        //     }

        //     if (count >= data.size() / 2)
        //     {
        //         gamma += "1";
        //         epsilon += "0";
        //     }
        //     else
        //     {
        //         gamma += "0";
        //         epsilon += "1";
        //     }
        // }

        // System.out.println(gamma);
        // System.out.println(epsilon);

        // System.out.println(Integer.parseInt(gamma, 2) * Integer.parseInt(epsilon, 2));

        ArrayList<String> data2 = (ArrayList<String>) data.clone();

        int position = 0;

        while (data.size() > 1)
        {
            // System.out.println(data);

            int common = getMostCommon(data, position);

            remove(data, position, common);

            position++;
        }

        position = 0;

        while (data2.size() > 1)
        {
            // System.out.println(data2);

            int common = getLeastCommon(data2, position);

            remove(data2, position, common);

            position++;
        }

        System.out.println(data);
        System.out.println(data2);

        System.out.println(Integer.parseInt(data.get(0), 2) * Integer.parseInt(data2.get(0), 2));
    }

    public static int getMostCommon(ArrayList<String> data, int position)
    {
        int sum = 0;

        for (int ii = 0; ii < data.size(); ++ii)
        {
            sum += Integer.parseInt(Character.toString(data.get(ii).charAt(position)));
        }

        // System.out.println(sum);
        // System.out.println(data.size() / 2);

        if (sum * 2 >= data.size())
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }

    public static int getLeastCommon(ArrayList<String> data, int position)
    {
        int sum = 0;

        for (int ii = 0; ii < data.size(); ++ii)
        {
            sum += Integer.parseInt(Character.toString(data.get(ii).charAt(position)));
        }

        // System.out.println(sum * 2);
        // System.out.println(data.size());

        if (sum * 2 >= data.size())
        {
            return 0;
        }
        else
        {
            return 1;
        }
    }

    public static void remove(ArrayList<String> data, int position, int value)
    {


        for (int ii = data.size() - 1; ii >= 0; --ii)
        {
            if (Integer.parseInt(Character.toString(data.get(ii).charAt(position))) != value)
            {
                // remove this entry
                data.remove(ii);
            }
        }
    }
}