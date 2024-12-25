def generate_magic_squares():
    def is_magic_square(square):
        target_sum = sum(square[0])
        for row in square:
            if sum(row) != target_sum:
                return False
        for col in range(len(square)):
            if sum(square[row][col] for row in range(len(square))) != target_sum:
                return False
        if sum(square[i][i] for i in range(len(square))) != target_sum:
            return False
        if sum(square[i][len(square) - i - 1] for i in range(len(square))) != target_sum:
            return False
        return True

    def generate_squares(current_square, remaining_numbers):
        if not remaining_numbers:
            if is_magic_square(current_square):
                yield current_square
        else:
            for i in range(len(current_square)):
                for j in range(len(current_square)):
                    if current_square[i][j] is None:
                        for number in remaining_numbers:
                            new_square = [row[:] for row in current_square]
                            new_square[i][j] = number
                            new_remaining_numbers = remaining_numbers - {number}
                            if len(new_remaining_numbers) == 0:
                                if is_magic_square(new_square):
                                    yield new_square
                            else:
                                yield from generate_squares(new_square, new_remaining_numbers)

    numbers = set(range(9))
    square = [[None]*3 for _ in range(3)]
    return list(generate_squares(square, numbers))

magic_squares = generate_magic_squares()
print("Количество магических квадратов:", len(magic_squares))