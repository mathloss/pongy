import pygame, sys
import random

# Pygame init
pygame.init()
clock = pygame.time.Clock()

# setup the screen
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pongy")
icon = pygame.image.load("C:/Users/eriol/Desktop/pongy/pong.png")
pygame.display.set_icon(icon)


# Game stuff
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player_1 = pygame.Rect(10,screen_height/2 - 70, 10, 140)
player_2 = pygame.Rect(1260,screen_height/2 - 70, 10, 140)
mid = pygame.Rect(637 ,0, 6, 960)

# Colors
my_grey = (220, 220, 220)

# ball animation
ball_speed_x = 7
ball_speed_y = 7

# players animation
player_1_speed = 0
player_2_speed = 0

# Score & countdown
player_1_score = 0
player_2_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

# Sounds
bounce = pygame.mixer.Sound("C:/Users/eriol/Desktop/pongy/bounce.ogg")
and1 = pygame.mixer.Sound("C:/Users/eriol/Desktop/pongy/and1.ogg")

##########################################       FONCTIONS           ######################################################
def ball_start():
	global ball_speed_x, ball_speed_y

	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))

def ball_animation():
    global ball_speed_x, ball_speed_y, player_1_score, player_2_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y
 
    # Collision
    if ball.top <=0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(bounce)
        ball_speed_y *= -1

    if ball.left <=0 :        
        ball_start()
        player_1_score += 1
        pygame.mixer.Sound.play(and1)

    if ball.right >=screen_width :              
        ball_start()
        player_2_score += 1
        pygame.mixer.Sound.play(and1)

    if ball.colliderect(player_1) and ball_speed_x < 0:
        if abs(ball.right - player_1.left) > 10:
            ball_speed_x *= -1
            pygame.mixer.Sound.play(bounce)
        elif abs(ball.bottom - player_1.top) > 10 and ball_speed_y < 0:
            ball_speed_x *= -1
            pygame.mixer.Sound.play(bounce)
        elif abs(ball.top - player_1.bottom) < 10 and ball_speed_y > 0:
            ball_speed_x *= -1
            pygame.mixer.Sound.play(bounce)


    if ball.colliderect(player_2) and ball_speed_x > 0:
        if abs(ball.left - player_2.right) > 10:
            ball_speed_x *= -1
            pygame.mixer.Sound.play(bounce)
        elif abs(ball.bottom - player_2.top) > 10 and ball_speed_y > 0:
            ball_speed_x *= -1
            pygame.mixer.Sound.play(bounce)
        elif abs(ball.top - player_2.bottom) < 10 and ball_speed_y < 0:
            ball_speed_x *= -1
            pygame.mixer.Sound.play(bounce)

# game loop
while True:
    # color screen / couleur de l'ecran
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_1_speed -= 7
            if event.key == pygame.K_q:
                player_1_speed += 7
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_1_speed += 7
            if event.key == pygame.K_q:
                player_1_speed -= 7

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_2_speed -= 7
            if event.key == pygame.K_DOWN:
                player_2_speed += 7
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_2_speed += 7
            if event.key == pygame.K_DOWN:
                player_2_speed -= 7
    ball_animation()

    player_1.y += player_1_speed
    player_2.y += player_2_speed

    # limits of the screen
    if player_1.top <= 0:
        player_1.top = 0
    if player_1.bottom >= screen_height:
        player_1.bottom = screen_height
    
    if player_2.top <= 0:
        player_2.top = 0
    if player_2.bottom >= screen_height:
        player_2.bottom = screen_height


    # Drawing game stuff
    pygame.draw.rect(screen, "white", player_1)
    pygame.draw.rect(screen, "white", player_2)
    pygame.draw.rect(screen, my_grey, mid)
    pygame.draw.ellipse(screen, "white", ball)

    player_1_text = game_font.render(f"{player_1_score}", True, my_grey)
    screen.blit(player_1_text, (660, 470))
    player_2_text = game_font.render(f"{player_2_score}", True, my_grey)
    screen.blit(player_2_text, (600, 470))

    

    pygame.display.flip()
    clock.tick(60)