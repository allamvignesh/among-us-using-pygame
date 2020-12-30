#exam.py
import sys
import pygame as pg
from pygame.math import Vector2


class Wall(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, *groups):
        super().__init__(*groups)
        self.image = pg.Surface((w, h))
        self.image.fill(pg.Color('goldenrod4'))
        self.rect = self.image.get_rect(topleft=(x, y))


def ray_cast(origin, target, obstacles):
    """Calculate the closest collision point.

    Adds the normalized `direction` vector to the `current_pos` to
    move along the heading vector and uses `pygame.Rect.collidepoint`
    to see if `current_pos` collides with an obstacle.

    Args:
        origin (pygame.math.Vector2, tuple, list): Origin of the ray.
        target (pygame.math.Vector2, tuple, list): Endpoint of the ray.
        obstacles (pygame.sprite.Group): A group of obstacles.

    Returns:
        pygame.math.Vector2: Closest collision point or target.
    """
    current_pos = Vector2(origin)
    heading = target - origin
    # A normalized vector that points to the target.
    direction = heading.normalize()
    for _ in range(int(heading.length())):
        current_pos += direction
        for sprite in obstacles:
            # If the current_pos collides with an
            # obstacle, return it.
            if sprite.rect.collidepoint(current_pos):
                return current_pos
    # Otherwise return the target.
    return Vector2(target)


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    walls = pg.sprite.Group()
    Wall(100, 170, 90, 20, all_sprites, walls)
    Wall(200, 100, 20, 140, all_sprites, walls)
    Wall(400, 60, 150, 100, all_sprites, walls)

    pos = Vector2(320, 440)
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        all_sprites.update()
        collision_point = ray_cast(pos, pg.mouse.get_pos(), walls)
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        pg.draw.line(screen, (50, 190, 100), pos, pg.mouse.get_pos(), 2)
        pg.draw.circle(screen, (40, 180, 250), [int(x) for x in collision_point], 5)

        pg.display.flip()
        clock.tick(30)
if __name__ == "__main__":
	main()