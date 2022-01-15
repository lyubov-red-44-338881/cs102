import pygame
from life import GameOfLife
from ui import UI


class GUI(UI):
    """отрисовка и запуск игры"""

    def __init__(self, game_life: GameOfLife, cell_size: int = 20, speed: int = 10) -> None:
        super().__init__(game_life)
        self.cell_size = cell_size
        self.speed = speed
        self.height = self.life.rows * self.cell_size, self.life.cols * self.cell_size
        self.width = self.life.rows * self.cell_size, self.life.cols * self.cell_size
        self.screen = pygame.display.set_mode((self.height, self.width))

    def draw_lines(self) -> None:
        """Отобразить сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, x), (self.height, x))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (y, 0), (y, self.width))

    def draw_grid(self) -> None:
        """Отобразить состояние клеток."""
        y = 0
        for row in self.life.curr_generation:
            x = 0
            for cell in row:
                color = pygame.Color("green") if cell else pygame.Color("white")
                pygame.draw.rect(self.screen, color, (y, x, self.cell_size, self.cell_size))
                x += self.cell_size
            y += self.cell_size

    def run(self) -> None:
        """запускаем игру"""
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        is_game_running = True
        is_game_in_pause = False
        while is_game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        is_game_running = False
                    elif event.key == pygame.K_SPACE:
                        is_game_in_pause = not is_game_in_pause
                    elif event.key == pygame.K_DOWN:
                        self.life.save(Path("Game_of_life.txt"))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_position = pygame.mouse.get_pos()
                        x_position, y_position = (
                            click_position[1] // self.cell_size,
                            click_position[0] // self.cell_size,
                        )
                        self.life.curr_generation[x_position][y_position] = (
                            1 - self.life.curr_generation[x_position][y_position]
                        )
            self.draw_lines()
            self.draw_grid()
            if not is_game_in_pause:
                self.life.step()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == "__main__":
    life = GameOfLife((30, 30))
    gui = GUI(life)
    gui.run()
