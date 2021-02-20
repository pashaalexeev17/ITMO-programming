import copy
import pathlib
import random
from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:

        if randomize == True:
            return [
                [random.randint(0, 1) for x in range(self.cols)]
                for _ in range(self.rows)
            ]
        else:
            return [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        row, col = cell
        for l in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if (
                    0 <= row + l < self.rows
                    and 0 <= col + k < self.cols
                    and (l, k) != (0, 0)
                ):
                    neighbours.append(self.curr_generation[row + l][col + k])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_gen = self.create_grid(False)
        for x in range(self.rows):
            for y in range(self.cols):
                new_neighbours = self.get_neighbours((x, y)).count(1)
                if self.curr_generation[x][y] == 0 and new_neighbours == 3:
                    new_gen[x][y] = 1
                elif self.curr_generation[x][y] == 1 and new_neighbours in [2, 3]:
                    new_gen[x][y] = 1
        return new_gen

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation[:]
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations == self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename) as file:
            grid = [[int(x) for x in list(rw)] for rw in file.readline()]
        row, col = len(grid), len(grid[0])

        game = GameOfLife((row, col))
        game.curr_generation = grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename) as file:
            for row in self.curr_generation:
                file.write("".join([str(x) for x in row]))
                file.write("\n")
