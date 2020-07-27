import pygame

width,height = 1024,768
window = pygame.display.set_mode((width,height), pygame.RESIZABLE)

files = ['Hi There', 'Test', 'Old', 'New', 'Creative', 'What', 'FBI', 'Really?']

boxWidth = int((width-20)/6)
boxHeight = int((height-90)/3)

row = 1
rowItem = []

saveBox = []
"""for i in range(len(files)):
    if i % 5 == True and i != 1: # 5 IS ACTUALLY SIX!!! | DONT FORGET IT STARTS FROM 0 NOT 1 SO 5+1 IS 6
        ybox += boxHeight+15
        row = True
    if row == False:
        saveBox.append((10+(15+boxWidth)*i,ybox))
    else:
        saveBox.append()"""

"""for x in range(len(files)):
    saveBox.append([10+(15+boxWidth)*x,0])

for y in range(len(saveBox)):
    if y % 5 == True and y != 1:
        row += 1
    if row == 1:
        saveBox[y][1] = 90
    else:
        saveBox[y][1] = (15+boxHeight)*row
    if saveBox[y][1] != saveBox[y-1][1]:
        # NEW ROW DETECTED RESET X
        rowItem = saveBox[y]
    if rowItem[1] == saveBox[y][1]:
        saveBox[y][0] = saveBox[y][0]-10-(15-boxWidth)/(y+1) # REVERSE ENGINEER X FORMULA"""

ybox = 90
for y in range(len(files)):
    ybox += 45
    saveBox.append([10,ybox])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)
            width,height = event.w, event.h
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ybox > 90 and ybox < height:
                if event.button == 4:
                    for scroll in saveBox:
                        scroll[1] += 45
                if event.button == 5:
                    for scroll in saveBox:
                        scroll[1] -= 45
    window.fill((0,0,255))

    for box in saveBox:
        if box[1] > 90 and box[1] < height:
            pygame.draw.rect(window, (128,128,128), (box[0],box[1],width-60,30))



    """for i in range(len(files)):
        pygame.draw.rect(window, (128,128,128), (10+(15+boxWidth)*i,90+(iHeight*boxHeight),boxWidth,boxHeight))
        if int(i) / 6 == 1.0:
            iHeight += 1
            print(iHeight)"""




    """for x in range(len(files)):
        for y in range(len(files)):
            if y % 6 == True:
                pygame.draw.rect(window, (128,128,128), (10+(15+boxWidth)*x),)
            pygame.draw.rect(window, (128,128,128), (10+(15+boxWidth)*x,90,boxWidth,boxHeight))"""


    for i in range(len(files)):
        if i == 0:
            pygame.draw.rect(window, (128,128,128), (10,y,width-60,40))
        else:
            y += 55
            pygame.draw.rect(window, (128,128,128), (10,y,width-60,40))
        




    pygame.display.flip()