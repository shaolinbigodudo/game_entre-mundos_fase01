import pygame
import pygame.display 

# Inicializaçao do paygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Entre Mundos (dev)')
fps = pygame.time.Clock()

# Cores

WHITE = (255, 255, 255)
BLACK = (0,0,0)
CRIMSON = (220,20,60)
P1 = (0, 0, 255)
P2 = (255, 0, 0)

#Funçoes
def menu_principal():
    # Loop do menu principal 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Atualiza a posiçao do mouse
                mouse = pygame.mouse.get_pos()

                # Verificar se o clique foi em 'Novo Jogo'
                if 100 <= mouse[0] <= 200 and 300 <= mouse[1] <= 400:
                    selecao_personagem()
        # Desenhar o menu
        screen.fill(BLACK)
        font = pygame.font.Font(None,36)
        text = font.render('Novo jogo', True, CRIMSON)
        screen.blit(text, (100, 300))

        pygame.display.flip()
        fps.tick(60)

def selecao_personagem():
    # Loop da tela de seleçao
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #desenhar a tela de seleçao
        screen.fill(BLACK)
        pygame.draw.rect(screen, P1, (100, 200, 50, 50))
        pygame.draw.rect(screen, P2, (300, 200, 50, 50))

        #EXIBIR A TELA DE SELEÇAO
        pygame.display.flip()
        fps.tick(60)
# Chamar o menu principal
menu_principal()
