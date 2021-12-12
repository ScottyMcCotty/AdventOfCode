
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
        int x = 0;
        int depth = 0;
        int aim = 0;

        for (int ii = 0; ii < data.size(); ++ii)
        {
            String[] commands = data.get(ii).split(" ", 0);

            if (commands[0].equals("forward"))
            {
                x += Integer.parseInt(commands[1]);
                depth += aim * Integer.parseInt(commands[1]);
            }
            else if (commands[0].equals("down"))
            {
                aim += Integer.parseInt(commands[1]);
            }
            else if (commands[0].equals("up"))
            {
                aim -= Integer.parseInt(commands[1]);
            }
            else
            {
                System.out.println("Help! I don't know this command: " + commands[0]);
            }
        }

        System.out.println(x * depth);
    }
}