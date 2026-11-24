import pygame
pygame.init()
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space invaders")

FUNDO = (0, 0, 0)
VERDE = (100, 255, 100)
TAMANHO_PIXEL = 20

alien = [
    "111111111111111",
    "100001000100001",
    "100000111000001",
    "1000111111100001",
    "100111010111001",
    "100101111010001",
    "000010000001000"
    "100000101000001",
    "111111111111111"

]

posicao_x = 5
posicao_y = 7
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((20, 20, 30))
    tela.blit(mensagem, (posicao_x, posicao_y))
    pygame.display.update()
pygame.quit()