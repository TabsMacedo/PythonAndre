import pygame, random, time
from pygame.locals import *

# Inicialização da biblioteca
pygame.init()

# Interface
screen_size = (600, 600)  # Renomeado para 'screen_size'
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Jogo da Cobrinha')

# Cores
vermelho = (255, 0, 0)
branco = (255, 255, 255)  # Definindo a cor branca

# Direções da cobra
esquerda = K_LEFT
direita = K_RIGHT
cima = K_UP
baixo = K_DOWN

# Variável de quando a cobrinha vai se movimentar
passo = 10

# Criação das variáveis
snake = [(200, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill(branco)
snake_dir = baixo

# Função para gerar a posição da maçã
def gerar_posicao_maca():
    while True:
        nova_posicao = (random.randint(0, (screen_size[0] // 10) - 1) * 10,
                        random.randint(0, (screen_size[1] // 10) - 1) * 10)
        if nova_posicao not in snake:
            return nova_posicao

# Função para verificar colisão com as bordas
def colidir_parede(posicao_cabeca):
    if (posicao_cabeca[0] < 0 or posicao_cabeca[0] >= screen_size[0] or
        posicao_cabeca[1] < 0 or posicao_cabeca[1] >= screen_size[1]):
        return True
    return False

# Função para exibir o game over
def exibir_game_over():
    fonte = pygame.font.SysFont('Arial', 48)
    mensagem = fonte.render('Game Over', True, vermelho)
    screen.blit(mensagem, (screen_size[0] // 3, screen_size[1] // 3))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    exit()

# Gerar a posição inicial da maçã
maca_pos = gerar_posicao_maca()

# Jogo principal
while True:
    screen.fill((0, 0, 0))
    pygame.time.Clock().tick(10)

    # Verificar os eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key in [cima, baixo, esquerda, direita]:
                snake_dir = event.key

    # Movimento da cobrinha
    if snake_dir == cima:
        nova_posicao = (snake[0][0], snake[0][1] - passo)
    elif snake_dir == baixo:
        nova_posicao = (snake[0][0], snake[0][1] + passo)
    elif snake_dir == esquerda:
        nova_posicao = (snake[0][0] - passo, snake[0][1])
    elif snake_dir == direita:
        nova_posicao = (snake[0][0] + passo, snake[0][1])

    # Verificar colisão com as bordas
    if colidir_parede(snake[0]):  # Corrigido para usar a posição atual da cabeça da cobra
        exibir_game_over()

    # Adicionar nova posição da cabeça da cobra
    snake.insert(0, nova_posicao)

    if snake[0] == maca_pos:
        maca_pos = gerar_posicao_maca()
    else:
        snake.pop()

    # Desenhar a cobra
    for pos in snake:
        screen.blit(snake_skin, pos)

    # Desenhar a maçã como um quadrado vermelho
    maca_tamanho = pygame.Surface((10, 10))
    maca_tamanho.fill(vermelho)
    screen.blit(maca_tamanho, maca_pos)  # Desenho da maçã como um quadrado

    pygame.display.update()
