import engine_beta as engine

# variables
paddle_y = 24
paddle2_y = 24
ball_x = 30
ball_y = 30
dx = 0.1
dy = 0.1
score = 0

class begin:
    def __init__(self,) -> None:
        self.engine = engine.engine_()
        
        
    # importing images and SFX into the game
    def initialize(self):
        # importing the images
        self.engine.image_import("Assets/paddle.png", "paddle")
        self.engine.image_import("Assets/ball.png", "ball")

        # importing the SFX
        self.engine.import_sfx("Assets/Hit.wav", "ball_hit")
        self.engine.import_sfx("Assets/Score.wav", "score")


    # updating the game
    def update(self):
        global paddle_y, paddle2_y, ball_x, ball_y, dx, dy, score

        # checks if up arrow or down arrow is pressed and moves the paddle
        if self.engine.key_down("K_UP"):
            paddle_y -= 2
        if self.engine.key_down("K_DOWN"):
            paddle_y += 2

        # locks the paddle so it cant go off-screen
        if paddle_y < 0:
            paddle_y = 0
        if paddle_y + 16 > 64:
            paddle_y = 48

        # adds the ball velocity to the balls position
        ball_x += dx
        ball_y += dy

        # moves the bot paddle
        if ball_y < paddle2_y + 8:
            paddle2_y -= 0.42
        if ball_y > paddle2_y + 8:
            paddle2_y += 0.42

        # collisions with top, down, left and right side of the screen
        if ball_y > 60:
            dy = -0.5
            self.engine.play_sfx("ball_hit")
        if ball_y < 0:
            dy = 0.5
            self.engine.play_sfx("ball_hit")
        if ball_x > 61:
            dx = -0.5
            ball_x = 30
            ball_y = 30
            score -= 1
            self.engine.play_sfx("score")
        if ball_x < 0:
            dx = 0.5
            ball_x = 30
            ball_y = 30
            score += 1
            self.engine.play_sfx("score")

        # collisions with the paddles
        if ball_x > 54 and paddle_y < ball_y < paddle_y + 16:
            dx = -0.5
            self.engine.play_sfx("ball_hit")
        if ball_x < 6 and paddle2_y < ball_y < paddle2_y + 16:
            dx = 0.5
            self.engine.play_sfx("ball_hit")


    # draws the game
    def draw(self):
        # makes the background dark blue
        self.engine.draw_rect_filled(0, 0, 64, 64, (24, 20, 37))
        # draws the score
        self.engine.text(score, 30, 1)
        # draws the paddles and ball
        self.engine.draw("paddle", 58, paddle_y)
        self.engine.draw("paddle", 2, paddle2_y)
        self.engine.draw("ball", ball_x, ball_y)

    def run(self):
        self.engine.pass_down(self.initialize,self.draw,self.update)
        self.engine.run()

app = begin()
app.run()