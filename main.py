import engine

paddle_y = 24

paddle2_y = 24

ball_x = 30
ball_y = 30

dx = 0.1
dy = 0.1

score = 0


def init_engine():
    engine.import_image("paddle.png", "paddle")
    engine.import_image("ball.png", "ball")


def update():
    global paddle_y
    global paddle2_y
    global ball_x
    global ball_y
    global dx
    global dy
    global score

    if engine.key_down("K_UP"): paddle_y -= 2
    if engine.key_down("K_DOWN"): paddle_y += 2
    if paddle_y < 0: paddle_y = 0
    if paddle_y + 16 > 64: paddle_y = 48

    ball_x += dx
    ball_y += dy

    if ball_y > 60:
        dy = -0.5
    if ball_y < 0:
        dy = 0.5
    if ball_x > 60:
        dx = -0.5
        ball_x = 30
        ball_y = 30
        score -= 1
    if ball_x < 0:
        dx = 0.5
        ball_x = 30
        ball_y = 30
        score += 1

    if ball_x > 54 and paddle_y < ball_y < paddle_y + 16:
        dx = -0.5
    if ball_x < 6 and paddle2_y < ball_y < paddle2_y + 16:
        dx = 0.5

    if ball_y < paddle2_y + 8: paddle2_y -= 0.38
    if ball_y > paddle2_y + 8: paddle2_y += 0.38


def draw():
    engine.screen.fill("#181425")
    engine.text(score, 30, 0)
    engine.draw("paddle", 58, paddle_y)
    engine.draw("paddle", 2, paddle2_y)
    engine.draw("ball", ball_x, ball_y)
