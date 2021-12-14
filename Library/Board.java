
import java.util.ArrayList;

public class Board
{
    protected ArrayList<ArrayList<Integer>> board = new ArrayList<ArrayList<Integer>>();
    protected int fill;

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

    public void set(int row, int col, int value)
    {
        if (row >= this.board.size() || col >= this.board.get(0).size())
        {
            throw new IllegalArgumentException(String.format("board is %d x %d, and you tried to 'set' at %d, %d", this.board.size(), this.board.get(0).size(), row, col));
        }

        this.board.get(row).set(col, value);
    }

    public int get(int row, int col)
    {
        if (row >= this.board.size() || col >= this.board.get(0).size())
        {
            throw new IllegalArgumentException(String.format("board is %d x %d, and you tried to 'get' at %d, %d", this.board.size(), this.board.get(0).size(), row, col));   
        }

        return this.board.get(row).get(col);
    }

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

    public void print()
    {
        printBoard(this.board);
    }

    private void printBoard(ArrayList<ArrayList<Integer>> board)
    {
        for (ArrayList<Integer> row : board)
        {
            System.out.println(row);
        }
    }

    // want:
    // rotate, mirror, fill, clear

    // THIS SHOULD BE MOVED TO THE SQUAREBOARD CLASS
    // rotate in the clockwise direction by degrees amount. Only multiples of 90 are allowed, only square boards are allowed
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

    // mirrors the board across the vertical center axis
    public void mirrorLR()
    {
        // 1 2 3    3 2 1
        // 4 5 6    6 5 4
        // 7 8 9    9 8 7

        ArrayList<ArrayList<Integer>> newboard = new ArrayList<ArrayList<Integer>>();

        for (int ii = 0; ii < this.board.size(); ++ii)
        {
            ArrayList<Integer> row = new ArrayList<Integer>();

            for (int jj = 0; jj < this.board.get(0).size(); ++jj)
            {
                // row.add()
            }
        }
    }
}