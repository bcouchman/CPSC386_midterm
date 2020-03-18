import pygame as pg


class Ship:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.image = pg.image.load('image/ship.gif')
        self.rect = self.image.get_rect()
        screen_rect = self.screen.get_rect()
        self.rect.midbottom = screen_rect.midbottom
        self.speed = game.settings.speed
        self.moving_right = False

    def center_ship(self):
        screen_rect = self.screen.get_rect()
        self.rect.midbottom = screen_rect.midbottom

    def fire(self):
        newlaser = Laser(game)  # game contains screen and ship
        self.game.lasers.add(newlaser)

    def remove_lasers(self):
        for laser in self.game.lasers.copy():
            self.game.lasers.remove(laser)

    def move(self):
        if self.moving_right:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > self.screen.right:
            self.rect.right = self.screen.right

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.move()
        self.draw()


class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector ({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __rmul__(self, k: float):
        return Vector(self.x * k, self.y * k)

    def __mul__(self, k: float):
        return Vector(self.x * k, self.y * k)

    def __truediv__(self, k: float):
        return Vector(self.x / k, self.y / k)

    def __neg__(self):
        self.x *= -1
        self.y *= -1

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def test(): # feel free to change the test code
        v = Vector(x=5, y=5)
        u = Vector(x=4, y=4)
        print('v is {}'.format(v))
        print('u is {}'.format(u))
        print('uplusv is {}'.format(u + v))
        print('uminusv is {}'.format(u - v))
        print('ku is {}'.format(3 * u))
        print('-u is {}'.format(-1 * u))


def main():
    Vector.test()
