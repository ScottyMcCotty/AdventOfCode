
public class ScottClass
{
    private static String[] joke_lines = {"Knock knock", "Who's there?", "Banana", "Banana who?"};
    private static int joke_index = 0;

    public static void joke()
    {
        System.out.println(joke_lines[joke_index++ % joke_lines.length]);
    }
}