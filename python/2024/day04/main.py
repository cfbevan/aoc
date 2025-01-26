class WordSearch:
    def __init__(self, input: str):
        """Create chart from string of characters."""
        self.data: list[str] = input.split("\n")
        self.length = len(self.data[0])
        self.height = len(self.data)

    def _get_lr(self, row: int, col: int, word_l: int) -> str | None:
        """Get a word from data at given coordinates and word length while moving left to right."""
        if col + (word_l - 1) < self.length:
            return "".join(self.data[row][col + i] for i in range(word_l))
        return None

    def _get_ddr(self, row: int, col: int, word_l: int) -> str | None:
        """Get a word from data at given coordinates and word length while moving diagonally down right."""
        if col + (word_l - 1) < self.length and row + (word_l - 1) < self.height:
            return "".join(self.data[row + i][col + i] for i in range(word_l))
        return None

    def _get_d(self, row: int, col: int, word_l: int) -> str | None:
        """Get a word from data at given coordinates and word length while moving down."""
        if row + (word_l - 1) < self.height:
            return "".join(self.data[row + i][col] for i in range(word_l))
        return None

    def _get_ddl(self, row: int, col: int, word_l: int) -> str | None:
        """Get a word form data at given coordinates and word length while moving diagonally down left."""
        if col - (word_l - 1) >= 0 and row + (word_l - 1) < self.height:
            return "".join(self.data[row + i][col - i] for i in range(word_l))
        return None

    def _get_rl(self, row: int, col: int, word_l: int) -> str | None:
        """Get a word from data at given coordinates and word length while moving right to left."""
        if col - (word_l - 1) >= 0 < self.height:
            return "".join(self.data[row][col - i] for i in range(word_l))
        return None

    def _get_dul(self, row: int, col: int, word_l: int) -> str | None:
        """Get a word form data at given coordinates and word length while moving diagonally up left."""
        if col - (word_l - 1) >= 0 and row - (word_l - 1) >= 0:
            return "".join(self.data[row - i][col - i] for i in range(word_l))
        return None

    def _get_u(self, row: int, col: int, word_l: int) -> str | None:
        """Get a word form data at given coordinates and word length while moving up."""
        if row - (word_l - 1) >= 0:
            return "".join(self.data[row - i][col] for i in range(word_l))
        return None

    def _get_dur(self, row: int, col: int, word_l: int) -> str | None:
        """Get a word form data at given coordinates and word length while moving diagonally up right."""
        if col + (word_l - 1) < self.length and row - (word_l - 1) >= 0:
            return "".join(self.data[row - i][col + i] for i in range(word_l))
        return None

    def _wordlist(self, row: int, col: int, word_l: int) -> list[str]:
        """Get a list of words created by starting at given row and col with given length."""
        return [
            self._get_lr(row, col, word_l),
            self._get_ddr(row, col, word_l),
            self._get_d(row, col, word_l),
            self._get_ddl(row, col, word_l),
            self._get_rl(row, col, word_l),
            self._get_dul(row, col, word_l),
            self._get_u(row, col, word_l),
            self._get_dur(row, col, word_l),
        ]

    def _check(self, row: int, col: int, word: str) -> int:
        """Find number of occurrences of word at given row and col."""
        word_l = len(word)
        return sum([w == word or 0 for w in self._wordlist(row, col, word_l)])

    def find(self, word: str) -> int:
        """Find all instances of word, return number found."""
        return sum(
            self._check(r, c, word)
            for r in range(self.height)
            for c in range(self.length)
        )

    def is_x_word(self, row: int, col: int, word: str) -> bool:
        """Check if given row and col form X with given word."""
        word_l = len(word)
        return (
            sum(
                [
                    self._get_ddr(row - 1, col - 1, word_l) == word or 0,
                    self._get_ddl(row - 1, col + 1, word_l) == word or 0,
                    self._get_dul(row + 1, col + 1, word_l) == word or 0,
                    self._get_dur(row + 1, col - 1, word_l) == word or 0,
                ]
            )
            == 2
        )

    def find_x(self, word: str) -> int:
        """Find all instances of X with word, return number found."""
        return sum(
            self.is_x_word(r, c, word)
            for r in range(1, self.height - 1)
            for c in range(1, self.length - 1)
        )


def pt1(input: str) -> str:
    return str(WordSearch(input).find("XMAS"))


def pt2(input: str) -> str:
    return str(WordSearch(input).find_x("MAS"))


if __name__ == "__main__":
    with open("day04/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
