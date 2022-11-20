import pygame
import random
import time
pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Sonic")
altura = 520
largura = 1000
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
fundo = pygame.image.load("assets/fundoSonic.png")
sonic = pygame.image.load("assets/sonic.jpg")
moeda = pygame.image.load("assets/moedaSonic.png")




def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    gameDisplay.blit(textoDisplay, (880,80))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",80)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("PERDEU !!!!",True,branco)
    textoDisplay2 = fonte2.render("Aperte Enter Para Continuar !!!!",True,branco)
    gameDisplay.blit(textoDisplay, (150,150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    sonicX = 500
    sonicY = 400
    movimentosonicX = 0
    largurasonic = 120
    alturasonic = 40
    alturamoeda = 40
    larguramoeda = 60
    posicaomoedaX = 400
    posicaomoedaY = -240
    velocidademoeda = 3
    pontos = 0

    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentosonicX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentosonicX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentosonicX = 0
            
        if jogando:
            if posicaomoedaY > altura:
                posicaomoedaY = -240
                posicaomoedaX = random.randint(0,largura)
                velocidademoeda = velocidademoeda + 1
                pontos = pontos + 1
            
            else:
                posicaomoedaY =posicaomoedaY + velocidademoeda

            if sonicX + movimentosonicX >0 and sonicX + movimentosonicX< largura-largurasonic:
                sonicX = sonicX + movimentosonicX
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(sonic, (sonicX,sonicY))
            
            gameDisplay.blit(moeda, (posicaomoedaX,posicaomoedaY))
            escreverTexto("Pontos: "+str(pontos))

            pixelsXsonic = list(range(sonicX, sonicX+largurasonic))
            pixelsYsonic = list(range(sonicY, sonicY+alturasonic))

            pixelXmoeda = list(range(posicaomoedaX, posicaomoedaX+larguramoeda))
            pixelYmoeda = list(range(posicaomoedaY, posicaomoedaY+alturamoeda))

            colisaoY = len(list(set(pixelYmoeda) & set(pixelsYsonic) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXmoeda) & set(pixelsXsonic) ))
                print(colisaoX)
                if colisaoX > 20:
                    morreu()
                    jogando=False


        pygameDisplay.update()
        clock.tick(60)

jogar()