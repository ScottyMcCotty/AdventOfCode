
public class MyMath
{
    public static int moveTowards(int current, int target, int change)
    {
        if (current < target)
        {
            return current + change;
        }
        else
        {
            return current - change;
        }
    }
}