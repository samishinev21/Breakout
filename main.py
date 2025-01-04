import pgzrun, os, pygame

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

HEIGHT = 1250
WIDTH = 1700
TITLE = "Breakout"

ball = pygame.image.load('images/ball.png')
scaled_ball = pygame.transform.scale(ball, (30, 30))
pygame.image.save(scaled_ball, 'images/ball.png')

ball = Actor("ball")
ball.pos = WIDTH // 2, HEIGHT // 2

ball_speed = [3, -3]

paddle_width = 115
paddle_height = 17

brick_width = 150
brick_height = 45

paddle_speed = 8

score = 0
lives = 3

player = Rect((WIDTH / 2, HEIGHT / 2 + 450), (paddle_width, paddle_height))

bricks = []
colors = ["cyan", "purple", "blue", "green", "yellow", "orange", "red", "pink"]

for row, color in enumerate(colors):
    for col in range(11):
        x = col * (brick_width + 5)
        y = 400 - row * (brick_height + 5)
        brick = {"rect": Rect((x, y), (brick_width, brick_height)), "color": color}
        bricks.append(brick)


def draw():
    screen.clear()
    screen.draw.filled_rect(player, "white")

    for brick in bricks:
        screen.draw.filled_rect(brick["rect"], brick["color"])

    ball.draw()
    screen.draw.text(f"SCORE: {score}", (WIDTH / 2 + 150, 0), fontsize=75, color="white")
    screen.draw.text(f"LIVES: {lives}", (WIDTH / 2 - 150, 0), fontsize=75, color="white")

def update():
    global score, lives

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if lives == 0:
        print("You lost")
    if ball.bottom >= HEIGHT:
        lives -= 1
        reset()
    if ball.colliderect(player):
        ball_speed[1] = -ball_speed[1]

    for brick in bricks[:]:
        if ball.colliderect(brick["rect"]):
            bricks.remove(brick)
            ball_speed[1] = -ball_speed[1]
            score += 1
            break

    if keyboard.a and player.left >= 0:
        player.x -= paddle_speed
    if keyboard.d and player.right <= WIDTH:
        player.x += paddle_speed

def reset():
    ball.y = HEIGHT / 2
    ball.x = WIDTH / 2


pgzrun.go()