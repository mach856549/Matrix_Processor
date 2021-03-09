def det_matrix(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        #  This is the recursive case
        counter = 0
        sum_det = 0
        for i in matrix[0]:
            sub_matrix = find_submatrix(matrix, counter)
            minor = det_matrix(sub_matrix)
            cofactor = ((-1) ** counter) * minor
            counter += 1
            sum_det += i * cofactor
        return sum_det


def cofactor_matrix(matrix):
    new_matrix = create_empty_matrix(len(matrix), len(matrix[0]))
    if len(matrix) == 1:
        pass
    elif len(matrix) == 2:
        pass
    else:
        for row1 in range(len(matrix)):
            for col1 in range(len(matrix[0])):
                sub_matrix = find_submatrix(matrix, col1, row1)
                minor = det_matrix(sub_matrix)
                cofactor = ((-1) ** (col1 + row1)) * minor
                new_matrix[row1][col1] = cofactor
        return new_matrix


def find_submatrix(matrix, col, row=0):
    #  Clone matrix, the pop command modifies the underlying lists. Need to clone them first
    matrix_mod = []
    for j in matrix:
        matrix_mod.append(j[:])
    if row == 0:
        sub_matrix = matrix_mod[1:]
    elif row == len(matrix) - 1:
        sub_matrix = matrix_mod[:(len(matrix) - 1)]
    else:

        sub_matrix = matrix_mod[:row] + matrix_mod[(row + 1):]
    for i in sub_matrix:
        i.pop(col)
    return sub_matrix


def create_empty_matrix(n, m):
    matrix = []
    for i in range(int(n)):
        row_vector = [None] * int(m)
        matrix.append(row_vector)
    return matrix


def create_matrix(n, m):
    # map(int, input().split())
    matrix = []
    for i in range(int(n)):
        input_line = input()
        if "." in input_line:
            row_vector = list(map(float, input_line.strip().split()))
        else:
            row_vector = list(map(int, input_line.strip().split()))
        if len(row_vector) != int(m):
            print("Error")
            return error_found()
        matrix.append(row_vector)
    return matrix


def error_found():
    print("The operation cannot be performed.")
    return main_code()


def multiply_rowcol(row, col):
    #  This code takes two lists (vectors) and multiplies them
    #  The first vector should be a 1 x n matrix
    #  The second should be an n x 1 matrix
    #  Both should be given as a list eg [1, 2, 3, 4], [1, 1, 1, 1]
    if len(row) != len(col):
        print("There is an error with rowcol mutiplier")
        return error_found()
    else:
        sum_1 = 0
        for i in range(len(row)):
            sum_1 += row[i] * col[i]
        return sum_1


def matrix_columnlist(matrix, col_id):
    #  This code takes a 2D matrix and column id and returns a list representing the column
    #  i.e. it transposes the column and returns this as a single 1 x n matrix
    column_list = []
    for i in matrix:
        column_list.append(i[col_id])
    return column_list


def matrix_multiply():
    row1, col1 = input("Enter size of first matrix").strip().split(" ")
    print("Enter first matrix:")
    matrix1 = create_matrix(row1, col1)
    row2, col2 = input("Enter size of second matrix").strip().split(" ")
    print("Enter second matrix:")
    matrix2 = create_matrix(row2, col2)
    if int(col1) == int(row2):
        matrix_out = [[0 for i in range(int(col2))] for j in range(int(row1))]
        for j in range(int(row1)):
            for i in range(int(col2)):
                row_cur = matrix1[j]
                col_cur = matrix_columnlist(matrix2, i)
                matrix_out[j][i] = multiply_rowcol(row_cur, col_cur)
        matrix_out = matrix_format(matrix_out)
        return matrix_out
    else:
        print(f"ERROR WITH MATRIX, CANNOT MULTIPLY {col1} COLUMNS WITH {row2} ROWS")
        return error_found()


def matrix_multiply_constant(matrix1=None, const=None):
    if matrix1 is None:
        row1, col1 = input("Enter size of matrix:").strip().split(" ")
        print("Enter matrix:")
        matrix1 = create_matrix(row1, col1)
    if const is None:
        const = int(input("Enter constant:"))
    matrix1_n = len(matrix1)
    matrix1_m = len(matrix1[0])
    matrix_out = [[0 for i in range(matrix1_m)] for j in range(matrix1_n)]
    for n_row, row in enumerate(matrix1, 0):
        for n_col, val in enumerate(row, 0):
            matrix_out[n_row][n_col] = val * const
    matrix_out = matrix_format(matrix_out)
    return matrix_out


def matrix_format(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
             matrix[i][j] = int(matrix[i][j]) if isinstance(matrix[i][j], int) == True else matrix[i][j]
    return matrix

def matrix_add():
    row1, col1 = input("Enter size of first matrix").strip().split(" ")
    print("Enter first matrix:")
    matrix1 = create_matrix(row1, col1)
    row2, col2 = input("Enter size of second matrix").strip().split(" ")
    print("Enter second matrix:")
    matrix2 = create_matrix(row2, col2)
    matrix1_n = int(row1)
    matrix2_n = int(row2)
    matrix1_m = int(col1)
    matrix2_m = int(col2)
    if matrix1_m == matrix2_m and matrix1_n == matrix2_n:
        matrix_out = []
        for k in range(matrix1_n):
            row_out = []
            for p in range(matrix1_m):
                row_out.append(matrix1[k][p] + matrix2[k][p])
            matrix_out.append(row_out)
        matrix_out = matrix_format(matrix_out)
        return matrix_out
    else:
        print("ERROR")
        return error_found()


def matrix_print(matrix):
    matrix_n = len(matrix)
    matrix_m = len(matrix[0])
    print("The result is:")
    for n1 in range(matrix_n):
        row = ""
        for m1 in range(matrix_m):
            row += " " + str(matrix[n1][m1])
        print(row.strip())


def matrix_transpose_main(matrix):
    matrix_out = []
    col_num = len(matrix[0])
    for i in range(col_num):
        matrix_out.append(matrix_columnlist(matrix, i))
    return matrix_out


def matrix_transpose_side(matrix):
    matrix_out = []
    col_num = len(matrix[0])
    for i in range(1, col_num + 1):
        matrix_out.append((matrix_columnlist(matrix, (-1 * i)))[::-1])
    return matrix_out


def matrix_transpose_vertical(matrix):
    matrix_out = []
    for row in matrix:
        matrix_out.append(row[::-1])
    return matrix_out


def matrix_transpose_horizontal(matrix):
    return matrix[::-1]


def print_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    user_input = input("Your choice:")
    if user_input in ["0", "1", "2", "3", "4", "5", "6"]:
        if user_input == "0":
            exit()
        else:
            return user_input
    else:
        print("Invalid input, please type 1, 2, 3, 4, 5, 6 or 0")
        return print_menu()


def transpose_menu():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    user_input = input("Your choice:")
    if user_input in ["1", "2", "3", "4"]:
        row1, col1 = input("Enter matrix size:").strip().split(" ")
        print("Enter matrix:")
        matrix_in = create_matrix(row1, col1)
        if user_input == "1":
            output_matrix = matrix_transpose_main(matrix_in)
            matrix_print(output_matrix)
            print()
        elif user_input == "2":
            output_matrix = matrix_transpose_side(matrix_in)
            matrix_print(output_matrix)
            print()
        elif user_input == "3":
            output_matrix = matrix_transpose_vertical(matrix_in)
            matrix_print(output_matrix)
            print()
        elif user_input == "4":
            output_matrix = matrix_transpose_horizontal(matrix_in)
            matrix_print(output_matrix)
            print()
    else:
        print("Invalid input, please type 1, 2, 3, 4")
        return print_menu()


def matrix_inverse(matrix):
    matrix_det = det_matrix(matrix)
    if matrix_det == 0:
        print("This matrix doesn't have an inverse.")
        return
    else:
        C_matrix = cofactor_matrix(matrix)
        C_trans = matrix_transpose_main(C_matrix)
        inv_matrix = matrix_multiply_constant(C_trans, 1 / matrix_det)
        matrix_print(inv_matrix)
        print()


def main_code():
    user_selection = print_menu()
    if user_selection == "1":
        output_matrix = matrix_add()
        matrix_print(output_matrix)
        print()
    elif user_selection == "2":
        output_matrix = matrix_multiply_constant()
        matrix_print(output_matrix)
        print()
    elif user_selection == "3":
        output_matrix = matrix_multiply()
        matrix_print(output_matrix)
        print()
    elif user_selection == "4":
        transpose_menu()
    elif user_selection == "5":
        row1, col1 = input("Enter matrix size:").strip().split(" ")
        if int(row1) != int(col1):
            print("Matrix is not square")
            main_code()
        print("Enter matrix:")
        matrix1 = create_matrix(row1, col1)
        print("The result is:")
        print(det_matrix(matrix1))
        print()
    elif user_selection == "6":
        row1, col1 = input("Enter matrix size:").strip().split(" ")
        if int(row1) != int(col1):
            print("Matrix is not square")
            main_code()
        print("Enter matrix:")
        matrix1 = create_matrix(row1, col1)
        matrix_inverse(matrix1)


while True:
    main_code()
