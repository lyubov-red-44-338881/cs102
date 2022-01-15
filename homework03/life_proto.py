import random
import typing as tp
from copy import deepcopy

import pygame

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
grid = tp.List[Cells]


class GameOfLife:
    """class for game of life"""

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
        # Список клеток
        self.grid = self.create_grid(True)

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.grid = self.get_next_generation()
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> grid:
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
        if randomize:
            return [
                [random.randint(0, 1) for i in range(self.cell_width)]
                for i in range(self.cell_height)
            ]
        return [[0 for i in range(self.cell_width)] for i in range(self.cell_height)]

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        y = 0
        for i in self.grid:
            x = 0
            for j in i:
                color = pygame.Color("green") if j else pygame.Color("white")
                pygame.draw.rect(self.screen, color, (x, y, self.cell_size, self.cell_size))
                x += self.cell_size
            y += self.cell_size

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
        x, y = cell
        neighbours = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < self.cell_height and 0 <= j < self.cell_width:
                    neighbours.append(self.grid[i][j])
        neighbours.remove(self.grid[x][y])
        return neighbours

    def get_next_generation(self) -> grid:
        """
        Получить следующее поколение клеток.
        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        new_grid = []
        for x in range(0, self.height, self.cell_size):
            row = []
            for y in range(0, self.width, self.cell_size):
                row.append(
                    1
                    if sum(self.get_neighbours((x, y))) == 3
                    or self.grid[x // self.cell_size][y // self.cell_size] == 1
                    and sum(self.get_neighbours((x, y))) == 2
                    else 0
                )
            new_grid.append(row)
        return new_grid


if __name__ == "__main__":
    game = GameOfLife(320, 240, 20)
    game.run()
