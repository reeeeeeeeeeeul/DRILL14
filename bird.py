from pico2d import get_canvas_width, load_image

import game_framework


FRAME_WIDTH = 183
FRAME_HEIGHT = 168
FRAME_COUNT = 14
DEFAULT_BIRD_COUNT = 10

FLIGHT_SPEED = 120
ANIMATION_FPS = 10


class Bird:
    image = None

    def __init__(self, x, y, speed=FLIGHT_SPEED):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.image = Bird.image
        self.x, self.y = x, y
        self.speed = abs(speed)
        self.direction = 1
        self.frame = 0

    def update(self):
        self.x += self.direction * self.speed * game_framework.frame_time

        half_width = FRAME_WIDTH / 2
        if self.x >= get_canvas_width() - half_width:
            self.x = get_canvas_width() - half_width
            self.direction = -1
        elif self.x <= half_width:
            self.x = half_width
            self.direction = 1

        self.frame = (
            self.frame + ANIMATION_FPS * game_framework.frame_time
        ) % FRAME_COUNT

    def draw(self):
        frame = int(self.frame)
        column = frame % 5
        row = frame // 5
        flip = '' if self.direction == 1 else 'h'

        self.image.clip_composite_draw(
            column * FRAME_WIDTH,
            row * FRAME_HEIGHT,
            FRAME_WIDTH,
            FRAME_HEIGHT,
            0,
            flip,
            self.x,
            self.y,
            FRAME_WIDTH,
            FRAME_HEIGHT,
        )


class BirdFlock:
    def __init__(self, count=DEFAULT_BIRD_COUNT):
        self.birds = [
            Bird(
                x=100 + index * 150,
                y=350 + (index % 3) * 35,
            )
            for index in range(count)
        ]

    def update(self):
        for bird in self.birds:
            bird.update()

    def draw(self):
        for bird in self.birds:
            bird.draw()
