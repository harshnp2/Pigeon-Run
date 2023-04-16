import pygame
import math
import random




# initialize the game
pygame.init()

# create the screen
SCREEN_WIDTH = 900
screen = pygame.display.set_mode((900, 555))

# set the FPS
clock = pygame.time.Clock()
FPS = 60

# background
background = pygame.image.load("background.jpg").convert()
# change size of background image
# background = pygame.transform.scale(background)
bg_width = background.get_width()

# define scrolling background variables
global scroll
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
scroll_change = 2

# Player
player_image = pygame.image.load("Airplane.png")
player_image = pygame.transform.scale(player_image, (234, 78))
playerX = 40
playerY = 33
playerY_change = 2
pos_state = 1
moving = ''


# bird
bird_image = []
birdX = []
birdY = []
birdX_change = 1
global num_birds
num_birds = 1
OG_score = 0
birdY_list = [40, 220, 400]
Y_spots_taken = []
birds_left = 0


bird_animation = [pygame.image.load("bird_1.png"),
                  pygame.image.load("bird_2.png"),
                  pygame.image.load("bird_3.png"),
                  pygame.image.load("bird_4.png"),
                  pygame.image.load("bird_5.png"),
                  pygame.image.load("bird_4.png"),
                  pygame.image.load("bird_3.png"),
                  pygame.image.load("bird_2.png")]

for b in range(num_birds):
    bird_image.append(bird_animation)
    birdX.append(900)
    Y_spot = random.choice(birdY_list)
    birdY.append(Y_spot)
    Y_spots_taken.append(Y_spot)
    birdY_list.remove(Y_spot)

value = 0

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 700
textY = 500
score_given = False
reached100 = False

# game over
game_over_background = pygame.image.load("sddefault.jpg").convert()
game_over_background = pygame.transform.scale(game_over_background, (900, 555))

# asl recognition variables
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letter_given = False
letter = ""
letters_assigned = []



# for loop variables
range_number = 500
first_round = True
gone_through = False
once = True
time = 11




def player(x, y):
    screen.blit(player_image, (x, y))

def bird(bird_image, x, y, value, i):
    # animate the bird
    if value >= len(bird_image[i]):
        value = 0

    bird_frame = 0

    bird_movement_list = bird_image[i]
    if isinstance(value, int) == True:
        bird_frame = bird_movement_list[value]
        screen.blit(bird_frame, (x, y))

    else:
        if value < 1:
            bird_frame = bird_movement_list[0]
        elif value < 2:
            bird_frame = bird_movement_list[1]
        elif value < 3:
            bird_frame = bird_movement_list[2]
        elif value < 4:
            bird_frame = bird_movement_list[3]
        elif value < 5:
            bird_frame = bird_movement_list[4]
        elif value < 6:
            bird_frame = bird_movement_list[5]
        elif value < 7:
            bird_frame = bird_movement_list[6]
        elif value < 8:
            bird_frame = bird_movement_list[7]

        screen.blit(bird_frame, (x, y))
        x -= birdX_change

    value += 0.25

    return value

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))




running = True
while True:

    if first_round != True:
        print('hi')
        range_number = 900
    if first_round == True:
        range_number = 500
        first_round = False

    for i in range(0, range_number):
        clock.tick(FPS)

        if i == range_number - 1:
            if playerY <= 33:
                moving = 'down'
                assigned_letters = random.sample(alphabet, k=1)
                print(f'Sign {assigned_letters[0]} to move {moving}')
                pos_state = 1

            elif playerY >= 450:
                print(playerY)
                moving = 'up'
                assigned_letters = random.sample(alphabet, k=1)
                print(f'Sign {assigned_letters[0]} to move {moving}')
                pos_state = 1

            elif 33 < playerY < 450:
                assigned_letters = random.sample(alphabet, k=2)
                print(f'Sign {assigned_letters[0]} to move down')
                print(f'Sign {assigned_letters[1]} to move up')
                pos_state = 2

        screen.fill((0, 0, 0))

        for i in range(0, tiles):
            screen.blit(background, (i * bg_width + scroll, 0))

        # scroll background
        scroll -= scroll_change
        # reset scroll
        if abs(scroll) > bg_width:
            scroll = 0

        for i in range(0, num_birds):
            value = bird(bird_image, birdX[i], birdY[i], value, i)
            birdX[i] -= birdX_change

            # score increase
            if birdX[i] + 105 <= 0 and score_given == False:
                birds_left += 1
                score_value += 10
                birdX[i] = 900
                birdY = random.sample(birdY_list, k = 2)

                score_given == True
                value = bird(bird_image, birdX[i], birdY[i], value, i)

            # collision
            if 0 < birdX[i] <= 274 and playerY + 7 == birdY[i]:
                while True:
                    screen.blit(game_over_background, (0, 0))
                    pygame.display.update()
                    while True:
                        pass






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if letter != "":
            if gone_through == False:
                print(letter)
                gone_through = True
                if letter == letters_assigned[0] and moving == 'down':
                    print(playerY)
                    print('a')
                    for i in range(0, 90):
                        clock.tick(FPS)
                        for i in range(0, tiles):
                            screen.blit(background, (i * bg_width + scroll, 0))

                        # scroll background
                        scroll -= scroll_change
                        # reset scroll
                        if abs(scroll) > bg_width:
                            scroll = 0

                        for i in range(0, num_birds):

                            value = bird(bird_image, birdX[i], birdY[i], value, i)
                            birdX[i] -= birdX_change

                            # score increase
                            if birdX[i] + 105 <= 0 and score_given == False:
                                birds_left += 1
                                score_value += 10
                                birdX[i] = 900
                                birdY = random.sample(birdY_list, k=2)

                                score_given == True
                                value = bird(bird_image, birdX[i], birdY[i], value, i)

                            # collision
                            if 0 < birdX[i]<= 274 and playerY + 7 == birdY[i]:
                                while True:
                                    screen.blit(game_over_background, (0, 0))
                                    pygame.display.update()
                                    while True:
                                        pass


                        playerY += playerY_change
                        print(playerY)
                        player(playerX, playerY)
                        show_score(textX, textY)
                        pygame.display.update()
                if (letter == letters_assigned[0] or letter == letters_assigned[1]) and moving == 'up':
                    print(playerY)
                    print('b')
                    for i in range(0, 90):
                        clock.tick(FPS)
                        for i in range(0, tiles):
                            screen.blit(background, (i * bg_width + scroll, 0))

                        # scroll background
                        scroll -= scroll_change
                        # reset scroll
                        if abs(scroll) > bg_width:
                            scroll = 0

                        for i in range(0, num_birds):

                            value = bird(bird_image, birdX[i], birdY[i], value, i)
                            birdX[i] -= birdX_change
                            # score increase
                            if birdX[i] + 105 <= 0 and score_given == False:
                                birds_left += 1
                                score_value += 10
                                birdX[i] = 900
                                birdY = random.sample(birdY_list, k=2)

                                score_given == True
                                value = bird(bird_image, birdX[i], birdY[i], value, i)

                                birdY_list = [40, 220, 400]

                            # collision
                            if 0 < birdX[i]<= 274 and playerY + 7 == birdY[i]:
                                screen.blit(game_over_background, (0, 0))
                                pygame.display.update()
                                while True:
                                    pass

                        playerY -= playerY_change
                        player(playerX, playerY)
                        show_score(textX, textY)
                        pygame.display.update()

                else:
                    pass

        if score_value == 100 and reached100 == False:
            birds_left = 0
            num_birds = 2
            bird_image.append(bird_animation)
            birdX.append(600)
            birdY = random.sample(birdY_list, k = 2)

            birdY_list = [40, 220, 400]

            reached100 = True


            birdY_list = [40, 220, 400]

        if birds_left == 10 and score_value != 100:
            birds_left = 0
            time -= 1

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()

    from asl_detection import detect_letter
    letter, letters_assigned, gone_through, moving = detect_letter(assigned_letters, gone_through, pos_state, moving, playerY, time)

