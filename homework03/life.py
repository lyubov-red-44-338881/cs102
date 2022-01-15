import pathlib
import random
import typing as tp
from copy import deepcopy

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, size, randomize: bool = True, max_generations: tp.Optional[int] = None
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
        grid = [[0] * self.cols] * self.rows
        if randomize:
            grid = [[random.choice([0, 1]) for i in row] for row in grid]
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        x, y = cell[0], cell[1]
        neighbours = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i <= self.rows - 1 and 0 <= j <= self.cols - 1:
                    if x != i or y != j:
                        neighbours.append(self.curr_generation[i][j])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid = []
        for y in range(0, self.rows):
            row = []
            for x in range(0, self.cols):
                if sum(self.get_neighbours((y, x))) == 3 or (
                    self.curr_generation[y][x] == 1 and sum(self.get_neighbours((y, x))) == 2
                ):
                    row.append(1)
                else:
                    row.append(0)
            new_grid.append(row)
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_generations is not None:
            return self.generations >= self.max_generations
        return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        grid = []
        with open(filename) as f:
            for line in f:
                row = [int(i) for i in line.strip()]
                if row:
                    grid.append(row)
                    cols = len(row)
        game = GameOfLife((len(grid), cols))
        game.curr_generation = grid
        return game

    def save(self, filename) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w", encoding="utf-8") as f:
            for i, rows in enumerate(self.curr_generation):
                for j, elem in enumerate(rows):
                    f.write(str(elem))
                f.write("\n")
