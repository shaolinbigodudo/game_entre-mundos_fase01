import pygame
from os import listdir
from os.path import join, isfile

# Inicialização do Pygame
WIDTH , HEIGHT = 1000 , 800
pygame.init()
SCREEN= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Entre Mundos (dev)')
FPS = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CRIMSON = (220,20,60)
P1 = (0, 0, 255)
P2 = (255, 0, 0)

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join('assets', dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

# Funções

def get_background(name):

    image = pygame.image.load(join('assets', 'Background', name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT   // height + 1):
            pos = (i * width, j * height )
            tiles.append(pos)

    return tiles, image

def draw(background, bg_image):
    for tile in background:
        SCREEN.blit(bg_image, tile)
    
    pygame.display.update()

def menu_principal():
    # Loop do Menu Principal
    running = True
    while running:
        background, bg_image = get_background('Pink.png')
        PLAYER = load_sprite_sheets('Characters', 'PinkMan', 32, 32, True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Atualiza a posição do mouse
                mouse = pygame.mouse.get_pos()

                # Verificar se o clique foi em 'Novo Jogo'
                if 100 <= mouse[0] <= 200 and 300 <= mouse[1] <= 400:
                    selecao_personagem()

        # Desenhar o menu
        # screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        text = font.render('Novo Jogo', True, CRIMSON)
        SCREEN.blit(text, (100, 300))

        pygame.display.flip()
        #FPS.tick(60)
        draw(background, bg_image)

def selecao_personagem():
    # Loop da tela de seleção
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Desenhar a Tela de Seleção
        SCREEN.fill(BLACK)
        pygame.draw.rect(SCREEN, P1, (100, 200, 50, 50))
        pygame.draw.rect(SCREEN, P2, (300, 200, 50, 50))

        # Exibir a Tela de Seleção
        pygame.display.flip()
        FPS.tick(60)
        

# Chamar o Menu Principal
menu_principal()