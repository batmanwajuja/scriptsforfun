#modules

from pygame import *
from random import choice
import sys

#game class

class PongGame:
#const game vars
	WIDTH, HEIGHT = 800, 600
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	PADDLE_SPEED = 5
	PADDLE_WIDTH = 15
	PADDLE_HEIGHT = 100
	BALL_RADIUS = 15
	BALL_SPEED_X = 5
	BALL_SPEED_Y = 5


# initialize pygame w/ game vars

	def __init__(self):
#game settings
		font.init()
		mixer.init()

		self.screen = display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = time.Clock()
		display.set_caption("pypong v0.1")
		mixer.music.load("background.mp3")
		mixer.music.play(-1)
# game vars
		self.player1 = [50, (self.HEIGHT - self.PADDLE_HEIGHT)/2]
		self.player2 = [self.WIDTH - 50 - self.PADDLE_WIDTH, (self.HEIGHT - self.PADDLE_HEIGHT)/2]
		self.ball_pos = [self.WIDTH//3, self.HEIGHT//2]
		self.ball_speed = [self.BALL_SPEED_X, self.BALL_SPEED_Y]
		self.p1_score = 0
		self.p2_score = 0
		self.font = font.Font(None,45)

#make paddle
	def paddle(self,pos):
		draw.rect(self.screen, self.WHITE,(pos[0], pos[1], self.PADDLE_WIDTH, self.PADDLE_HEIGHT))
#make ball
	def ball(self,pos):
		draw.circle(self.screen,self.WHITE,pos,self.BALL_RADIUS)
#collision
	def hit_paddle(self,ball_pos,paddle_pos) -> bool:
		return(paddle_pos[0]< ball_pos[0]<paddle_pos[0] + self.PADDLE_WIDTH) and (paddle_pos[1]< ball_pos[1]<paddle_pos[1] + self.PADDLE_WIDTH)

#move ball
	def update_ball(self):
		self.ball_pos[0] += self.ball_speed[0]
		self.ball_pos[1] += self.ball_speed[1]

		if self.ball_pos[1] - self.BALL_RADIUS <= 0 or self.ball_pos[1]+ self.BALL_RADIUS >= self.HEIGHT - self.BALL_RADIUS:
			self.ball_speed[1] = -self.ball_speed[1]
		if self.hit_paddle(self.ball_pos,self.player1) or self.hit_paddle(self.ball_pos,self.player2):
			self.ball_speed[0] = -self.ball_speed[0]

		if self.ball_pos[0] <= 0:
			self.p2_score += 1
			self.reset()

		if self.ball_pos[0] >= self.WIDTH:
			self.p1_score += 1
			self.reset()


#reset game
	def reset(self):
		self.ball_pos = [self.WIDTH//2, self.HEIGHT//2]
		random_direction = choice([-1,1])
		self.ball_speed = [self.BALL_SPEED_X * random_direction, self.BALL_SPEED_Y]
#RUN GAME
	def run_game(self):
		run = True
		while run:
			for e in event.get():
				if e.type == QUIT:
					run = False
					sys.exit()
			keys = key.get_pressed()
			if keys[K_w] and self.player1[1] > 0:
				self.player1[1] -= self.PADDLE_SPEED
			elif keys[K_s] and self.player1[1] < self.HEIGHT - self.PADDLE_HEIGHT:
				self.player1[1] += self.PADDLE_SPEED
			if keys[K_UP] and self.player2[1] > 0:
				self.player2[1] -= self.PADDLE_SPEED
			elif keys[K_DOWN] and self.player2[1] < self.HEIGHT - self.PADDLE_HEIGHT:
				self.player2[1] += self.PADDLE_SPEED




			self.update_ball()
			self.screen.fill(self.BLACK)
			self.paddle(self.player1)
			self.paddle(self.player2)
			self.ball(self.ball_pos)

			p1_text = self.font.render(str(self.p1_score), True, self.WHITE)
			p2_text = self.font.render(str(self.p2_score), True, self.WHITE)

			self.screen.blit(p1_text,(self.WIDTH/4, 20))
			self.screen.blit(p2_text,(self.WIDTH* 3/4,20))

#wining condition
			if self.p1_score >= 5 or self.p2_score >= 5:
				run = False
#add wining screen??? add user sliders for speed, and other features

			display.update()
			self.clock.tick(30)

if __name__ == "__main__":
	game = PongGame()
	game.run_game()
