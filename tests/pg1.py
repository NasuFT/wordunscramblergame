import pygame as p

p.init()
#Note: Still have to replace a lot of recs and surfaces with images

class Settings():
    def __init__(self):
        self.name   = 'Autistic-induced Word Unscrambler'
        self.assets = 'Assets/'
        self.clock  = p.time.Clock()
        self.width  = 1200
        self.height = 720

        self.screen = p.display.set_mode((self.width, self.height))
        self.tag    = p.display.set_caption(self.name)
        self.f      = '8bitwondernominal'
        self.f_big  = p.font.SysFont(self.f, 75)
        self.f_mid  = p.font.SysFont(self.f, 50)
        self.f_tiny = p.font.SysFont(self.f, 25)
        self.frames = 50
        self.colors = {"red"   : (255, 0, 0),
                       "green" : (0, 255, 0),
                       "blue"  : (0, 0, 255),
                       "yellow": (255, 255, 0),
                       "purple": (255, 0, 255),
                       "orange": (255, 165, 0),
                       "white" : (255, 255, 255),
                       "black" : (0, 0, 0),
                       "brown" : (153, 76, 0),
                       "grey"  : (100, 100, 100)}
        @property
        def  width(self): return self.width
        @property
        def height(self): return self.height
        @property
        def  f_big(self): return self.f_big
        @property
        def  f_mid(self): return self.f_mid
        @property
        def f_tiny(self): return self.f_tiny
        @width.setter
        def  width(self, x): self._width  = x
        @height.setter
        def height(self, x): self._height = x
        @f_big.setter
        def  f_big(self, x): self._f_big  = p.font.SysFont(f, x)
        @f_mid.setter
        def  f_mid(self, x): self._f_mid  = p.font.SysFont(f, x)
        @f_tiny.setter
        def f_tiny(self, x): self._f_tiny = p.font.SysFont(f, x)

#shortcuts
z = Settings()
a = z.assets
c = z.colors
d = z.screen
f = z.f_tiny
sw, sh, sc = z.width, z.height, (z.width/2, z.height/2)


def asset(x): return a+x+'.png'
def collide(x, m): return p.Rect(x).collidepoint(m)
def seq(x, y):
    if x>=len(y): x -= 3
    elif x<0: x += 3
    return x

#to be used for game_screen()
word_list, done = sorted(['jack', 'jill', 'hill', 'fetch', 'pail', 'water', 'down', 'broke', 'crown', 'tumble', 'after']), []

def title_screen():
    title  = p.image.load(asset('Rocket0')).convert_alpha()
    d.fill(c['black'])
    while True:
        start = button(sc[0], sc[1], 'Play0', 'Play1')
        for event in p.event.get():
            if event.type == p.QUIT: quit()
            elif event.type == p.KEYDOWN:
                if event.key == p.K_RETURN: menu_screen()
            elif event.type == p.MOUSEBUTTONDOWN:
                m = p.mouse.get_pos()
                if p.Rect(start).collidepoint(m): menu_screen()
        d.blit(title, (sc[0]-title.get_rect().width/2, sc[1]-title.get_rect().height))
        p.display.update()
        z.clock.tick(z.frames)

def menu_screen():
    d.fill(c['black'])
    mode = ['ANAGRAM', 'COMBINE', '[COMING SOON]']
    diff = ['ZEN', 'CHALLENGE', 'HELL']
    md, df = 0, 0
    diff_r = button(sc[0]+223, sc[1]+23, 'Arrow_R')
    diff_l = button(sc[0]-223, sc[1]+23, 'Arrow_L')
    mode_r = button(sc[0]+223, sc[1]-23, 'Arrow_R')
    mode_l = button(sc[0]-223, sc[1]-23, 'Arrow_L')
    while True:
        start = button(sc[0], sh-23, 'Play0', 'Play1')
        
        for event in p.event.get():
            if event.type == p.QUIT: quit()
            elif event.type == p.KEYDOWN:
                if event.key == p.K_RETURN: game_screen(word_list, done)
            elif event.type == p.MOUSEBUTTONDOWN:
                m = p.mouse.get_pos()
                if collide(start, m): game_screen(word_list, done)
                if collide(mode_r, m): md = seq(md+1, mode)
                if collide(mode_l, m): md = seq(md-1, mode)
                if collide(diff_r, m): df = seq(df+1, diff)
                if collide(diff_l, m): df = seq(df-1, diff)
             
        p.draw.rect(d, c['red'], (sc[0]-200, sc[1]-46, 400, 46))
        p.draw.rect(d, c['blue'], (sc[0]-200, sc[1], 400, 46))
        md_s = f.render(mode[md], True, c['white'])
        df_s = f.render(diff[df], True, c['white'])
        d.blit(md_s, (sc[0]-md_s.get_rect().width/2, sc[1]-46+46/4))
        d.blit(df_s, (sc[0]-df_s.get_rect().width/2, sc[1]+46/4))
        p.display.update()
        z.clock.tick(z.frames)
    
#art shortcuts
tile = p.image.load(asset('Tile'))
life = p.image.load(asset('Life'))

pause_state = 1 #global pause state

def game_screen(word_list, done):
    global pause_state
    p.key.set_repeat(30, 30)
    text, timer, time, lives, score = '', 999, 300, 5, 0
    n = len(max(word_list))
    while True:  #initializer for start and pause sequences
        if pause_state == 1:
            d.fill(c['black'])
            text, lives, score = list_words(text, lives, score)
            prev_lives = lives_update(lives, 256, 0)
            prev_score = score_update(score, 770, 0)
            timer, pause_state = 999, 0
        timer += 1
        if timer*20%1000==0: time = timer_update(time-1, 0, 0)
        
        pause = button(sw-25, 25, 'Pause0', 'Pause1')

        for event in p.event.get():
            if event.type == p.MOUSEBUTTONDOWN:
                m = p.mouse.get_pos()
                if p.Rect(pause).collidepoint(m): pause_panel()
            elif event.type == p.KEYDOWN:
                if event.key == p.K_RETURN:
                    p.key.set_repeat(30, 30)
                    text, lives, score = list_words(text, lives, score)
                    if prev_lives!=lives: prev_lives = lives_update(lives, 256, 0)
                    if prev_score!=score: prev_score = score_update(score, 770, 0)
                elif event.key == p.K_BACKSPACE: text = text[:-1]
                else:
                    p.key.set_repeat(30, 30)
                    text += event.unicode.upper()
        
        text = text[:n]
        t_s = f.render(text, True, c['white'])
        p.draw.rect(d, c['red'], (sc[0]-200, sc[1]+46, 400, 46))
        d.blit(t_s, (sc[0]-t_s.get_rect().width/2, sc[1]+46+46/4)) 
        p.display.update()
        z.clock.tick(z.frames)

def pause_panel():
    global pause_state
    fade(c['black'], 75)
    pause_state = 1
    while True:
        play = button(sc[0]-88, sc[1], 'Play0', 'Play1')
        res  = button(sc[0], sc[1], 'Res0', 'Res1')
        bbye = button(sc[0]+88, sc[1], 'Pause0', 'Pause1')
        for event in p.event.get():
            if event.type == p.MOUSEBUTTONDOWN:
                m = p.mouse.get_pos()
                if p.Rect(play).collidepoint(m): return
                elif p.Rect(res).collidepoint(m): game_screen(word_list, done)
                elif p.Rect(bbye).collidepoint(m): menu_screen()
            elif event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE or event.key == p.K_RETURN: return
                elif event.key == p.K_r: game_screen()
        p.display.update()
        z.clock.tick(z.frames)

def timer_update(time, x, y, w=256, h=46):
    p.draw.rect(d, c['white'], (x, y, w, h))
    if time%2==0: t_surf = f.render('X TIME: {}'.format(time), True, (0, 0, 0))
    else:         t_surf = f.render('# TIME: {}'.format(time), True, (0, 0, 0))
    d.blit(t_surf, (x+11, y+11))
    return time

def lives_update(lives, x, y):
    l_surf = f.render('LIVES: ', True, c['red'])
    l_w, i = l_surf.get_rect().width, 0
    p.draw.rect(d, c['grey'], (x, y, l_w+375, 46))
    d.blit(l_surf, (x+11, y+11))
    x2 = x+l_w+44
    while i<lives:
        d.blit(life, (x2, y))
        x2, i = x2+66, i+1
    return lives
   
def score_update(score, x, y):
    s_surf = f.render('SCORE: '+str(score), True, c['black'])
    s_w = s_surf.get_rect().width+23*len(str(score))
    p.draw.rect(d, c['white'], (x, y, s_w+23, 46))
    d.blit(s_surf, (x+11, y+11))
    return score

def list_words(text, lives, score):
    i, y = 0, 69
    while i<len(word_list):
        if i==0: x = 23
        if i!=0 and i%5==0:
            x, y = x+256, 69
            def_x = x
        else: def_x = x
        if (text.lower()==word_list[i] or word_list[i] in done) and text!='':
            if text.lower() not in done:
                if text.lower() in word_list: score += 10
                done.append(text.lower())
            for j in range(len(word_list[i])):
                slot = f.render(word_list[i][j], True, (255, 255, 255))
                d.blit(tile, (x, y))
                d.blit(slot, (x+tile.get_rect().width/2-slot.get_rect().width/2,
                              y+tile.get_rect().height/2-slot.get_rect().height/2))
                x += 46
        else:
            for j in range(len(word_list[i])):
                slot  = f.render(word_list[i][j], True, (0, 255, 0))
                d.blit(tile, (x, y))
                d.blit(slot, (x+tile.get_rect().width/2-slot.get_rect().width/2,
                              y+tile.get_rect().height/2-slot.get_rect().height/2))
                x += 46
        x = def_x
        i, y = i+1, y+69
    if text!='' and text.lower() not in word_list: lives -= 1
    return '', lives, score

def fade(color, alpha): #tints screen
    fade = p.Surface((sw, sh))
    fade.fill(color)
    fade.set_alpha(alpha)
    d.blit(fade, (0, 0))

def button(x, y, off, on=0): #in/active button image; returns rect for collision detection purposes
    mouse = p.mouse.get_pos()
    b_off = p.image.load(asset(off)).convert_alpha()
    if on!=0: b_on = p.image.load(asset(on)).convert_alpha()
    w, h = b_off.get_rect().width, b_off.get_rect().height
    new_x, new_y = x-w/2, y-h/2
    if new_x+w>mouse[0]>new_x and new_y+h>mouse[1]>new_y and on!=0: d.blit(b_on, (new_x, new_y))
    else: d.blit(b_off, (new_x, new_y))
    return (new_x, new_y, w, h)

title_screen()
#menu_screen()
#game_screen(word_list, done)

