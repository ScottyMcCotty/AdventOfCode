
import java.util.ArrayList;

public class BoardWithGenerics<T>
{
    //  Because these guys are "functional interfaces"--having only one method--
    //  you can use them for lambda expressions; example later.  Here's a
    //  conditional which just takes the value.
    @FunctionalInterface  //  <-- not required, but tells the compiler to slap
                          //      you if this *isn't* a functional interface.
    public interface Conditional<T>
    {
        /**
         * Returns true if the given value matches the condition; false if not.
         */
        public boolean matches(T value);
    }
    //  Same thing, but if you need to know the value's location in the board
    //  in order to evaluate the condition.
    @FunctionalInterface
    public interface PositionalConditional<T>
    {
        /**
         * Returns true if the value in the board at the given position
         * matches the condition; false if not.
         */
        public boolean matches(BoardWithGenerics<T> board, int row, int col);
    }
    @FunctionalInterface
    public interface BoardFiddler<T>
    {
        /**
         * Performs some operation on the element at the given position.
         */
        public void fiddleBoard(BoardWithGenerics<T> board, int row, int col);
    }

    protected ArrayList<ArrayList<T>> board;
    private int numRows;
    private int numCols;

    public BoardWithGenerics(int numRows, int numCols, T fill)
    {
        this.numRows = numRows;
        this.numCols = numCols;
        //  we can be slightly more efficient if we create the initial
        //  ArrayList at the right size instead of growing it, which is why I
        //  didn't initialize it above.
        board = new ArrayList<>(numRows);
        for (int ii = 0; ii < numRows; ++ii)
        {
            ArrayList<T> row = new ArrayList<>(numCols);

            for (int jj = 0; jj < numCols; ++jj)
            {
                row.add(fill);
            }

            board.add(row);
        }

        // System.out.println(board);
    }

    public int getNumRows()
    {
        return numRows;
    }
    
    public int getNumCols()
    {
        return numCols;
    }
    
    public void set(int row, int col, T value)
    {
        //  note that you only need this.board if you have a local variable
        //  which is also named board.  But if you *like* using this.
        //  everywhere, then fine!
        //if (row >= this.board.size() || col >= this.board.get(0).size())
        if (row >= board.size() || col >= board.get(0).size())
        {
            throw new IllegalArgumentException(String.format("board is %d x %d, and you tried to 'set' at %d, %d", this.board.size(), this.board.get(0).size(), row, col));
        }

        this.board.get(row).set(col, value);
    }

    public T get(int row, int col)
    {
        if (row >= this.board.size() || col >= this.board.get(0).size())
        {
            throw new IllegalArgumentException(String.format("board is %d x %d, and you tried to 'get' at %d, %d", this.board.size(), this.board.get(0).size(), row, col));   
        }

        return this.board.get(row).get(col);
    }

    //  Your addIf() and setIf() can be replaced by one guy:

    /**
     * Calls <code>operation</code> on each value which matches
     * <code>condition</code>.
     */
    public void forEach(Conditional<T> condition, BoardFiddler<T> operation)
    {
        for (int ii = 0; ii < this.board.size(); ++ii)
        {
            for (int jj = 0; jj < this.board.get(0).size(); ++jj)
            {
                if (condition.matches(get(ii, jj)))
                {
                    operation.fiddleBoard(this, ii, jj);
                }
            }
        }
    }

    //  well, OK, *two* guys, if you keep both Conditional and
    //  PositionalConditional.
    public void forEach(PositionalConditional<T> condition, BoardFiddler<T> operation)
    {
        for (int ii = 0; ii < this.board.size(); ++ii)
        {
            for (int jj = 0; jj < this.board.get(0).size(); ++jj)
            {
                if (condition.matches(this, ii, jj))
                {
                    operation.fiddleBoard(this, ii, jj);
                }
            }
        }
    }

    //  OK, I totally lied about only two versions of this method; how about
    //  one which doesn't take a condition, and applies the operation to *all*
    //  elements!
    public void forEach(BoardFiddler<T> operation)
    {
        for (int ii = 0; ii < this.board.size(); ++ii)
        {
            for (int jj = 0; jj < this.board.get(0).size(); ++jj)
            {
                operation.fiddleBoard(this, ii, jj);
            }
        }
    }

    public void print()
    {
        for (ArrayList<T> row : board)
        {
            System.out.println(row);
        }
    }

    //  I whacked the rest of the class, since this was just to give an example
    //  of those functional interfaces.
}
