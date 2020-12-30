import pygame
import sys

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, loc = 'idle.png'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(loc) #pygame.Surface([20, 20])
        #self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.center = pos

def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50
    bg = [255, 255, 255]
    size =[500, 500]


    screen = pygame.display.set_mode(size)

    player = Sprite([0, 0])
    player.move = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]
    player.vx = 5
    player.vy = 5


    wall = pygame.sprite.Sprite()
    wall.image = pygame.transform.scale(pygame.image.load("wall.png"), (100, 100))
    wall.rect = wall.image.get_rect()
    wall.rect.center = (200, 200)


    wall_group = pygame.sprite.Group()
    wall_group.add(wall)

    player_group = pygame.sprite.Group()
    player_group.add(player)

    # I added loop for a better exit from the game
    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0

        key = pygame.key.get_pressed()
        before_pos = player.rect.x, player.rect.y

        for i in range(2):
            if key[player.move[i]]:
                player.rect.x += player.vx * [-1, 1][i]

        for i in range(2):
            if key[player.move[2:4][i]]:
                player.rect.y += player.vy * [-1, 1][i]

        screen.fill(bg)

        # first parameter takes a single sprite
        # second parameter takes sprite groups
        # third parameter is a do kill command if true
        # all group objects colliding with the first parameter object will be
        # destroyed. The first parameter could be bullets and the second one
        # targets although the bullet is not destroyed but can be done with
        # simple trick bellow
        hit = pygame.sprite.spritecollide(player, wall_group, False)
        if key[pygame.K_w]:
            if abs(player.rect.top - wall.rect.bottom) < 10 and hit:
                player.rect.y = before_pos[1]
            else:
                player.rect.y -= 1
        if key[pygame.K_a]:
            if abs(player.rect.left - wall.rect.right) < 10 and hit:
                player.rect.x = before_pos[0]
            else:
                player.rect.x -= 1
        if key[pygame.K_s]:
            if abs(player.rect.bottom - wall.rect.top) < 10 and hit:
                player.rect.y = before_pos[1]
            else:
                player.rect.y += 1
        if key[pygame.K_d]:
            if abs(player.rect.right - wall.rect.left) < 10 and hit:
                player.rect.x = before_pos[0]
            else:
                player.rect.x += 1

        player_group.draw(screen)
        wall_group.draw(screen)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    # sys.exit


if __name__ == '__main__':
    main()