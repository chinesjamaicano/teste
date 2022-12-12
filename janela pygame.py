import sys, pygame
pygame.init()

WHITE = (255, 255, 255)
janela=pygame.display.set_mode((1300,700))

objeto1=pygame.Rect(300,150,100,100)

x=300
y=150

objeto1=pygame.Rect(x,y,100,100)

pygame.draw.rect(janela,WHITE,objeto1)

run = True

while run == True:
	
    objeto1=pygame.Rect(x,y,100,100)
    imagem=pygame.image.load("40b6768847e6bb5c68cc13ed2fe314b68f633359f7260e1ff5ad4141d0019900_1.jpg")
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: 
                      x = x  + 100
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
	                  x = x  - 100
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
	                  y = y  + 100
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
	                  y = y  - 100 

        if event.type == pygame.QUIT:
            run = False

    janela.fill((0, 0, 0))
    pygame.draw.rect(janela,WHITE,objeto1)

    janela.blit(imagem,objeto1)
    pygame.display.update()





