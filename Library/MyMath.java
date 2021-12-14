
public class MyMath
{
    /**
     * Moves the current value towards the target by the desired change amount
     * <p>
     * It's possible for the resulting value to be further from the target than it was already,
     * in the case where change is greater than the difference between current and target.
     * 
     * @param current   The current value
     * @param target    The target value
     * @param change    The amount to change the current value
     * @return          The adjusted value
     */
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