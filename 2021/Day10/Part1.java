
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

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
        int score = 0;

        for (int ii = data.size() - 1; ii >= 0; --ii)
        {
            String line = data.get(ii);
            
            Stack<Character> chunks = new Stack<Character>();

            for (int jj = 0; jj < line.length(); ++jj)
            {
                char ch = line.charAt(jj);

                if (ch == '(' || ch == '[' || ch == '{' || ch == '<')
                {
                    chunks.push(ch);
                }
                else if (ch == ')')
                {
                    if (chunks.pop() != '(')
                    {
                        data.remove(ii);
                        score += 3;
                        continue;
                    }
                }
                else if (ch == ']')
                {
                    if (chunks.pop() != '[')
                    {
                        data.remove(ii);
                        score += 57;
                        continue;
                    }
                }
                else if (ch == '}')
                {
                    if (chunks.pop() != '{')
                    {
                        data.remove(ii);
                        score += 1197;
                        continue;
                    }
                }
                else if (ch == '>')
                {
                    if (chunks.pop() != '<')
                    {
                        data.remove(ii);
                        score += 25137;
                        continue;
                    }
                }
                else
                {
                    System.out.format("WTF is %c??\n", ch);
                }
            }
        }

        System.out.format("Score: %d\n", score);
    }
}