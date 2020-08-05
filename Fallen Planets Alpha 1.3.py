import pygame, os
from datetime import datetime

BASE_DIR = os.getcwd()

user = ''

colours = {"Sky_blue": (116,187,251), 'Steel_gray': (67,70,75), 'Azure': (240,255,255)}

class GUI:

    def text(x, y, font, size, msg, colour, surf):
        font = pygame.font.SysFont(font, size)
        text = font.render(msg, True, colour)
        textRect = text.get_rect()
        textRect.center = (x,y)
        surf.blit(text, textRect)

    def form(self,x,y,w,h,font,textSize,text,undefinedText,bgColor,fgColor,activeForm,surf,key,cursor=True): #REMOVE CURSOR FUNCTIONALITY THIS SEEMS UNLIKELY AS YOU NEED TO RELY ON THE EVENT QUE TOO MUCH FOR THIS TO WORK!!!
        mouse,click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        if cursor == True:
            pygame.draw.rect(surf, bgColor, (x,y,w,h))
            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                if click[0] == 1 and activeForm == False:
                    activeForm = True
            if x+w < mouse[0] < x and y+h < mouse[1] < y:
                if click[0] == 1 and activeForm == True:
                    activeForm = False
        if activeForm == False:
            if undefinedText == '':
                self.text(x+50,y+15,font,textSize, text, fgColor, surf)
            else:
                self.text(x+50,y+15,font,textSize, undefinedText, fgColor, surf)
        else:
            if key == 'return':
                if undefinedText != '':
                    key = 'form filled'
                activeForm = False
            elif key == 'backspace':
                if undefinedText != '':
                    undefinedText = undefinedText.strip(undefinedText[-1])
                    key = ''
            elif len(key) == 1:
                undefinedText += key
                key = ''
            self.text(x+50,y+15,font,textSize, undefinedText, fgColor, surf)
        return key, undefinedText, activeForm
            



            


class Game:

    saveData = []

    def initiate(self, method): # LOAD IMAGES AND SAVES HERE. SELECT CHARACTER HERE. SHOW NEW SAVE HERE. LOAD SAVE HERE
        #METHOD = LOAD SAVE|NEW SAVE|
        key = ''
        if method == 'new': # INITAITES A NEW SAVE
            saveForm = ''
            saveActiveForm = False
            completed = False
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.VIDEORESIZE:
                        auth.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                        auth.width,auth.height = event.w,event.h
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            key = 'return'
                        elif event.key == pygame.K_BACKSPACE:
                            key = 'backspace'
                        else:
                            key = event.unicode
                auth.window.fill(colours.get("Sky_blue"))
                if completed == False:
                    #pygame.draw.rect(auth.window, (colours.get('Steel_gray')), (40,auth.height/2-80,auth.width-80,40))
                    GUI.text(auth.width/2,160, 'Biome', 46, 'New Save', colours.get('Steel_gray'), auth.window)
                    key, saveForm, saveActiveForm = GUI.form(GUI, 40, auth.height/2-80,auth.width-80,40, 'Biome', 30, 'Save Name', saveForm, colours.get('Steel_gray'), colours.get('Azure'), saveActiveForm, auth.window, key)
                    if key == 'form filled' and saveActiveForm == False:
                        if os.path.isdir(BASE_DIR + '/Saves'):
                            # CHECK IF A SAVE ALREADY HAS THE SAME NAME
                            if os.path.isfile(BASE_DIR + '/Saves/%s.save' % (saveForm)):
                                print("A save already has this name: %s" % (saveForm))
                            else: #CREATE A SAVE FILE
                                # --- LAYOUT OF SAVE FILE---
                                # USERNAME
                                # DATE CREATED
                                # SPRITE
                                # LEVEL
                                # CURRENT WORLD
                                # DICT OF ITEMS IN INVENTORY WITH A POSITION NUMBER OF LOCATION IN INVENTORY ETC.... {'Gun': 0} - GUN IS IN SLOT 0 OF INVENTORY
                                # dict of items with health values etc... {'Gun': 100%} - FULL HEALTH. {'Gun': 50%} - HALF HEALTH
                                # --- LAYOUT OF SAVE FILE---
                                with open(BASE_DIR + '/Saves/%s' % (saveForm), 'w') as f: # CREATE GENERIC SAVE
                                    f.write('Username: %s\nDate Created: %s\nSprite: %s\nCurrent level: %s\nCurrent World: %s\nInventoy: %s\nHealth Inventory: %s' % (auth.user,datetime.now(),'None',1,'map1',{},{}))
                                completed = True
                                # self.initiate(self, 'load')
                        else:
                            os.mkdir(BASE_DIR + '/Saves')    
                            with open(BASE_DIR + "/Saves/%s" % (saveForm), "w") as f: # CREATE GENERIC SAVE
                                f.write('Username: %s\nDate Created: %s\nCurrent level: %s\nCurrent World: %s\nInventoy: %s\nHealth Inventory: %s' % (auth.user,datetime.now(),1,'map1',{},{}))
                            completed = True
                else:
                    pygame.draw.rect(auth.window, colours.get('Steel_gray'), (10,10,auth.width/2-5,auth.height-20))
                    pygame.draw.rect(auth.window, colours.get('Steel_gray'), (auth.width/2+10,10,auth.width/2-15 ,auth.height-20))

                    mouse,click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
                    if 10+auth.width/2-5 > mouse[0] > 10 and 10+auth.height-20 > mouse[1] > 10 and click[0] == 1:
                        #male selected | FIRST RECTANGLE |
                        with open(BASE_DIR + '\\' + '/Saves/%s' % (saveForm), 'r') as f:
                            data = f.read()
                        data = data.split('\n')
                        data[2] = 'Sprite: Male'
                        #COMPILE LIST INTO NEW LINE STRING TO BE WRITTEN BACK TO SAVE
                        for i in range(len(data)):
                            if i == 0:
                                compiled = data[i]
                            else:
                                compiled = compiled + "\n" + data[i]
                        with open(BASE_DIR + '/Saves/%s' % (saveForm), 'w') as f:
                            f.write(compiled)
                        #SAVE LOADED SAVE DATA TO CLASS FOR EASY ACCESS WITHOUT HAVING TO RELOAD SAVE DURING GAME AND UPDATE SAVE ON GAME CLSOE OR SAVE
                        self.saveData = data
                        self.initiate(self, 'load')

                    if auth.width/2+20 > mouse[0] > auth.width/2+10 and 10+auth.height-20 > mouse[1] > auth.height-20:
                        # female selected | SECOND RECTANGLE |
                        with open(BASE_DIR + '//Saves//%s' % (saveForm), 'r') as f:
                            data = f.read()
                        data = data.split('\n')
                        data[2] = 'Sprite: Female'
                        for i in range(len(data)):
                            if i == 0:
                                compiled = data[i]
                            else:
                                compiled = compiled + '\n' + data[i]
                        with open(BASE_DIR + '/Saves/%s' % (saveForm), "w") as f:
                            f.write(compiled)
                        self.saveData = data
                        self.initiate(self, 'load') # WHY ARE WE LOADING WHEN WE HAVE ALREADY ADDED SAVE TO SELF.SAVEDATA                 



                pygame.display.flip()
        if method == 'load': #LOAD SCREEN, WORLD, SAVE DATA IF NOT LOADED, LOAD INVENTORY AND WORLD ITEMS, FINIALIZE AND SEND TO MAIN FUNC
            if self.saveData == []: # NO SAVE LOADED | DISPLAY ALL SAVES IN SAVE FOLDER AND ALLOW USER TO SELECT SAVE
                if os.path.isdir(BASE_DIR + '//' + '/Saves/'):
                    saveDir = BASE_DIR + '//' + '/Saves/'
                    files = os.listdir(saveDir)
                    print(files)
                    for f in files:
                        if not os.path.isfile( BASE_DIR + '//' + f):
                            #program pssibly found dir or other fodler | remove
                            files.remove(f)
                    #NOW SHOW ALL SAVES AND LE USER SELECT ONE
                    loadSaveFile = None # VAR FOR FILE NAME AFTER SELECTED


                    ybox = 90
                    saveBox = []
                    for y in range(16):
                        ybox += 45
                        saveBox.append([10,ybox])
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.VIDEORESIZE:
                                auth.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                                auth.width, auth.height = event.w, event.h
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if ybox > auth.height:
                                    if event.button == 4:
                                        for scroll in saveBox:
                                            scroll[1] -= 45
                                    if event.button == 5:
                                        for scroll in saveBox:
                                            scroll[1] += 45
                        auth.window.fill(colours.get('Sky_blue'))

                        for box in range(len(saveBox)):
                            if saveBox[box][0] > 90 and saveBox[box][1] < auth.height:
                                pygame.draw.rect(auth.window, colours.get('Steel_gray'), (saveBox[box][0],saveBox[box][1],auth.width-20,30))
                                #GUI.text((aut.width-20)/2,saveBox[box][1]+10,'Biome', 15, files[box], colours.get('Azure'), auth.window)

                        
                        pygame.display.flip()

class auth:

    pygame.init()
    width,height = 1024,768
    window = pygame.display.set_mode((width,height), pygame.RESIZABLE)
    pygame.display.set_caption('Fallen Planets 1.3A')

    user = 'Dextron'

    def Login(self): #DISPLAY LOGIN PAGE UNLESS RAN THROUGH LAUNCHER | DISPLAY MAIN MENU
        #FOR NOW USE A GENERIC STATEMENT AS A PLACE OLDER FOR A LOGIN SCRIOT
        if self.user == 'Dextron':
            Game.initiate(Game, 'load')
        else:
            print("Incorrect login")

auth.Login(auth)
