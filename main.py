import pygame, random

pygame.init()
pygame.mixer.init()


font = pygame.font.SysFont(None, 40)

pygame.mixer.music.load("edm-gaming-music-335408.mp3")
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

car_window_sound = pygame.mixer.Sound("Car-Window-Smash.mp3")
car_window_sound.set_volume(0.5)

car_crash_sound = pygame.mixer.Sound("car_crash_sound.mp3")
car_crash_sound.set_volume(0.5)


screen = pygame.display.set_mode((1200, 800))

def draw_game_over_screen(score, time):
   screen.fill((0, 0, 0))
   title = font.render('Game Over', True, (255, 255, 255))
   score_txt = font.render(f"+score+: {score}", True, (255, 255, 255))
   time_text = font.render(time, True, (255, 255, 255))
   screen.blit(title, (500, 300))
   screen.blit(score_txt, (500, 400))
   screen.blit(time_text, (500, 600))
   pygame.display.update()


pygame.display.set_caption("....speed racers....")
icon  = pygame.image.load("speed_racers.jpg")
pygame.display.set_icon(icon)



background = pygame.image.load("speed_racers_background.jpg")
background_y = 0
speed = 2




car_yellow_img = pygame.image.load("yellow_car.png")
car_yellow_img = pygame.transform.scale(car_yellow_img, (50, 100))
car_yellow_x = 600
car_yellow_y = 650
car_yellow_speed = 0.9


car1_img = pygame.image.load("car1.png")
car1_img = pygame.transform.scale(car1_img, (50, 90))
car1_x = random.randint(390, 770)
car1_y = -100
car1_go = True

car2_img = pygame.image.load("car2.png")
car2_img = pygame.transform.scale(car2_img, (50, 90))
car2_x = random.randint(390, 770)
car2_y = -100
car2_go = False

car3_img = pygame.image.load("car3.png")
car3_img = pygame.transform.scale(car3_img, (50, 90))
car3_x = random.randint(390, 770)
car3_y = -100
car3_go = False

car4_img = pygame.image.load("car4.png")
car4_img = pygame.transform.scale(car4_img, (50, 90))
car4_x = random.randint(390, 770)
car4_y = -100
car4_go = False


ball_img = pygame.image.load("football.png")
ball_img = pygame.transform.scale(ball_img, (20, 20))
ball_x = -20
ball_y = -20
ball_speed = 1.3
ball_active = True

score = 0



running = True
while running:
    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            running = False

    background_y += speed
        
    
    
    if score < 0:
        draw_game_over_screen(score, out)
        pygame.mixer.music.stop()

    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_yellow_x -= car_yellow_speed
        if keys[pygame.K_RIGHT]:
            car_yellow_x += car_yellow_speed
        if keys[pygame.K_SPACE] and ball_active :
            ball_x = car_yellow_x + 15
            ball_y = car_yellow_y
            ball_active = False
        
        if background_y >= 700:
            background_y = 0 

        if car_yellow_x < 390:
            car_yellow_x = 390
        if car_yellow_x > 770:
            car_yellow_x = 770

        
        if car1_go:
            car1_y += 1.6
            if car1_y > 800:
                car1_y = -100
                car1_go = False
                car2_go = True
                
                
        elif car2_y < 800 and car2_go:
            car2_y += 1.6
            if car2_y > 800:
                car2_y = -100
                car2_go = False
                car3_go = True
                
            
        elif car3_y < 800 and car3_go:
            car3_y += 1.6
            if car3_y > 800:
                car3_y = -100
                car3_go = False
                car4_go = True
                
            
        elif car4_y < 800 and car4_go:
            car4_y += 1.6
            if car4_y > 800:
                car4_y = -100
                car4_go = False
                car1_go = True   

        car1_rect = car1_img.get_rect(topleft=(car1_x, car1_y))
        car2_rect = car2_img.get_rect(topleft=(car2_x, car2_y))
        car3_rect = car3_img.get_rect(topleft=(car3_x, car3_y))
        car4_rect = car4_img.get_rect(topleft=(car4_x, car4_y))

        if not ball_active:
            ball_y -= ball_speed
            if ball_y < -20:
                ball_active = True

            ball_rect = ball_img.get_rect(topleft=(ball_x, ball_y))
            if ball_rect.colliderect(car1_rect):
                car_window_sound.play()
                car1_x = random.randint(375, 650)
                car1_y = -100
                ball_active = True
                ball_x, ball_y = -100, -100
                car1_go = False
                car2_go = True
                score += 1
                
            if ball_rect.colliderect(car2_rect):
                car_window_sound.play()
                car2_x = random.randint(375, 650)
                car2_y = -100
                ball_active = True
                ball_x, ball_y = -100, -100
                car2_go = False
                car3_go = True
                score += 1
                
            if ball_rect.colliderect(car3_rect):
                car_window_sound.play()
                car3_x = random.randint(375, 650)
                car3_y = -100
                ball_active = True
                ball_x, ball_y = -100, -100
                car3_go = False
                car4_go = True
                score += 1

            if ball_rect.colliderect(car4_rect):
                car_window_sound.play()
                car4_x = random.randint(375, 650)
                car4_y = -100
                ball_active = True
                ball_x, ball_y = -100, -100
                car4_go = False
                car1_go = True
                score += 1
                
        car_yellow_rect = car_yellow_img.get_rect(topleft=(car_yellow_x, car_yellow_y))    
        if car_yellow_rect.colliderect(car1_rect):
            car_crash_sound.play()
            car1_x = random.randint(350, 650)
            car1_y = -100
            ball_active = True
            ball_x, ball_y = -100, -100
            car1_go = False
            car2_go = True
            score -= 1

        if car_yellow_rect.colliderect(car2_rect):
            car_crash_sound.play()
            car2_x = random.randint(350, 650)
            car2_y = -100
            ball_active = True
            ball_x, ball_y = -100, -100
            car2_go = False
            car3_go = True
            score -= 1

        if car_yellow_rect.colliderect(car3_rect):
            car_crash_sound.play()
            car3_x = random.randint(350, 650)
            car3_y = -100
            ball_active = True
            ball_x, ball_y = -100, -100
            car3_go = False
            car4_go = True
            score -= 1

        if car_yellow_rect.colliderect(car4_rect):
            car_crash_sound.play()
            car4_x = random.randint(350, 650)
            car4_y = -100
            ball_active = True
            ball_x, ball_y = -100, -100
            car4_go = False
            car1_go = True
            score -= 1

        score_txt = font.render(f"+score+: {score}", True, (255, 255, 255))
        ticks = pygame.time.get_ticks()
        millis = ticks % 1000
        seconds = int(ticks/1000 % 60)
        minutes = int(ticks/60000 % 24)
        out ='{minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)
        time = font.render(out, True, (255, 255, 255))
        
        
        background = pygame.image.load("speed_racers_background.jpg")
        background = pygame.transform.scale(background, (1200, 800))
        screen.blit(background, (0, 0))
        screen.blit(background, (0, background_y))
        screen.blit(background, (0, background_y - 700))
        screen.blit(car_yellow_img, (car_yellow_x, car_yellow_y))
        screen.blit(score_txt, (1000, 10))
        screen.blit(time, (1000, 40))
        screen.blit(car1_img, (car1_x, car1_y))
        screen.blit(car2_img, (car2_x, car2_y))
        screen.blit(car3_img, (car3_x, car3_y))
        screen.blit(car4_img, (car4_x, car4_y))
        screen.blit(ball_img, (ball_x, ball_y))
        pygame.display.update()