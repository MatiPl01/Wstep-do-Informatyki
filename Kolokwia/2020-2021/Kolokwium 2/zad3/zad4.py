"""
Mateusz Łopaciński

Wewnątrz funkcji chess(T) korzystam ze zmiennych pomocniczych, które pomagają zredukować
czas obliczeń oraz przechowują informację o postawionych wieżach.

Funkcja row_col_sum służy do zwracania sumy szochowanych pól po dostawieniu nowej wieży na
pole o współrzędnych row_idx, col_idx, przekazanych jako argumenty. Funkcja oblicza sumę tylko
wtedy, gdy nie została ona wcześniej wyliczona.

Funkcja update_row_col_sums zmniejsza wartośc sum w oddpowiednim wierszu i kolumnie po dostawieniu
nowej wieży.

Funkcja place_tower szuka w pętli współrzędnych, dla których obecna suma szachowanych pól przez
dostawioną wieżę będzie największa.

Na koniec w pętli stawiam 2 wieże na planszy.
"""


def chess(T):
    row_sums = {}  # Store calculated sums to improve performance
    col_sums = {}

    taken_fields = set()  # Store information about already taken fields
    taken_rows = set()
    taken_cols = set()

    # A helper function to calculate sums
    def row_col_sum(row_idx, col_idx):
        # Get sum of values in a row
        if row_idx in taken_rows:  # Set row_sum to 0 if the row is already taken
            row_sum = 0
        else:
            if row_idx in row_sums:  # Return cached sum of a row if exists
                row_sum = row_sums[row_idx]
            else:
                row_sum = 0
                for i in range(len(T[row_idx])):
                    row_sum += T[row_idx][i]
                row_sums[row_idx] = row_sum  # Store calculated sum of all elements in a row
            row_sum -= T[row_idx][col_idx]  # Subtract value of the current element from this sum

        # Get sum of values in a column
        if col_idx in taken_cols:  # Set col_sum to 0 if the row is already taken
            col_sum = 0
        else:
            if col_idx in col_sums:  # Return cached sum of a column if exists
                col_sum = col_sums[col_idx]
            else:
                col_sum = 0
                for i in range(len(T)):
                    col_sum += T[i][col_idx]
                col_sums[col_idx] = col_sum  # Store calculated sum of all elements in a column
            col_sum -= T[row_idx][col_idx]  # Subtract value of the current element from this sum

        return row_sum + col_sum

    # Another helper function that subtracts proper values from sums of rows and columns
    def update_row_col_sums(row_idx, col_idx):
        for i in range(len(T)):
            row_sums[i] -= T[i][col_idx]
        for i in range(len(T[row_idx])):
            col_sums[i] -= T[row_idx][i]

    def place_tower():
        # As we accept also negative sums (because of integers) we have to set a placeholder
        # value to the lowest value possible (so the solution is to use a negative infinity)
        max_sum = float('-inf')

        max_sum_row_idx = None
        max_sum_col_idx = None
        for row_idx in range(len(T)):
            for col_idx in range(len(T[row_idx])):
                if (row_idx, col_idx) in taken_fields:
                    continue

                curr_sum = row_col_sum(row_idx, col_idx)
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    max_sum_row_idx = row_idx
                    max_sum_col_idx = col_idx

        coordinates = (max_sum_row_idx, max_sum_col_idx)
        if max_sum_row_idx is not None and max_sum_col_idx is not None:
            taken_rows.add(max_sum_row_idx)
            taken_cols.add(max_sum_col_idx)
            taken_fields.add(coordinates)
            update_row_col_sums(max_sum_row_idx, max_sum_col_idx)

        return coordinates

    result = ()
    for _ in range(2):
        result += place_tower()

    return result


if __name__ == '__main__':
    print(chess([[4,0,2], [3,0,0], [6,5,3]]))
    print(chess([[1,1,2,3], [-1,3,-1,4], [4,1,5,4], [5,0,3,6]]))
    print(chess([[-4,0,-2], [-3,0,0], [-6,-5,-3]]))
