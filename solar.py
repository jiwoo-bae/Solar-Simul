import pygame
from math import atan2, sin, cos, hypot
from planet import Planet

# Screen size
WIDTH = 1200
H_WIDTH = 600
HEIGHT = 800

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
JUPITER = (191, 177, 119)
URANUS = (78, 160, 163)

# Clock
clock = pygame.time.Clock()

def draw_planets(surface, planets, sun, moons, titans):
    """ Draws the planets """
    win.fill(BLACK)
    
    # Easier without the sun in the list
    sun.draw(surface)

    for planet in planets:
        planet.draw(surface)

    for planet in moons:
        planet.draw(surface)

    for planet in titans:
        planet.draw(surface)
    
    pygame.display.update()

def calculate_angle(p1, p2):
    """ Calculates the angle between two points """
    x1, y1 = p1
    x2, y2 = p2

    return atan2((y2 - y1), (x2 - x1))

def return_direction(angle):
    """ Returns two values between -1 and 1 which indicate the direction """
    dx = cos(angle)
    dy = sin(angle)

    return dx, dy

def distance(p1, p2):
    """ Returns the distance between two points """
    x1, y1 = p1
    x2, y2 = p2

    return hypot((x2 - x1), (y2 - y1))

def move_planets(planets, sun):
    """ Moves one planet to the other """

    for planet in planets:
        # Angle between two planets
        angle = calculate_angle(planet.coordinates, sun.coordinates)
        
        # Distance between two points
        _distance = distance(planet.coordinates, sun.coordinates)

        # Gravitational vector
        gravitational_pull = (planet.mass * sun.mass) / (_distance ** 2)

        dx, dy = return_direction(angle)
        gravity_vector = gravitational_pull * pygame.Vector2(dx, dy)

        # Calculating the new direction vector
        planet.velocity += gravity_vector

        planet.move()




def main(surface):
    """ Main function """
    run = True

    # Yes, I know that the Sun is a star but it's easier this way
    sun = Planet(333, H_WIDTH, HEIGHT/2, 0, 0, 150, YELLOW)
    venus = Planet(0.88112, H_WIDTH - 75, HEIGHT/2, 0, 1, 9.5, ORANGE)
    earth = Planet(1, H_WIDTH - 100, HEIGHT/2, 0, 1, 10, BLUE)
    saturn = Planet(3.152, H_WIDTH - 185, HEIGHT/2, 0, 1, 90, GRAY)
    moon = Planet(0.0123, H_WIDTH - 50, HEIGHT/2, 0, 1, 2, ORANGE)
    titan = Planet(0.0225, H_WIDTH - 50, HEIGHT/2, 0, 1, 2, ORANGE)

    # Planet list
    planets = [venus, earth, saturn, moon, titan]
    moons = [moon]
    titans = [titan]


    while run:
        clock.tick(500)

        draw_planets(surface, planets, sun, moons, titans)
        move_planets(planets, sun)
        move_planets(moons, earth)
        move_planets(moons, earth)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

# The screen
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

if __name__ == '__main__':
    main(win)
