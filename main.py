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
level = 1
balls_left = 3

player = Rect((WIDTH / 2, HEIGHT / 2 + 450), (paddle_width, paddle_height))
cyan_brick_0 = Rect((0, 400), (brick_width, brick_height))
cyan_brick_1 = Rect((155, 400), (brick_width, brick_height))
cyan_brick_2 = Rect((155 * 2, 400), (brick_width, brick_height))
cyan_brick_3 = Rect((155 * 3, 400), (brick_width, brick_height))
cyan_brick_4 = Rect((155 * 4, 400), (brick_width, brick_height))
cyan_brick_5 = Rect((155 * 5, 400), (brick_width, brick_height))
cyan_brick_6 = Rect((155 * 6, 400), (brick_width, brick_height))
cyan_brick_7 = Rect((155 * 7, 400), (brick_width, brick_height))
cyan_brick_8 = Rect((155 * 8, 400), (brick_width, brick_height))
cyan_brick_9 = Rect((155 * 9, 400), (brick_width, brick_height))
cyan_brick_10 = Rect((155 * 10, 400), (brick_width, brick_height))

purple_brick_0 = Rect((0, 400 - 50), (brick_width, brick_height))
purple_brick_1 = Rect((155, 400 - 50), (brick_width, brick_height))
purple_brick_2 = Rect((155 * 2, 400 - 50), (brick_width, brick_height))
purple_brick_3 = Rect((155 * 3, 400 - 50), (brick_width, brick_height))
purple_brick_4 = Rect((155 * 4, 400 - 50), (brick_width, brick_height))
purple_brick_5 = Rect((155 * 5, 400 - 50), (brick_width, brick_height))
purple_brick_6 = Rect((155 * 6, 400 - 50), (brick_width, brick_height))
purple_brick_7 = Rect((155 * 7, 400 - 50), (brick_width, brick_height))
purple_brick_8 = Rect((155 * 8, 400 - 50), (brick_width, brick_height))
purple_brick_9 = Rect((155 * 9, 400 - 50), (brick_width, brick_height))
purple_brick_10 = Rect((155 * 10, 400 - 50), (brick_width, brick_height))

blue_brick_0 = Rect((0, 400 - 100), (brick_width, brick_height))
blue_brick_1 = Rect((155, 400 - 100), (brick_width, brick_height))
blue_brick_2 = Rect((155 * 2, 400 - 100), (brick_width, brick_height))
blue_brick_3 = Rect((155 * 3, 400 - 100), (brick_width, brick_height))
blue_brick_4 = Rect((155 * 4, 400 - 100), (brick_width, brick_height))
blue_brick_5 = Rect((155 * 5, 400 - 100), (brick_width, brick_height))
blue_brick_6 = Rect((155 * 6, 400 - 100), (brick_width, brick_height))
blue_brick_7 = Rect((155 * 7, 400 - 100), (brick_width, brick_height))
blue_brick_8 = Rect((155 * 8, 400 - 100), (brick_width, brick_height))
blue_brick_9 = Rect((155 * 9, 400 - 100), (brick_width, brick_height))
blue_brick_10 = Rect((155 * 10, 400 - 100), (brick_width, brick_height))

green_brick_0 = Rect((0, 400 - 150), (brick_width, brick_height))
green_brick_1 = Rect((155, 400 - 150), (brick_width, brick_height))
green_brick_2 = Rect((155 * 2, 400 - 150), (brick_width, brick_height))
green_brick_3 = Rect((155 * 3, 400 - 150), (brick_width, brick_height))
green_brick_4 = Rect((155 * 4, 400 - 150), (brick_width, brick_height))
green_brick_5 = Rect((155 * 5, 400 - 150), (brick_width, brick_height))
green_brick_6 = Rect((155 * 6, 400 - 150), (brick_width, brick_height))
green_brick_7 = Rect((155 * 7, 400 - 150), (brick_width, brick_height))
green_brick_8 = Rect((155 * 8, 400 - 150), (brick_width, brick_height))
green_brick_9 = Rect((155 * 9, 400 - 150), (brick_width, brick_height))
green_brick_10 = Rect((155 * 10, 400 - 150), (brick_width, brick_height))

yellow_brick_0 = Rect((0, 400 - 200), (brick_width, brick_height))
yellow_brick_1 = Rect((155, 400 - 200), (brick_width, brick_height))
yellow_brick_2 = Rect((155 * 2, 400 - 200), (brick_width, brick_height))
yellow_brick_3 = Rect((155 * 3, 400 - 200), (brick_width, brick_height))
yellow_brick_4 = Rect((155 * 4, 400 - 200), (brick_width, brick_height))
yellow_brick_5 = Rect((155 * 5, 400 - 200), (brick_width, brick_height))
yellow_brick_6 = Rect((155 * 6, 400 - 200), (brick_width, brick_height))
yellow_brick_7 = Rect((155 * 7, 400 - 200), (brick_width, brick_height))
yellow_brick_8 = Rect((155 * 8, 400 - 200), (brick_width, brick_height))
yellow_brick_9 = Rect((155 * 9, 400 - 200), (brick_width, brick_height))
yellow_brick_10 = Rect((155 * 10, 400 - 200), (brick_width, brick_height))

orange_brick_0 = Rect((0, 400 - 250), (brick_width, brick_height))
orange_brick_1 = Rect((155, 400 - 250), (brick_width, brick_height))
orange_brick_2 = Rect((155 * 2, 400 - 250), (brick_width, brick_height))
orange_brick_3 = Rect((155 * 3, 400 - 250), (brick_width, brick_height))
orange_brick_4 = Rect((155 * 4, 400 - 250), (brick_width, brick_height))
orange_brick_5 = Rect((155 * 5, 400 - 250), (brick_width, brick_height))
orange_brick_6 = Rect((155 * 6, 400 - 250), (brick_width, brick_height))
orange_brick_7 = Rect((155 * 7, 400 - 250), (brick_width, brick_height))
orange_brick_8 = Rect((155 * 8, 400 - 250), (brick_width, brick_height))
orange_brick_9 = Rect((155 * 9, 400 - 250), (brick_width, brick_height))
orange_brick_10 = Rect((155 * 10, 400 - 250), (brick_width, brick_height))

red_brick_0 = Rect((0, 400 - 250), (brick_width, brick_height))
red_brick_1 = Rect((155, 400 - 250), (brick_width, brick_height))
red_brick_2 = Rect((155 * 2, 400 - 250), (brick_width, brick_height))
red_brick_3 = Rect((155 * 3, 400 - 250), (brick_width, brick_height))
red_brick_4 = Rect((155 * 4, 400 - 250), (brick_width, brick_height))
red_brick_5 = Rect((155 * 5, 400 - 250), (brick_width, brick_height))
red_brick_6 = Rect((155 * 6, 400 - 250), (brick_width, brick_height))
red_brick_7 = Rect((155 * 7, 400 - 250), (brick_width, brick_height))
red_brick_8 = Rect((155 * 8, 400 - 250), (brick_width, brick_height))
red_brick_9 = Rect((155 * 9, 400 - 250), (brick_width, brick_height))
red_brick_10 = Rect((155 * 10, 400 - 250), (brick_width, brick_height))

pink_brick_0 = Rect((0, 400 - 300), (brick_width, brick_height))
pink_brick_1 = Rect((155, 400 - 300), (brick_width, brick_height))
pink_brick_2 = Rect((155 * 2, 400 - 300), (brick_width, brick_height))
pink_brick_3 = Rect((155 * 3, 400 - 300), (brick_width, brick_height))
pink_brick_4 = Rect((155 * 4, 400 - 300), (brick_width, brick_height))
pink_brick_5 = Rect((155 * 5, 400 - 300), (brick_width, brick_height))
pink_brick_6 = Rect((155 * 6, 400 - 300), (brick_width, brick_height))
pink_brick_7 = Rect((155 * 7, 400 - 300), (brick_width, brick_height))
pink_brick_8 = Rect((155 * 8, 400 - 300), (brick_width, brick_height))
pink_brick_9 = Rect((155 * 9, 400 - 300), (brick_width, brick_height))
pink_brick_10 = Rect((155 * 10, 400 - 300), (brick_width, brick_height))

def draw():
    screen.clear()
    screen.draw.filled_rect(player, "white")
    screen.draw.filled_rect(cyan_brick_0, "cyan")
    screen.draw.filled_rect(cyan_brick_1, "cyan")
    screen.draw.filled_rect(cyan_brick_2, "cyan")
    screen.draw.filled_rect(cyan_brick_3, "cyan")
    screen.draw.filled_rect(cyan_brick_4, "cyan")
    screen.draw.filled_rect(cyan_brick_5, "cyan")
    screen.draw.filled_rect(cyan_brick_6, "cyan")
    screen.draw.filled_rect(cyan_brick_7, "cyan")
    screen.draw.filled_rect(cyan_brick_8, "cyan")
    screen.draw.filled_rect(cyan_brick_9, "cyan")
    screen.draw.filled_rect(cyan_brick_10, "cyan")

    screen.draw.filled_rect(purple_brick_0, "purple")
    screen.draw.filled_rect(purple_brick_1, "purple")
    screen.draw.filled_rect(purple_brick_2, "purple")
    screen.draw.filled_rect(purple_brick_3, "purple")
    screen.draw.filled_rect(purple_brick_4, "purple")
    screen.draw.filled_rect(purple_brick_5, "purple")
    screen.draw.filled_rect(purple_brick_6, "purple")
    screen.draw.filled_rect(purple_brick_7, "purple")
    screen.draw.filled_rect(purple_brick_8, "purple")
    screen.draw.filled_rect(purple_brick_9, "purple")
    screen.draw.filled_rect(purple_brick_10, "purple")

    screen.draw.filled_rect(blue_brick_0, "blue")
    screen.draw.filled_rect(blue_brick_1, "blue")
    screen.draw.filled_rect(blue_brick_2, "blue")
    screen.draw.filled_rect(blue_brick_3, "blue")
    screen.draw.filled_rect(blue_brick_4, "blue")
    screen.draw.filled_rect(blue_brick_5, "blue")
    screen.draw.filled_rect(blue_brick_6, "blue")
    screen.draw.filled_rect(blue_brick_7, "blue")
    screen.draw.filled_rect(blue_brick_8, "blue")
    screen.draw.filled_rect(blue_brick_9, "blue")
    screen.draw.filled_rect(blue_brick_10, "blue")

    screen.draw.filled_rect(green_brick_0, "green")
    screen.draw.filled_rect(green_brick_1, "green")
    screen.draw.filled_rect(green_brick_2, "green")
    screen.draw.filled_rect(green_brick_3, "green")
    screen.draw.filled_rect(green_brick_4, "green")
    screen.draw.filled_rect(green_brick_5, "green")
    screen.draw.filled_rect(green_brick_6, "green")
    screen.draw.filled_rect(green_brick_7, "green")
    screen.draw.filled_rect(green_brick_8, "green")
    screen.draw.filled_rect(green_brick_9, "green")
    screen.draw.filled_rect(green_brick_10, "green")

    screen.draw.filled_rect(yellow_brick_0, "yellow")
    screen.draw.filled_rect(yellow_brick_1, "yellow")
    screen.draw.filled_rect(yellow_brick_2, "yellow")
    screen.draw.filled_rect(yellow_brick_3, "yellow")
    screen.draw.filled_rect(yellow_brick_4, "yellow")
    screen.draw.filled_rect(yellow_brick_5, "yellow")
    screen.draw.filled_rect(yellow_brick_6, "yellow")
    screen.draw.filled_rect(yellow_brick_7, "yellow")
    screen.draw.filled_rect(yellow_brick_8, "yellow")
    screen.draw.filled_rect(yellow_brick_9, "yellow")
    screen.draw.filled_rect(yellow_brick_10, "yellow")

    screen.draw.filled_rect(orange_brick_0, "orange")
    screen.draw.filled_rect(orange_brick_1, "orange")
    screen.draw.filled_rect(orange_brick_2, "orange")
    screen.draw.filled_rect(orange_brick_3, "orange")
    screen.draw.filled_rect(orange_brick_4, "orange")
    screen.draw.filled_rect(orange_brick_5, "orange")
    screen.draw.filled_rect(orange_brick_6, "orange")
    screen.draw.filled_rect(orange_brick_7, "orange")
    screen.draw.filled_rect(orange_brick_8, "orange")
    screen.draw.filled_rect(orange_brick_9, "orange")
    screen.draw.filled_rect(orange_brick_10, "orange")

    screen.draw.filled_rect(red_brick_0, "red")
    screen.draw.filled_rect(red_brick_1, "red")
    screen.draw.filled_rect(red_brick_2, "red")
    screen.draw.filled_rect(red_brick_3, "red")
    screen.draw.filled_rect(red_brick_4, "red")
    screen.draw.filled_rect(red_brick_5, "red")
    screen.draw.filled_rect(red_brick_6, "red")
    screen.draw.filled_rect(red_brick_7, "red")
    screen.draw.filled_rect(red_brick_8, "red")
    screen.draw.filled_rect(red_brick_9, "red")
    screen.draw.filled_rect(red_brick_10, "red")

    screen.draw.filled_rect(pink_brick_0, "pink")
    screen.draw.filled_rect(pink_brick_1, "pink")
    screen.draw.filled_rect(pink_brick_2, "pink")
    screen.draw.filled_rect(pink_brick_3, "pink")
    screen.draw.filled_rect(pink_brick_4, "pink")
    screen.draw.filled_rect(pink_brick_5, "pink")
    screen.draw.filled_rect(pink_brick_6, "pink")
    screen.draw.filled_rect(pink_brick_7, "pink")
    screen.draw.filled_rect(pink_brick_8, "pink")
    screen.draw.filled_rect(pink_brick_9, "pink")
    screen.draw.filled_rect(pink_brick_10, "pink")

    ball.draw()
    screen.draw.text(f"{score}", (WIDTH / 2 - 400, 25), fontsize = 75, color = "white")
    screen.draw.text(f"Level {level}", (WIDTH / 2 + 300, 25), fontsize = 75, color = "white")
    screen.draw.text(f"Balls left: {balls_left}", (WIDTH / 2 - 150, 25),  fontsize = 75, color = "white")

def update():
    global score

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]

    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

#To DO reset function
    if ball.bottom <= 0:
        pass

    if ball.colliderect(player):
        ball_speed[1] = -ball_speed[1]

    if ball.colliderect(cyan_brick_0) or ball.colliderect(cyan_brick_1) or ball.colliderect(cyan_brick_2):
        pass

    if keyboard.a and player.left >= 0:
        player.x -= paddle_speed
    if keyboard.d and player.right <= WIDTH:
        player.x += paddle_speed

pgzrun.go()