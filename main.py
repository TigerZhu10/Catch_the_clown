import pygame
import random

pygame.init()


WINDOW_WIDTH = 800 #x
WINDOW_HEIGHT = 400 #y

score = 0
lives = 5
FPS = 30
clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown!")

back_music = pygame.mixer.Sound('ctc_background_music.wav')
miss_music = pygame.mixer.Sound('miss_sound.wav')
hit_music = pygame.mixer.Sound('click_sound.wav')
back_music.play(-1)

back_ground = pygame.image.load("background.png")
back_ground = pygame.transform.scale(back_ground, (WINDOW_WIDTH, WINDOW_HEIGHT))

title_font = pygame.font.Font('Franxurter.ttf',23)
score_font = pygame.font.Font('Franxurter.ttf',23)
lives_font = pygame.font.Font('Franxurter.ttf',23)
reset_font = pygame.font.Font('Franxurter.ttf',45)
restart_font = pygame.font.Font('Franxurter.ttf',45)

reset_text = reset_font.render("Game Over!", True, (40, 55, 59))
reset_text_rect = reset_text.get_rect()
reset_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

restart_text = restart_font.render("Click Anywhere to Restart!", True, (40, 55, 59))
restart_text_rect = restart_text.get_rect()
restart_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50)

title_text = title_font.render("Catch the Clown!", True, (14,193,237))
title_text_rect = title_text.get_rect()
title_text_rect.topleft = (0 + 30, 0 + 10)

score_text = score_font.render("Score: " + str(score), True, (239,247,5))
score_text_rect = score_text.get_rect()
score_text_rect.topright = (WINDOW_WIDTH - 25, 0 + 10)

lives_text = lives_font.render("Lives: " + str(lives), True, (239,247,5))
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_WIDTH - 25, 0 + 35)

clown_image = pygame.image.load("clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)


clown_speed = 5
clown_direction = random.choice([1,-1])
clown_speed = clown_speed * clown_direction

dx = clown_speed
dy = clown_speed

Choice = random.choice([1,0])

game_running = True
while game_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_running = False

        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            if clown_rect.collidepoint(ev.pos):
                hit_music.play(0)
                score += 1
                score_text = score_font.render("Score: " + str(score), True, (239,247,5))
                dx = dx + 2 if dx > 0 else dx - 2
                dy = dy + 2 if dy > 0 else dy - 2

            else:
                miss_music.play(0)
                lives -= 1
                lives_text = lives_font.render("Lives: " + str(lives), True, (239,247,5))
                if lives <= 0:
                    back_music.stop()
                    pause = True
                    while pause:
                        display_surface.blit(reset_text, reset_text_rect)
                        display_surface.blit(restart_text, restart_text_rect)
                        for ev in pygame.event.get():
                            if ev.type == pygame.MOUSEBUTTONDOWN:
                                back_music.play(-1)
                                clown_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2)
                                dx = 5
                                dy = 5
                                score = 0
                                lives = 5
                                score_text = score_font.render("Score: " + str(score), True, (239,247,5))
                                lives_text = lives_font.render("Lives: " + str(lives), True, (239,247,5))
                                pause = False
                            if ev.type == pygame.QUIT:
                                game_running = False
                                pause = False 

                        pygame.display.update()


    clown_rect.x += dx

    if Choice == 1:
        clown_rect.y += dy
    else:
        clown_rect.y -= dy
        

    if clown_rect.right >= WINDOW_WIDTH:
        dx = -dx
    if clown_rect.bottom >= WINDOW_HEIGHT:
        dy = -dy
    if clown_rect.left <= 0:
        dx = -dx
    if clown_rect.top <= 0:
        dy = -dy


    display_surface.blit(back_ground, (0, 0)) #背景图片
    display_surface.blit(title_text, title_text_rect) #title
    display_surface.blit(score_text, score_text_rect) #积分
    display_surface.blit(lives_text, lives_text_rect) #生命
    display_surface.blit(clown_image, clown_rect) #clown
     

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()