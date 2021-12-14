
import java.util.ArrayList;

public class Board
{
    protected ArrayList<ArrayList<Integer>> board = new ArrayList<ArrayList<Integer>>();
    protected int fill;

    /**
     * A rectangular Board constructor where every cell is initialized with the specified fill value.
     * <p>
     * Has built in methods for rotating, mirroring, and folding.
     * 
     * @param numRows   Number of rows
     * @param numCols   Number of columns
     * @param fill      Value to fill in each cell
     */
    public Board(int numRows, int numCols, int fill)
    {
        this.fill = fill;

        // initialize the board
        for (int ii = 0; ii < numRows; ++ii)
        {
            ArrayList<Integer> row = new ArrayList<Integer>();

            for (int jj = 0; jj < numCols; ++jj)
            {
                row.add(fill);
            }

            board.add(row);
        }

        // System.out.println(board);
    }

    /**
     * Set the value at the specified position.
     * 
     * @param row   Row of the board, indexed from 0 starting at the top
     * @param col   Column of the board, indexed from 0 starting on the left
     * @param value New value of the cell
     */
    public void set(int row, int col, int value)
    {
        if (row >= this.board.size() || col >= this.board.get(0).size())
        {
            throw new IllegalArgumentException(String.format("board is %d x %d, and you tried to 'set' at %d, %d", this.board.size(), this.board.get(0).size(), row, col));
        }

        this.board.get(row).set(col, value);
    }

    /**
     * Get the value at the specified position.
     * 
     * @param row   Row of the board, indexed from 0 starting at the top
     * @param col   Column of the board, indexed from 0 starting on the left
     * @return      The value in the cell
     */
    public int get(int row, int col)
    {
        if (row >= this.board.size() || col >= this.board.get(0).size())
        {
            throw new IllegalArgumentException(String.format("board is %d x %d, and you tried to 'get' at %d, %d", this.board.size(), this.board.get(0).size(), row, col));   
        }

        return this.board.get(row).get(col);
    }

    /**
     * @return  The default fill value for this board, which was set in the object constructor
     */
    public int getFill()
    {
        return this.fill;
    }

    /**
     * For every cell in the board, the value in that cell is incremented by <code>increment</code>
     * if the cell is equal to <code>condition</code>.
     * <p>
     * Similar to the <code>setIf()</code> method but meant for setting a new value which depends on the previous value
     * 
     * @param condition The condition to check whether each cell is equal to
     * @param increment The value to change each cell if it matches <code>condition</code>
     */
    public void addIf(int condition, int increment)
    {
        for (int ii = 0; ii < this.board.size(); ++ii)
        {
            for (int jj = 0; jj < this.board.get(0).size(); ++jj)
            {
                if (get(ii, jj) == condition)
                {
                    set(ii, jj, get(ii, jj) + increment);
                }
            }
        }
    }

    /**
     * For every cell in the board, the value in that cell is set to <code>value</code>
     * if the cell is equal to <code>condition</code>.
     * <p>
     * Similar to the <code>addIf()</code> method but meant for setting a new value regardless of the previous value
     * 
     * @param condition The condition to check whether each cell is equal to
     * @param value     The value to set each cell if it matches <code>condition</code>
     */
    public void setIf(int condition, int value)
    {
        for (int ii = 0; ii < this.board.size(); ++ii)
        {
            for (int jj = 0; jj < this.board.get(0).size(); ++jj)
            {
                if (get(ii, jj) == condition)
                {
                    set(ii, jj, value);
                }
            }
        }
    }

    /**
     * Prints the contents of <code>this.board</code>, where (0,0) is the top left corner.
     */
    public void print()
    {
        printBoard(this.board);
    }

    /**
     * Prints any board.
     * <p>
     * Useful for debugging methods which change the values in a board because
     * the board can be printed in its before and after states.
     * 
     * @param board The board to print
     */
    private void printBoard(ArrayList<ArrayList<Integer>> board)
    {
        for (ArrayList<Integer> row : board)
        {
            System.out.println(row);
        }
    }

    // want:
    // rotate, mirror, fill, clear

    /**
     * Rotates the contents of <code>this.board</code> by <code>degrees</code> amount.
     * <p>
     * NOTE TO SELF: This method should be moved to the SquareBoard class which extends Board,
     * because rotations are only defined for a square board.
     * 
     * @param degrees   The amount of degrees to rotate. Clockwise is positive. Must be a multiple of 90
     */
    public void rotate(int degrees)
    {
        // is this a valid board to rotate?
        if (this.board.size() != this.board.get(0).size())
        {
            throw new IllegalArgumentException(String.format("board is %d x %d, but only rotations on square boards are allowed", this.board.get(0).size(), this.board.size()));
        }

        // is this a valid amount to rotate?
        if (degrees % 90 != 0)
        {
            throw new IllegalArgumentException(String.format("degrees = %d, but only rotations in multiples of 90 are allowed", degrees));
        }

        // eliminate extraneous rotations
        degrees = degrees % 360;

        // get degrees into the range of [0, 270]
        while (degrees < 0)
        {
            degrees += 360;
        }

        // okay, now do the actual rotation by copying the correct values into a new board
        int length = this.board.size();
        ArrayList<ArrayList<Integer>> newboard = new ArrayList<ArrayList<Integer>>();

        if (degrees == 0)
        {
            // 1 2 3    1 2 3
            // 4 5 6    4 5 6
            // 7 8 9    7 8 9
            
            newboard = this.board;
        }
        else if (degrees == 90)
        {
            // 1 2 3    7 4 1
            // 4 5 6    8 5 2
            // 7 8 9    9 6 3

            for (int ii = 0; ii < length; ++ii)
            {
                ArrayList<Integer> row = new ArrayList<Integer>();

                for (int jj = 0; jj < length; ++jj)
                {
                    row.add( this.board.get(length - 1 - jj).get(ii) );
                }
                newboard.add(row);
            }
        }
        else if (degrees == 180)
        {
            // 1 2 3    // 9 8 7
            // 4 5 6    // 6 5 4
            // 7 8 9    // 3 2 1

            for (int ii = 0; ii < length; ++ii)
            {
                ArrayList<Integer> row = new ArrayList<Integer>();

                for (int jj = 0; jj < length; ++jj)
                {
                    row.add( this.board.get(length - 1 - ii).get(length - 1 - jj) );
                }
                newboard.add(row);
            }
        }
        else if (degrees == 270)
        {
            // 1 2 3    // 3 6 9
            // 4 5 6    // 2 5 8
            // 7 8 9    // 1 4 7

            for (int ii = 0; ii < length; ++ii)
            {
                ArrayList<Integer> row = new ArrayList<Integer>();

                for (int jj = 0; jj < length; ++jj)
                {
                    row.add( this.board.get(jj).get(length - 1 - ii) );
                }
            }
        }

        System.out.format("Rotation of %d degrees complete.\nOld board:\n", degrees);
        printBoard(this.board);
        System.out.println("New board:");
        printBoard(newboard);

        this.board = newboard;
    }

    /**
     * Mirror the contents of <code>this.board</code> across the vertical center axis.
     * <p>
     * The board: <p>
     * 1 2 3 <p>
     * 4 5 6 <p>
     * 7 8 9 <p>
     * becomes: <p>
     * 3 2 1 <p>
     * 6 5 4 <p>
     * 9 8 7 <p>
     */
    public void mirrorHorizontal()
    {
        // 1 2 3    3 2 1
        // 4 5 6    6 5 4
        // 7 8 9    9 8 7

        ArrayList<ArrayList<Integer>> newboard = new ArrayList<ArrayList<Integer>>();

        for (int ii = 0; ii < this.board.size(); ++ii)
        {
            ArrayList<Integer> row = new ArrayList<Integer>();

            for (int jj = 0; jj < this.board.get(ii).size(); ++jj)
            {
                row.add( this.board.get(ii).get(this.board.get(ii).size() - 1 - jj) );
            }

            newboard.add(row);
        }

        System.out.println("Mirror across vertical axis complete.\nOld board:");
        printBoard(this.board);
        System.out.println("New board:");
        printBoard(newboard);

        this.board = newboard;
    }

    /**
     * Mirror the contents of <code>this.board</code> across the horizontal center axis.
     * <p>
     * The board: <p>
     * 1 2 3 <p>
     * 4 5 6 <p>
     * 7 8 9 <p>
     * becomes: <p>
     * 7 8 9 <p>
     * 4 5 6 <p>
     * 1 2 3 <p>
     */
    public void mirrorVertical()
    {
        // 1 2 3    7 8 9
        // 4 5 6    4 5 6
        // 7 8 9    1 2 3

        ArrayList<ArrayList<Integer>> newboard = new ArrayList<ArrayList<Integer>>();

        for (int ii = 0; ii < this.board.size(); ++ii)
        {
            ArrayList<Integer> row = new ArrayList<Integer>();

            for (int jj = 0; jj < this.board.get(ii).size(); ++jj)
            {
                row.add( this.board.get(this.board.size() - 1 - ii).get(jj) );
            }

            newboard.add(row);
        }

        System.out.println("Mirror across horizontal axis complete.\nOld board:");
        printBoard(this.board);
        System.out.println("New board:");
        printBoard(newboard);

        this.board = newboard;
    }

    /**
     * Fills the entire board with <code>value</code>.
     * 
     * @param value The value to fill into the entire board
     */
    public void fill(int value)
    {
        for (int ii = 0; ii < this.board.size(); ++ii)
        {
            for (int jj = 0; jj < this.board.get(ii).size(); ++ii)
            {
                this.board.get(ii).set(jj, value);
            }
        }
    }
    
    /**
     * Fills the entire value with this board's default fill value.
     */
    public void clear()
    {
        fill(this.fill);
    }
}