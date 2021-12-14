
import java.util.ArrayList;

//  TO RUN THIS GUY:
//
//  $ make
//  $ java BoardWithGenericsExample

public class BoardWithGenericsExample
{
    //  An example class we'll store in our board.
    public static class Pet {
        boolean isZombie = false;
        @Override
        public String toString() {
            return isZombie ? "Z" : ".";
        }
    }

    //  optional shorthand if "BoardWithGenerics<Pet>" is too long
    public static class Yard extends BoardWithGenerics<Pet>
    {
        public Yard(int numRows, int numCols, Pet fill)
        {
            super(numRows, numCols, fill);
        }
    }

    //  One way to implement one of those interfaces is with a normal class,
    //  which we'll instantiate later...
    public static class IsNeighborAZombie implements BoardWithGenerics.PositionalConditional<Pet>
    {
        @Override
        public boolean matches(BoardWithGenerics<Pet> board, int row, int col)
        {
            //  this assumes all cells are non-null...
            if ((row > 0) && (board.get(row - 1, col).isZombie)) return true;
            if ((row < (board.getNumRows() - 1)) && (board.get(row + 1, col).isZombie)) return true;
            if ((col > 0) && (board.get(row, col - 1).isZombie)) return true;
            if ((col < (board.getNumCols() - 1)) && (board.get(row, col + 1).isZombie)) return true;
            return false;
        }
    }

    //  Another way to implement one of those interfaces is with an anonymous
    //  inner class... this creates an object named "zombify" which is a
    //  BoardFiddler for Pets.  (I like this way; I use it all the time for
    //  java.util.Comparator<> implementations for sorting.)
    public static final BoardWithGenerics.BoardFiddler<Pet> zombify = new BoardWithGenerics.BoardFiddler<Pet>() {
        @Override
        public void fiddleBoard(BoardWithGenerics<Pet> board, int row, int col)
        {
            board.get(row, col).isZombie = true;
        }
    };

    //  A third way is with a lambda expression; see later.

    public static void main(String[] argv)
    {
        //  Passing new Pet() as the initializer here means each element in the
        //  board is a reference to the same instance, which is probably not
        //  what we want!
        Yard yard = new Yard(5, 5, null);
        //  So instead let's initialize the yard with a new, different Pet in
        //  each cell.  This one uses a lambda expression, which I think is the
        //  hardest to read & understand, so see the lambda examples later.
        yard.forEach((b, r, c) -> b.set(r, c, new Pet()));

        yard.get(2, 2).isZombie = true;  //  uh oh
        yard.print();

        //  This is using an instance of the IsNeighborAZombie class for the
        //  comparator, and our "zombify" instance of our BoardFiddler<Pet>
        //  anonymous inner class for the operation.  Normally you would use
        //  the same approach for both, depending on which you prefer.  (I
        //  prefer the latter, although that doesn't work in all cases.)
        yard.forEach(new IsNeighborAZombie(), zombify);
        //  Now, there's a bug there... for each pet in the yard, if one of its
        //  neighbors is a zombie, *it* becomes a zombie... but that's almost
        //  certainly not what we actually want, because depending on the order
        //  in which we traverse the elements in the yard, we might turn *all*
        //  the pets into zombies.  Probably we want a forEachInCopy() method
        //  which creates a *copy* of the board, and for each cell in the
        //  original which matches the condition, we apply the change in the
        //  *copy* (and then return the copy).
        System.out.println("\nAfter zombification:\n");
        yard.print();

        //  Anyway, how about a Board which stores Integers?
        BoardWithGenerics<Integer> board = new BoardWithGenerics<>(10, 10, null);
        //  Instead of explicitly implementing the various functional
        //  interfaces, how about lambda expressions?  They *are* hard to read;
        //  here we're calling the version of forEach() which takes one
        //  BoardFiddler<T>, and it's going to get called once per element, and
        //  get passed the board, the row, and the column.
        board.forEach((b, r, c) -> b.set(r, c, Integer.valueOf(r * c)));
        System.out.println("\nBoard with Integers:\n");
        board.print();

        //  Here we're calling the one which takes a Conditional and a
        //  BoardFiddler.  For the conditional, we see that if the lambda
        //  takes only one argument, it doesn't need to be wrapped in
        //  parentheses; and if you have more than one line, wrap it in
        //  curlies.
        board.forEach(v ->
                {
                    if (v.intValue() > 40)
                    {
                        return true;
                    }
                    return false;
                },  //  that block could've been written as v -> v > 40
                (b, r, c) -> b.set(r, c, Integer.valueOf(81 - b.get(r, c))));
        System.out.println("\nAfter fiddling values over 40:\n");
        board.print();
    }
}
