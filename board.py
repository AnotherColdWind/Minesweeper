import pygame
from mines import coords, window_width, window_height
from random import choice

class GameBoard(pygame.sprite.Sprite):
    def __init__(self, 
                 mode, 
                 coordinates: list[coords], 
                 size: int, 
                 lines: int, 
                 thickness: int, 
                 offset: int, 
                 cellgroup: pygame.sprite.Group):
        super().__init__()
        self.cells = []
        self.mode = mode
        self.image = pygame.Surface((size, size))
        self.image.fill("Teal")
        self.image.fill("Black", (offset - 3, offset - 3, size - offset - 3, size - offset - 3))
        self.image.fill("White", (offset, offset, size - 2*offset, size - 2*offset))
        self.rect = self.image.get_rect()
        self.rect.center = (640, 360)
        for x in range(lines + 1):
            line_pos = ((size - offset * 2) / (lines)) * x + offset
            pygame.draw.line(self.image, "Black", (offset, line_pos), (size - offset, line_pos), thickness)
            pygame.draw.line(self.image, "Black", (line_pos, offset), (line_pos, size - offset), thickness)

        line_pos = ((size - offset * 2) / (lines)) + offset
        print(line_pos)
        square_size = line_pos - offset - thickness
        print(square_size)
        for coord in coordinates:
            self.cells.append(cell(coord, 
                                   (
                                    window_width/2 - size/2 + offset + square_size/2 + (square_size * (coord.x - 1)) + thickness/2, 
                                    window_height/2 - size/2 + offset + square_size/2 + (square_size * (coord.y - 1)) + thickness/2
                                    ), 
                                   square_size, 
                                   cellgroup))
            print((
                    window_width/2 - size/2 + offset + square_size/2 + (square_size * (coord.x - 1)) + thickness, 
                    window_height/2 - size/2 + offset + square_size/2 + (square_size * (coord.y - 1)) + thickness
                                    ))
            
    def update(self):
        pass

class cell(pygame.sprite.Sprite): # yes he perfect
    def __init__(self, 
                 coord: coords, 
                 pos: tuple[int, int], 
                 size: int, 
                 *groups):
        colors = ["Green", "Blue", "Red", "Cyan", "Teal", "Yellow", "Orange"]
        super().__init__(*groups)
        self.image = pygame.Surface((size, size))
        self.image.fill(choice(colors))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.coord = coord

    def reveal():
        pass