import copy
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (x, 0), (x, self.height)
            )
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (0, y), (self.width, y)
            )

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        self.grid = self.create_grid(True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_lines()
            self.draw_grid()
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.grid = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.
        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.
        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.
        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        if randomize == True:
            return [
                [random.randint(0, 1) for x in range(self.cell_width)]
                for _ in range(self.cell_height)
            ]
        else:
            return [
                [0 for _ in range(self.cell_width)] for _ in range(self.cell_height)
            ]

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        tab = self.cell_size - 1
        for x in range(self.cell_width):
            for y in range(self.cell_height):
                if self.grid[y][x] != 0:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("green"),
                        (
                            (self.cell_size * x + 1),
                            (self.cell_size * y + 1),
                            tab,
                            tab,
                        ),
                    )
                else:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("white"),
                        (
                            (self.cell_size * x + 1),
                            (self.cell_size * y + 1),
                            tab,
                            tab,
                        ),
                    )

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.
        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.
        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.
        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        neighbours = []
        row, col = cell
        for l in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if (
                    0 <= row + l < self.cell_height
                    and 0 <= col + k < self.cell_width
                    and (l, k) != (0, 0)
                ):
                    neighbours.append(self.grid[row + l][col + k])
        return neighbours

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.
        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        new_gen = self.create_grid(False)
        for x in range(self.cell_height):
            for y in range(self.cell_width):
                new_ngbrs = self.get_neighbours((x, y)).count(1)
                if self.grid[x][y] == 0 and new_ngbrs == 3:
                    new_gen[x][y] = 1
                elif self.grid[x][y] == 1 and new_ngbrs in [2, 3]:
                    new_gen[x][y] = 1
        return new_gen


if __name__ == "__main__":
    game = GameOfLife(320, 240, 20)
    game.run()
