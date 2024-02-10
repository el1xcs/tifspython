
import pygame
import random



pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golden Dash")


BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


player_size = 50
player_color = WHITE
player_speed = 5


collectible_size = 20

# Scor
font = pygame.font.Font(None, 36)

def reset_game():
    global player_x, player_y, objects, score, running
    player_x = WIDTH // 2 - player_size // 2
    player_y = HEIGHT - player_size * 2
    objects = []  # Resetarea listei de obiecte
    score = 0
    running = True
    
def message (msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT/3])

def draw_player(x, y):
    pygame.draw.rect(screen, player_color, (x, y, player_size, player_size))

def generate_object():
    x = random.randint(0, WIDTH - collectible_size)
    y = 0
    obj_type = "gold" if random.randint(0, 1) == 0 else "red"
    objects.append([x, y, obj_type])

def move_objects():
    global score, running
    for obj in objects[:]:
        obj[1] += 1  
        if player_x < obj[0] < player_x + player_size and player_y < obj[1] < player_y + player_size:
            if obj[2] == "gold":
                score += 1
                objects.remove(obj)
            else:
                running = False  
        pygame.draw.rect(screen, GOLD if obj[2] == "gold" else RED, (obj[0], obj[1], collectible_size, collectible_size))


reset_game()


while True:
    if running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Aici la miscare am pus doar stanga drepta(imi place mai tare asa)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed


     
        if random.randint(1, 20) == 1:
            generate_object()
        move_objects()

        draw_player(player_x, player_y)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        pygame.time.Clock().tick(60)
    else:
       while running==False:
            screen.fill(WHITE)
            message ("Ai pierdut! Pentru a restarta apasa tasta 'r' sau 'q' pentru a iesi ", RED)
            pygame.display.update()
            for event in pygame.event.get():
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    pygame.quit()
                    game_close = False
                if event.key == pygame.K_r:
                    reset_game()
 