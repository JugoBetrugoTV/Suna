#!/usr/bin/env python3
"""
HOLLOWMERE - A Story-Driven Horror RPG
Standalone Pygame version. Pixel art, top-down, Stardew Valley style.
"""
import pygame
import sys
import math
import random
import time as pytime

# ============================================================
#  INIT
# ============================================================
pygame.init()
pygame.mixer.quit()  # no sound for now

TILE = 16
SCALE = 3
TS = TILE * SCALE  # 48px display
SCREEN_W, SCREEN_H = 15 * TS, 11 * TS  # 720x528

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.RESIZABLE)
pygame.display.set_caption("HOLLOWMERE")
clock = pygame.time.Clock()

# Pixel-perfect surface
game_surface = pygame.Surface((15 * TILE, 11 * TILE))

# ============================================================
#  COLORS
# ============================================================
C_GRASS = [(74,124,63), (90,156,79), (61,107,52)]
C_PATH = (139,115,85)
C_PATH2 = (160,128,96)
C_WOOD = (107,68,35)
C_WOOD_DARK = (74,48,25)
C_STONE = (128,128,128)
C_STONE_DARK = (96,96,96)
C_ROOF = (139,69,19)
C_ROOF2 = (160,82,45)
C_DOOR = (107,68,35)
C_DOOR_HANDLE = (200,168,78)
C_WINDOW = (58,90,138)
C_TREE_TRUNK = (90,56,24)
C_TREE_LEAF = [(42,90,36), (58,106,52), (26,74,24)]
C_DARK_LEAF = [(26,58,20), (15,42,15), (37,58,32)]
C_WELL_STONE = (128,128,128)
C_WELL_SEAL = (100,100,100)
C_WATER = [(58,110,165), (74,142,197)]
C_SKIN = (232,184,157)
C_BLACK = (0,0,0)
C_WHITE = (255,255,255)
C_RED = (180,0,0)
C_YELLOW = (240,192,64)
C_UI_BG = (0,0,0)
C_UI_BORDER = (85,85,85)
C_THOUGHT = (176,112,208)

# ============================================================
#  TILE GENERATION (16x16 pixel surfaces)
# ============================================================
tile_cache = {}

def make_tile(name, draw_fn):
    if name in tile_cache:
        return tile_cache[name]
    surf = pygame.Surface((TILE, TILE))
    draw_fn(surf)
    tile_cache[name] = surf
    return surf

def draw_grass(surf, variant=0):
    base = C_GRASS[variant % 3]
    surf.fill(base)
    rng = random.Random(variant * 137)
    for _ in range(8):
        x, y = rng.randint(0,15), rng.randint(0,15)
        c = C_GRASS[rng.randint(0,2)]
        surf.set_at((x,y), c)

def draw_path(surf, variant=0):
    rng = random.Random(variant * 97)
    for y in range(16):
        for x in range(16):
            c = C_PATH if rng.random() > 0.3 else C_PATH2
            if rng.random() < 0.1:
                c = (122,101,72)
            surf.set_at((x,y), c)

def draw_wood_wall(surf):
    for y in range(16):
        for x in range(16):
            c = C_WOOD if x % 4 != 0 else C_WOOD_DARK
            if (x+y) % 8 == 0:
                c = (124,94,48)
            surf.set_at((x,y), c)

def draw_window_wall(surf):
    draw_wood_wall(surf)
    # Window
    for y in range(3,10):
        for x in range(4,12):
            surf.set_at((x,y), C_WINDOW)
    # Frame
    for x in range(4,12):
        surf.set_at((x,3), C_WOOD_DARK)
        surf.set_at((x,9), C_WOOD_DARK)
    for y in range(3,10):
        surf.set_at((4,y), C_WOOD_DARK)
        surf.set_at((11,y), C_WOOD_DARK)
        surf.set_at((7,y), C_WOOD_DARK)

def draw_stone_wall(surf):
    for y in range(16):
        for x in range(16):
            c = C_STONE if (x+y*3)%5 != 0 else C_STONE_DARK
            if y%8==0 or x%8==0: c = (102,102,102)
            surf.set_at((x,y), c)

def draw_roof(surf, dark=False):
    base = (64,64,64) if dark else C_ROOF
    alt = (74,74,74) if dark else C_ROOF2
    for y in range(16):
        for x in range(16):
            c = base if y%3 != 0 else alt
            if x%6 == 0: c = (122,58,15) if not dark else (55,55,55)
            surf.set_at((x,y), c)

def draw_door(surf):
    surf.fill(C_WOOD_DARK)
    for y in range(1,16):
        for x in range(3,13):
            surf.set_at((x,y), C_DOOR)
    for y in range(7,9):
        for x in range(10,12):
            surf.set_at((x,y), C_DOOR_HANDLE)

def draw_tree(surf, dark=False):
    surf.fill((0,0,0,0))
    surf.set_colorkey((0,0,0))
    colors = C_DARK_LEAF if dark else C_TREE_LEAF
    trunk = (42,24,8) if dark else C_TREE_TRUNK
    # Trunk
    for y in range(10,16):
        for x in range(6,10):
            surf.set_at((x,y), trunk)
    # Leaves
    rng = random.Random(42 if not dark else 99)
    for y in range(0 if dark else 1, 12 if dark else 11):
        for x in range(1 if dark else 2, 15 if dark else 14):
            if abs(x-8)+abs(y-5) < (9 if dark else 8):
                surf.set_at((x,y), colors[rng.randint(0, len(colors)-1)])

def draw_well(surf):
    surf.fill(C_GRASS[0])
    # Base
    for y in range(4,16):
        for x in range(2,14):
            surf.set_at((x,y), C_WELL_STONE)
    # Sealed top
    for y in range(6,14):
        for x in range(4,12):
            c = C_WELL_SEAL if (x+y)%3 != 0 else (120,120,120)
            surf.set_at((x,y), c)

def draw_flower(surf, color):
    draw_grass(surf, 0)
    rng = random.Random(hash(color))
    for _ in range(4):
        fx, fy = rng.randint(2,12), rng.randint(2,12)
        surf.set_at((fx,fy), color)
        surf.set_at((fx+1,fy), color)
        surf.set_at((fx,fy+1), color)
        surf.set_at((fx+1,fy+1), color)
        surf.set_at((fx,fy-1), (255,230,128))

def draw_water(surf, frame=0):
    rng = random.Random(frame * 31)
    for y in range(16):
        for x in range(16):
            i = (x+y+frame) % 4
            c = C_WATER[0] if i < 2 else C_WATER[1]
            if rng.random() < 0.15:
                c = (42,94,149)
            surf.set_at((x,y), c)

# Build all tiles
def init_tiles():
    for i in range(6):
        make_tile(f'grass{i}', lambda s, v=i: draw_grass(s, v))
    for i in range(4):
        make_tile(f'path{i}', lambda s, v=i: draw_path(s, v))
    make_tile('wood', draw_wood_wall)
    make_tile('window', draw_window_wall)
    make_tile('stone', draw_stone_wall)
    make_tile('roof', lambda s: draw_roof(s, False))
    make_tile('roofD', lambda s: draw_roof(s, True))
    make_tile('door', draw_door)
    make_tile('tree', lambda s: draw_tree(s, False))
    make_tile('dtree', lambda s: draw_tree(s, True))
    make_tile('well', draw_well)
    make_tile('flowerR', lambda s: draw_flower(s, (220,60,60)))
    make_tile('flowerY', lambda s: draw_flower(s, (220,220,60)))
    make_tile('flowerB', lambda s: draw_flower(s, (80,80,220)))
    for i in range(4):
        make_tile(f'water{i}', lambda s, f=i: draw_water(s, f))

init_tiles()

# ============================================================
#  CHARACTER SPRITES (16x16)
# ============================================================
def make_char_sprite(skin, hair, shirt, pants, direction, frame):
    surf = pygame.Surface((TILE, TILE), pygame.SRCALPHA)
    f = frame % 2
    # Head
    for y in range(0,6):
        for x in range(4,12):
            surf.set_at((x,y), skin)
    # Hair
    for x in range(4,12):
        surf.set_at((x,0), hair)
    if direction == 0:  # up
        for x in range(4,12): surf.set_at((x,1), hair)
    else:
        for x in range(4,6): surf.set_at((x,1), hair); surf.set_at((x,2), hair)
        for x in range(10,12): surf.set_at((x,1), hair); surf.set_at((x,2), hair)
    # Eyes
    if direction == 2: surf.set_at((6,3),(34,34,34)); surf.set_at((9,3),(34,34,34))
    elif direction == 1: surf.set_at((5,3),(34,34,34)); surf.set_at((8,3),(34,34,34))
    elif direction == 3: surf.set_at((7,3),(34,34,34)); surf.set_at((10,3),(34,34,34))
    # Body
    for y in range(6,12):
        for x in range(4,12):
            surf.set_at((x,y), shirt)
    for y in range(6,10):
        surf.set_at((3,y), shirt); surf.set_at((12,y), shirt)
    surf.set_at((3,10), skin); surf.set_at((12,10), skin)
    # Legs
    for y in range(12,16):
        for x in range(5,8): surf.set_at((x,y), pants)
        for x in range(8,11): surf.set_at((x,y), pants)
    if f == 1:
        surf.set_at((4,14), pants); surf.set_at((11,14), pants)
    # Shoes
    for x in range(5,8): surf.set_at((x,15), (58,42,26))
    for x in range(8,11): surf.set_at((x,15), (58,42,26))
    return surf

# ============================================================
#  MAP
# ============================================================
MAP_W, MAP_H = 40, 35
map_data = [
"TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
"TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",
"TT......TT....pppppp....TT......TT...TT",
"TT......TT....p....p....TT......TT...TT",
"TT..ff..TT....p....p....TT..ff..TT...TT",
"TTTTTTTTTTRRRRp....prrrrTTTTTTTTTT...TT",
"TT........RRRRp....prwwrTT........TT.TT",
"TT........sssspp..pprWWr..........TT.TT",
"TT..ff....ssss.pppp.rddr..ff......TT.TT",
"TT........ssss.p..p.p..p.........TT..TT",
"TTT..TT...sDss.p..p.p..p...TT..TTT..TT",
"TT........ssss.p..p.p..p.........TT..TT",
"TT..pp....pppppp..pppppp....pp.....pp.TT",
"TT..pp....p..........p.....pp.....pp.TT",
"TT..pp....p..........p.....pp.....pp.TT",
"TT..pp....p....BB....p.....pp.....pp.TT",
"TT..pppppppp...BB...pppppppppp....pp.TT",
"TT..pp....p..........p.....pp.....pp.TT",
"TT..pp....p..........p.....pp.....pp.TT",
"TT..pp.rwwr.pppppppp.rwwr..pp.....pp.TT",
"TT..pp.rwwr.p......p.rwwr..pp.....pp.TT",
"TT..pp.rddr.p......p.rddr..pp..ff.pp.TT",
"TT..pp.p..p.p......p.p..p..pp.....pp.TT",
"TT..pppppppppp....pppppppppppp.....pp.TT",
"TT..pp....p..........p.....pp.....pp.TT",
"TT..pp....p..........p.....pp..ff.pp.TT",
"TT..pp....p..........p.....pp.....pp.TT",
"TT..pppppppppppppppppppppppppp.....pp.TT",
"TT......pp..............pp.........pp.TT",
"TT......pp..............pp..........TTTT",
"TT......pp..............pp..........TTTT",
"TT..ff..pp..............pp..ff......TTTT",
"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
]

def tile_at(x, y):
    if x < 0 or y < 0 or x >= MAP_W or y >= MAP_H:
        return 'T'
    row = map_data[y] if y < len(map_data) else ''
    return row[x] if x < len(row) else 'T'

def tile_solid(ch):
    return ch in 'TDwWsrRcCSB'

def get_tile_name(ch, x, y):
    v = (x*7+y*13) % 6
    pv = (x*3+y*5) % 4
    return {
        '.': f'grass{v}', 'f': f'grass{v}',
        'T': 'tree', 'D': 'dtree',
        'p': f'path{pv}',
        'w': 'wood', 'W': 'window',
        's': 'stone', 'S': 'stone',
        'r': 'roof', 'R': 'roofD',
        'd': 'door', 'B': 'well',
        'c': 'stone',
        '~': 'water0',
    }.get(ch, f'grass{v}')

def get_overlay(ch, x, y):
    if ch == 'f':
        v = (x*3+y*7) % 3
        return ['flowerR','flowerY','flowerB'][v]
    return None

# ============================================================
#  GAME STATE
# ============================================================
class GameState:
    def __init__(self):
        self.name = ''
        self.origin = ''
        self.trauma = ''
        self.attrs = {'wil':1,'emp':1,'per':1,'agg':1,'int':1}
        self.pts_left = 10
        self.mental_state = 80
        self.guilt = 0
        self.day = 1
        self.time_of_day = 'Nachmittag'
        self.flags = set()
        self.notebook = []
        self.clues = []
        self.rels = {'maren':50,'brandt':50,'ernst':50,'nina':50,'lena':50}
        self.phase = 'title'  # title, intro, creation, playing, dialogue

    def check(self, attr, val):
        return self.attrs.get(attr, 0) >= val

    def mod_ms(self, n):
        self.mental_state = max(0, min(100, self.mental_state + n))

    def mod_rel(self, npc, n):
        self.rels[npc] = max(0, min(100, self.rels.get(npc,50) + n))

    def add_note(self, t):
        if t not in self.notebook:
            self.notebook.append(t)

    def has_flag(self, f):
        return f in self.flags

gs = GameState()

# ============================================================
#  PLAYER & NPCs
# ============================================================
class Entity:
    def __init__(self, x, y, skin, hair, shirt, pants, name=''):
        self.x = float(x)
        self.y = float(y)
        self.dir = 2  # 0=up 1=left 2=down 3=right
        self.frame = 0
        self.frame_timer = 0
        self.moving = False
        self.name = name
        self.sprites = {}
        for d in range(4):
            for f in range(2):
                self.sprites[f'{d}_{f}'] = make_char_sprite(skin,hair,shirt,pants,d,f)

    def get_sprite(self):
        return self.sprites.get(f'{self.dir}_{self.frame}')

player = Entity(19, 28, C_SKIN, (106,74,42), (74,106,138), (58,58,90))
player.dir = 0

npcs = [
    Entity(17, 8, C_SKIN, (106,58,26), (200,168,50), (238,238,238), 'Maren Voss'),
    Entity(9, 9, (212,160,136), (136,136,136), (34,34,34), (34,34,34), 'Pfarrer Brandt'),
    Entity(22, 8, C_SKIN, (102,102,102), (106,90,58), (74,58,42), 'Ernst Hofer'),
    Entity(14, 25, C_SKIN, (160,64,32), (58,122,74), (90,74,58), 'Nina Althammer'),
    Entity(15, 16, (212,160,136), (170,170,170), (102,102,102), (85,85,85), '???'),
]

# ============================================================
#  CAMERA
# ============================================================
cam_x, cam_y = 0.0, 0.0

def update_camera():
    global cam_x, cam_y
    tw = game_surface.get_width() / TILE
    th = game_surface.get_height() / TILE
    tx = player.x - tw/2 + 0.5
    ty = player.y - th/2 + 0.5
    cam_x += (tx - cam_x) * 0.1
    cam_y += (ty - cam_y) * 0.1

# ============================================================
#  DIALOGUE SYSTEM
# ============================================================
class DialogueSystem:
    def __init__(self):
        self.active = False
        self.lines = []  # list of (speaker, text, style, choices)
        self.current_idx = 0
        self.shown_chars = 0
        self.char_timer = 0
        self.done_typing = False
        self.choices = None
        self.selected_choice = 0
        self.font = pygame.font.SysFont('Courier New', 14)
        self.font_small = pygame.font.SysFont('Courier New', 12)
        self.font_title = pygame.font.SysFont('Courier New', 16, bold=True)

    def start(self, lines):
        self.lines = lines
        self.current_idx = 0
        self.shown_chars = 0
        self.char_timer = 0
        self.done_typing = False
        self.choices = None
        self.selected_choice = 0
        self.active = True
        gs.phase = 'dialogue'
        self._load_current()

    def _load_current(self):
        if self.current_idx >= len(self.lines):
            self.close()
            return
        entry = self.lines[self.current_idx]
        self.shown_chars = 0
        self.done_typing = False
        self.choices = entry.get('choices')
        self.selected_choice = 0

    def advance(self):
        if not self.done_typing:
            entry = self.lines[self.current_idx]
            self.shown_chars = len(entry.get('text',''))
            self.done_typing = True
            if self.choices:
                self.selected_choice = 0
            return

        if self.choices:
            return  # must pick a choice

        self.current_idx += 1
        if self.current_idx >= len(self.lines):
            self.close()
        else:
            self._load_current()

    def pick_choice(self):
        if not self.choices or not self.done_typing:
            return
        ch = self.choices[self.selected_choice]
        if ch.get('action'):
            ch['action']()
        # Insert follow-up lines if any
        follow = ch.get('follow', [])
        if follow:
            idx = self.current_idx + 1
            for f in follow:
                self.lines.insert(idx, f)
                idx += 1
        self.choices = None
        self.current_idx += 1
        if self.current_idx >= len(self.lines):
            self.close()
        else:
            self._load_current()

    def close(self):
        self.active = False
        self.lines = []
        gs.phase = 'playing'

    def update(self, dt):
        if not self.active:
            return
        if self.current_idx >= len(self.lines):
            return
        entry = self.lines[self.current_idx]
        text = entry.get('text','')
        if self.shown_chars < len(text):
            self.char_timer += dt
            if self.char_timer > 30:
                self.char_timer = 0
                self.shown_chars += 1
                if self.shown_chars >= len(text):
                    self.done_typing = True

    def draw(self, surface):
        if not self.active or self.current_idx >= len(self.lines):
            return
        entry = self.lines[self.current_idx]
        sw, sh = surface.get_size()

        # Dialogue box
        box_h = 130
        box_y = sh - box_h - 10
        box_rect = pygame.Rect(20, box_y, sw-40, box_h)
        pygame.draw.rect(surface, (0,0,0), box_rect)
        pygame.draw.rect(surface, (85,85,85), box_rect, 2)

        # Speaker
        speaker = entry.get('speaker','')
        style = entry.get('style','normal')
        text = entry.get('text','')
        shown = text[:self.shown_chars]

        y_off = box_y + 10
        if speaker:
            sp_surf = self.font_title.render(speaker, True, C_YELLOW)
            surface.blit(sp_surf, (36, y_off))
            y_off += 22

        # Text color
        tc = C_WHITE
        if style == 'thought': tc = C_THOUGHT
        elif style == 'horror': tc = C_RED

        # Word wrap
        words = shown.split(' ')
        line = ''
        for w in words:
            test = line + (' ' if line else '') + w
            if self.font.size(test)[0] > box_rect.width - 30:
                ts = self.font.render(line, True, tc)
                surface.blit(ts, (36, y_off))
                y_off += 18
                line = w
            else:
                line = test
        if line:
            ts = self.font.render(line, True, tc)
            surface.blit(ts, (36, y_off))
            y_off += 18

        # Choices
        if self.choices and self.done_typing:
            y_off = max(y_off + 4, box_y + 50)
            for i, ch in enumerate(self.choices):
                if ch.get('req') and not ch['req']():
                    continue
                prefix = '> ' if i == self.selected_choice else '  '
                color = C_YELLOW if i == self.selected_choice else (170,170,170)
                cs = self.font_small.render(prefix + ch['text'], True, color)
                surface.blit(cs, (36, y_off))
                y_off += 16

        # Advance hint
        if self.done_typing and not self.choices:
            hint = self.font_small.render('[LEERTASTE]', True, (100,100,100))
            surface.blit(hint, (box_rect.right - 100, box_rect.bottom - 18))

dlg = DialogueSystem()

# ============================================================
#  NPC DIALOGUE DATA
# ============================================================
def make_maren_dialogue():
    if gs.has_flag('talked_maren'):
        return [{'speaker':'Maren','text':'Brauchen Sie noch etwas? Abendessen gibt es ab sechs.'}]
    gs.flags.add('talked_maren')
    lines = [
        {'speaker':'Maren','text':'Oh! Ein Gast!'},
        {'speaker':'','text':'Sie laechelt. Breit. Warm. Ihre Augen brauchen eine Sekunde laenger.','style':'thought'},
        {'speaker':'Maren','text':'Willkommen in Hollowmere! Ich bin Maren. Sie muessen hungrig sein.'},
        {'speaker':'','text':'','choices':[
            {'text':f'{gs.name}. Haetten Sie ein Zimmer?',
             'follow':[
                {'speaker':'Maren','text':'Natuerlich! Zimmer drei, oben rechts. Frisch bezogen.'},
                {'speaker':'','text':'Sie greift unter die Theke. Ein Schluessel. Kein Gaestebuch.','style':'thought'},
             ],
             'action': lambda: gs.mod_rel('maren',5)},
            {'text':'Der Fahrer sagte, ich soll nicht zu lang bleiben.',
             'follow':[
                {'speaker':'','text':'Marens Laecheln flackert. Nur fuer einen Moment.','style':'thought'},
                {'speaker':'Maren','text':'Ach, der alte Gerhard. Bleiben Sie so lang Sie wollen. Wirklich.'},
             ],
             'action': lambda: (gs.mod_rel('maren',-3), gs.add_note('Maren besteht darauf dass ich bleibe. Zu nachdruecklich.'))},
        ]},
    ]
    return lines

def make_brandt_dialogue():
    if gs.has_flag('talked_brandt'):
        return [{'speaker':'Brandt','text':'Die Kirche ist immer offen. Falls Sie Ruhe suchen.'}]
    gs.flags.add('talked_brandt')
    return [
        {'speaker':'Brandt','text':'Ah. Ein neues Gesicht.'},
        {'speaker':'','text':'Sein Griff ist fest, aber die Finger sind kalt.','style':'thought'},
        {'speaker':'Brandt','text':'Thomas Brandt. Pfarrer. Fuer das, was es wert ist.'},
        {'speaker':'','text':'','choices':[
            {'text':'Grosse Kirche fuer einen kleinen Ort.',
             'follow':[{'speaker':'Brandt','text':'Sie wurde gebaut, als der Glaube groesser war. Ich weiss nicht, was zuerst geschrumpft ist.'}],
             'action': lambda: gs.mod_rel('brandt',5)},
            {'text':'Ist Hollowmere schon immer so ruhig?',
             'req': lambda: gs.check('emp',2),
             'follow':[
                {'speaker':'','text':'Er schaut zum Fenster. Lange.','style':'thought'},
                {'speaker':'Brandt','text':'Manche Naechte sind lauter als andere. Aber das werden Sie selbst merken.'},
             ],
             'action': lambda: (gs.mod_rel('brandt',3), gs.add_note('Brandt: "Manche Naechte sind lauter als andere."'))},
        ]},
    ]

def make_ernst_dialogue():
    if gs.has_flag('talked_ernst'):
        return [{'speaker':'Ernst','text':'Batterien im Regal links. Falls Sie welche brauchen.'}]
    gs.flags.add('talked_ernst')
    return [
        {'speaker':'Ernst','text':'Guten Tag! Der neue Gast, nicht wahr? Man hoert ja so Dinge.'},
        {'speaker':'','text':'Klein, duenn, Brille. Haende nie still.','style':'thought'},
        {'speaker':'','text':'','choices':[
            {'text':'Was fuer Dinge?',
             'follow':[
                {'speaker':'Ernst','text':'Nichts, nichts! Kleiner Ort. Man weiss eben, wenn jemand Neues da ist.'},
                {'speaker':'','text':'Er sortiert Dosen. Immer und immer wieder.','style':'thought'},
             ]},
            {'text':'Ich brauche eine Taschenlampe.',
             'follow':[
                {'speaker':'Ernst','text':'Natuerlich. Gute Wahl. Die Naechte sind dunkel hier.'},
                {'speaker':'','text':'Seine Hand zittert leicht.','style':'thought'},
             ],
             'action': lambda: gs.flags.add('has_flashlight')},
        ]},
        {'speaker':'Ernst','text':'Seien Sie vorsichtig da draussen. Nachts. Die Wege sind uneben.'},
        {'speaker':'','text':'Er laechelt. Es erreicht seine Augen nicht.','style':'thought'},
    ]

def make_nina_dialogue():
    if gs.has_flag('talked_nina'):
        return [{'speaker':'Nina','text':'Grossvater braucht seine Medizin. Ich muss weiter.'}]
    gs.flags.add('talked_nina')
    return [
        {'speaker':'Nina','text':'Sie sind der Gast.'},
        {'speaker':'','text':'Keine Frage. Eine Feststellung. Sommersprossig. Muede.','style':'thought'},
        {'speaker':'','text':'','choices':[
            {'text':f'{gs.name}. Und du?',
             'follow':[
                {'speaker':'Nina','text':'Nina. Althammer. Mein Grossvater lebt am Ortsrand. Ich kuemmere mich um ihn.'},
             ],
             'action': lambda: gs.mod_rel('nina',5)},
            {'text':'Du siehst muede aus.',
             'req': lambda: gs.check('emp',3),
             'follow':[
                {'speaker':'','text':'Sie blinzelt. Ueberrascht.','style':'thought'},
                {'speaker':'Nina','text':'Mein Grossvater schlaeft schlecht. Und wenn er nicht schlaeft, schlafe ich nicht.'},
                {'speaker':'Nina','text':'Aber danke. Fuer die Ehrlichkeit.'},
                {'speaker':'','text':'Ein halbes Laecheln. Das erste, das echt wirkt in diesem Ort.','style':'thought'},
             ],
             'action': lambda: gs.mod_rel('nina',10)},
        ]},
        {'speaker':'','text':'Sie dreht sich noch einmal um.','style':'thought'},
        {'speaker':'Nina','text':'Nicht nachts in den Wald gehen. Bitte.'},
        {'speaker':'','text':'Ihre Augen. Da ist Angst. Echte Angst.','style':'thought'},
    ]

def make_oldwoman_dialogue():
    if gs.has_flag('talked_old'):
        return [{'speaker':'','text':'Sie sitzt da. Starrt den Brunnen an. Reglos.','style':'thought'}]
    gs.flags.add('talked_old')
    return [
        {'speaker':'','text':'Du setzt dich neben sie. Sie reagiert nicht.','style':'thought'},
        {'speaker':'','text':'Stille. Zehn Sekunden. Zwanzig.','style':'thought'},
        {'speaker':'','text':'Sie dreht den Kopf. Langsam. Laechelt.','style':'thought'},
        {'speaker':'','text':'Dann steht sie auf und geht. Ohne ein Wort.','style':'thought'},
    ]

def make_well_dialogue():
    if gs.has_flag('examined_well'):
        return [{'speaker':'','text':'Der zugemauerte Brunnen. Kalt. Still.','style':'thought'}]
    gs.flags.add('examined_well')
    lines = [
        {'speaker':'','text':'Du legst die Hand auf den Zement. Kuehl. Rau.','style':'thought'},
        {'speaker':'','text':'Du klopfst. Einmal. Zweimal.','style':'thought'},
        {'speaker':'','text':'Hohl. Der Brunnen ist hohl.','style':'thought'},
    ]
    if gs.check('per',3):
        lines.append({'speaker':'','text':'Ein Geruch. Suesslich. Wie verdorbene Blumen.','style':'horror'})
        gs.mod_ms(-2)
        gs.add_note('Der Brunnen ist hohl. Suesslicher Geruch. Warum zugemauert?')
    return lines

NPC_DIALOGUES = {
    'Maren Voss': make_maren_dialogue,
    'Pfarrer Brandt': make_brandt_dialogue,
    'Ernst Hofer': make_ernst_dialogue,
    'Nina Althammer': make_nina_dialogue,
    '???': make_oldwoman_dialogue,
}

# ============================================================
#  TITLE / CREATION SCREENS
# ============================================================
title_font_big = pygame.font.SysFont('Courier New', 36, bold=True)
title_font = pygame.font.SysFont('Courier New', 16)
title_font_small = pygame.font.SysFont('Courier New', 13)
ui_font = pygame.font.SysFont('Courier New', 12)

class CreationScreen:
    def __init__(self):
        self.step = 'title'  # title, intro, name, origin, trauma, attrs
        self.intro_lines = [
            'Es gibt Orte, die auf keiner Karte verzeichnet sind.',
            'Nicht weil sie vergessen wurden.',
            'Sondern weil jemand dafuer gesorgt hat.',
            '', '',
            'Die Leute dort werden freundlich sein.',
            'Sie werden laecheln.',
            '', '',
            'Glaub ihnen nicht.',
        ]
        self.intro_idx = 0
        self.intro_timer = 0
        self.intro_shown = []
        self.name_input = ''
        self.cursor_blink = 0
        self.attr_sel = 0
        self.origin_sel = 0
        self.trauma_sel = 0
        self.origins = [
            ('Journalist/in - Ich suche eine Geschichte', 'journalist'),
            ('Verwandtschaft - Ich suche jemanden', 'relative'),
            ('Zufall - Autopanne, falscher Ort', 'stranger'),
        ]
        self.traumas = [
            ('Ich habe jemanden verloren', 'loss'),
            ('Es gab einen Unfall. Meine Schuld.', 'accident'),
            ('Eine verdraengte Erinnerung', 'memory'),
            ('Nichts. Mir geht es gut.', 'none'),
        ]
        self.attr_names = ['Willenskraft','Empathie','Wahrnehmung','Gewaltbereitschaft','Verstand']
        self.attr_keys = ['wil','emp','per','agg','int']

    def handle_key(self, event):
        if self.step == 'title':
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.step = 'intro'
                self.intro_timer = 0
                self.intro_idx = 0
                self.intro_shown = []

        elif self.step == 'intro':
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.step = 'name'

        elif self.step == 'name':
            if event.key == pygame.K_RETURN:
                if self.name_input.strip():
                    gs.name = self.name_input.strip()
                    self.step = 'origin'
            elif event.key == pygame.K_BACKSPACE:
                self.name_input = self.name_input[:-1]
            elif event.unicode and len(self.name_input) < 20:
                if event.unicode.isprintable():
                    self.name_input += event.unicode

        elif self.step == 'origin':
            if event.key == pygame.K_UP: self.origin_sel = max(0, self.origin_sel-1)
            elif event.key == pygame.K_DOWN: self.origin_sel = min(len(self.origins)-1, self.origin_sel+1)
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                _, key = self.origins[self.origin_sel]
                gs.origin = key
                if key == 'journalist': gs.attrs['per']+=1; gs.attrs['int']+=1; gs.pts_left-=2
                elif key == 'relative': gs.attrs['emp']+=1; gs.pts_left-=1
                self.step = 'trauma'

        elif self.step == 'trauma':
            if event.key == pygame.K_UP: self.trauma_sel = max(0, self.trauma_sel-1)
            elif event.key == pygame.K_DOWN: self.trauma_sel = min(len(self.traumas)-1, self.trauma_sel+1)
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                _, key = self.traumas[self.trauma_sel]
                gs.trauma = key
                if key == 'accident': gs.guilt += 10
                self.step = 'attrs'

        elif self.step == 'attrs':
            if event.key == pygame.K_UP: self.attr_sel = max(0, self.attr_sel-1)
            elif event.key == pygame.K_DOWN: self.attr_sel = min(4, self.attr_sel+1)
            elif event.key == pygame.K_RIGHT:
                k = self.attr_keys[self.attr_sel]
                if gs.pts_left > 0 and gs.attrs[k] < 5:
                    gs.attrs[k] += 1; gs.pts_left -= 1
            elif event.key == pygame.K_LEFT:
                k = self.attr_keys[self.attr_sel]
                if gs.attrs[k] > 1:
                    gs.attrs[k] -= 1; gs.pts_left += 1
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                gs.phase = 'playing'
                self.step = 'done'
                # Start arrival dialogue
                start_arrival()

    def update(self, dt):
        self.cursor_blink += dt
        if self.step == 'intro':
            self.intro_timer += dt
            if self.intro_timer > 1000 and self.intro_idx < len(self.intro_lines):
                self.intro_shown.append(self.intro_lines[self.intro_idx])
                self.intro_idx += 1
                self.intro_timer = 0

    def draw(self, surface):
        surface.fill(C_BLACK)
        sw, sh = surface.get_size()
        cx = sw // 2

        if self.step == 'title':
            t = title_font_big.render('HOLLOWMERE', True, C_RED)
            surface.blit(t, (cx - t.get_width()//2, sh//3))
            t2 = title_font_small.render('Ein Ort, der auf keiner Karte verzeichnet ist.', True, (100,100,100))
            surface.blit(t2, (cx - t2.get_width()//2, sh//3 + 50))
            t3 = title_font_small.render('[ENTER] Spielen', True, (150,150,150))
            surface.blit(t3, (cx - t3.get_width()//2, sh*2//3))

        elif self.step == 'intro':
            y = sh//4
            for line in self.intro_shown:
                if line == '':
                    y += 10
                    continue
                c = C_RED if line.startswith('Glaub') else (136,136,136)
                t = title_font_small.render(line, True, c)
                surface.blit(t, (cx - t.get_width()//2, y))
                y += 22
            t3 = title_font_small.render('[ENTER] Weiter', True, (80,80,80))
            surface.blit(t3, (cx - t3.get_width()//2, sh - 40))

        elif self.step == 'name':
            t = title_font.render('Wer bist du?', True, (136,136,136))
            surface.blit(t, (cx - t.get_width()//2, sh//3))
            # Input box
            bx = cx - 100
            pygame.draw.rect(surface, (30,30,30), (bx, sh//2-2, 200, 28))
            pygame.draw.rect(surface, C_YELLOW if int(self.cursor_blink/500)%2==0 else (85,85,85), (bx, sh//2-2, 200, 28), 1)
            nt = title_font.render(self.name_input, True, C_WHITE)
            surface.blit(nt, (bx+8, sh//2+2))
            h = title_font_small.render('[ENTER] Bestaetigen', True, (80,80,80))
            surface.blit(h, (cx - h.get_width()//2, sh*2//3))

        elif self.step == 'origin':
            t = title_font.render('Warum bist du hier?', True, (136,136,136))
            surface.blit(t, (cx - t.get_width()//2, sh//4))
            y = sh//3 + 20
            for i, (text, _) in enumerate(self.origins):
                c = C_YELLOW if i == self.origin_sel else (170,170,170)
                prefix = '> ' if i == self.origin_sel else '  '
                t = title_font_small.render(prefix + text, True, c)
                surface.blit(t, (cx - 180, y))
                y += 28

        elif self.step == 'trauma':
            t = title_font.render('Was traegst du mit dir?', True, (136,136,136))
            surface.blit(t, (cx - t.get_width()//2, sh//5))
            y = sh//3
            for i, (text, _) in enumerate(self.traumas):
                c = C_YELLOW if i == self.trauma_sel else (170,170,170)
                prefix = '> ' if i == self.trauma_sel else '  '
                t = title_font_small.render(prefix + text, True, c)
                surface.blit(t, (cx - 180, y))
                y += 28

        elif self.step == 'attrs':
            t = title_font.render('Verteile deine Punkte', True, (136,136,136))
            surface.blit(t, (cx - t.get_width()//2, 30))
            pts = title_font.render(f'Verbleibend: {gs.pts_left}', True, C_YELLOW)
            surface.blit(pts, (cx - pts.get_width()//2, 60))
            y = 100
            for i, name in enumerate(self.attr_names):
                k = self.attr_keys[i]
                v = gs.attrs[k]
                c = C_YELLOW if i == self.attr_sel else (170,170,170)
                sel = '> ' if i == self.attr_sel else '  '
                bar = '#' * v + '.' * (5-v)
                t = title_font_small.render(f'{sel}{name:20s} [{bar}] {v}', True, c)
                surface.blit(t, (cx - 180, y))
                y += 26
            h = title_font_small.render('[Pfeiltasten] Waehlen  [Links/Rechts] Aendern  [ENTER] Start', True, (80,80,80))
            surface.blit(h, (cx - h.get_width()//2, sh - 30))

creation = CreationScreen()

def start_arrival():
    dlg.start([
        {'speaker':'','text':'Du stehst am Ortseingang von Hollowmere. Spaeter Nachmittag.','style':'thought'},
        {'speaker':'','text':'Warmes Licht. Vogelgesang. Alte Haeuser, Blumengaerten. Wie aus einem Bilderbuch.','style':'thought'},
        {'speaker':'','text':'Erkunde den Ort. WASD = Bewegen, LEERTASTE = Interagieren.'},
    ])

# ============================================================
#  HUD
# ============================================================
def draw_hud(surface):
    sw = surface.get_width()
    # Background bar
    pygame.draw.rect(surface, (0,0,0,180), (0,0,sw,24))
    # Mental state
    ms = gs.mental_state
    label = ui_font.render('Mental State:', True, (170,170,170))
    surface.blit(label, (10, 5))
    bx = 110
    pygame.draw.rect(surface, (50,50,50), (bx, 6, 100, 12))
    mc = (70,170,70) if ms > 60 else (200,170,50) if ms > 35 else (170,50,50)
    pygame.draw.rect(surface, mc, (bx, 6, ms, 12))
    pct = ui_font.render(f'{ms}%', True, (200,200,200))
    surface.blit(pct, (bx+104, 5))

    # Day
    day = ui_font.render(f'Tag {gs.day}  {gs.time_of_day}', True, (170,170,170))
    surface.blit(day, (sw - day.get_width() - 10, 5))

# ============================================================
#  RENDER
# ============================================================
water_frame = 0
water_timer = 0

def render_world():
    global water_frame, water_timer

    gw, gh = game_surface.get_size()
    tw = gw // TILE + 2
    th = gh // TILE + 2

    game_surface.fill(C_BLACK)

    # Draw tiles
    for ty in range(th):
        for tx in range(tw):
            mx = int(cam_x) + tx - 1
            my = int(cam_y) + ty - 1
            ch = tile_at(mx, my)
            tn = get_tile_name(ch, mx, my)
            if ch == '~':
                tn = f'water{water_frame}'
            tile = tile_cache.get(tn)
            if not tile:
                continue
            sx = int((mx - cam_x) * TILE)
            sy = int((my - cam_y) * TILE)
            game_surface.blit(tile, (sx, sy))
            ov = get_overlay(ch, mx, my)
            if ov and ov in tile_cache:
                game_surface.blit(tile_cache[ov], (sx, sy))

    # Draw NPCs
    for npc in npcs:
        sx = int((npc.x - cam_x) * TILE)
        sy = int((npc.y - cam_y) * TILE) - 4
        spr = npc.get_sprite()
        if spr:
            game_surface.blit(spr, (sx, sy))

    # Draw player
    sx = int((player.x - cam_x) * TILE)
    sy = int((player.y - cam_y) * TILE) - 4
    spr = player.get_sprite()
    if spr:
        game_surface.blit(spr, (sx, sy))

# ============================================================
#  MAIN LOOP
# ============================================================
def main():
    global water_frame, water_timer
    running = True

    while running:
        dt = clock.tick(60)
        water_timer += dt
        if water_timer > 400:
            water_timer = 0
            water_frame = (water_frame + 1) % 4

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                pass  # handled automatically
            elif event.type == pygame.KEYDOWN:
                if gs.phase in ('title','intro','creation'):
                    creation.handle_key(event)
                elif gs.phase == 'dialogue':
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        if dlg.choices and dlg.done_typing:
                            dlg.pick_choice()
                        else:
                            dlg.advance()
                    elif event.key == pygame.K_UP and dlg.choices:
                        avail = [i for i,c in enumerate(dlg.choices) if not c.get('req') or c['req']()]
                        ci = avail.index(dlg.selected_choice) if dlg.selected_choice in avail else 0
                        dlg.selected_choice = avail[max(0, ci-1)]
                    elif event.key == pygame.K_DOWN and dlg.choices:
                        avail = [i for i,c in enumerate(dlg.choices) if not c.get('req') or c['req']()]
                        ci = avail.index(dlg.selected_choice) if dlg.selected_choice in avail else 0
                        dlg.selected_choice = avail[min(len(avail)-1, ci+1)]
                elif gs.phase == 'playing':
                    if event.key in (pygame.K_SPACE, pygame.K_e):
                        interact()

        # Update
        if gs.phase in ('title','intro','creation'):
            creation.update(dt)
        elif gs.phase == 'playing':
            update_player(dt)
            update_camera()
        elif gs.phase == 'dialogue':
            dlg.update(dt)
            update_camera()

        # Render
        sw, sh = screen.get_size()

        if gs.phase in ('title','intro','creation') and creation.step != 'done':
            creation.draw(screen)
        else:
            render_world()
            # Scale game_surface to screen
            scaled = pygame.transform.scale(game_surface, (sw, sh))
            screen.blit(scaled, (0,0))

            # Vignette (dark edges)
            vig = pygame.Surface((sw, sh), pygame.SRCALPHA)
            for r in range(20):
                alpha = int(r * 3)
                pygame.draw.rect(vig, (0,0,0,alpha), (r*2, r*2, sw-r*4, sh-r*4), 3)
            screen.blit(vig, (0,0))

            # Night overlay
            if gs.time_of_day == 'Nacht':
                night = pygame.Surface((sw,sh), pygame.SRCALPHA)
                night.fill((10,10,40,120))
                screen.blit(night, (0,0))
            elif gs.time_of_day == 'Abend':
                night = pygame.Surface((sw,sh), pygame.SRCALPHA)
                night.fill((10,10,40,50))
                screen.blit(night, (0,0))

            # Horror flicker
            if gs.mental_state < 40 and random.random() < 0.02:
                fl = pygame.Surface((sw,sh), pygame.SRCALPHA)
                fl.fill((139,0,0,20))
                screen.blit(fl, (0,0))

            # HUD
            draw_hud(screen)

            # NPC name labels
            for npc in npcs:
                dx = abs(npc.x - player.x)
                dy = abs(npc.y - player.y)
                if dx < 3 and dy < 3:
                    nx = int((npc.x - cam_x) * TILE * (sw / game_surface.get_width()))
                    ny = int((npc.y - cam_y) * TILE * (sh / game_surface.get_height())) - 20
                    nt = ui_font.render(npc.name, True, C_YELLOW)
                    bg = pygame.Surface((nt.get_width()+8, 16), pygame.SRCALPHA)
                    bg.fill((0,0,0,180))
                    screen.blit(bg, (nx - nt.get_width()//2 + 20, ny))
                    screen.blit(nt, (nx - nt.get_width()//2 + 24, ny + 1))

            # Interact hint
            near = False
            for npc in npcs:
                if abs(npc.x-player.x)<2 and abs(npc.y-player.y)<2: near = True
            if abs(player.x-15.5)<2 and abs(player.y-15.5)<2: near = True
            if near and gs.phase == 'playing':
                ht = ui_font.render('[LEERTASTE] Interagieren', True, C_YELLOW)
                hbg = pygame.Surface((ht.get_width()+12, 18), pygame.SRCALPHA)
                hbg.fill((0,0,0,180))
                screen.blit(hbg, (sw//2 - ht.get_width()//2 - 6, sh - 160))
                screen.blit(ht, (sw//2 - ht.get_width()//2, sh - 158))

            # Dialogue
            dlg.draw(screen)

        pygame.display.flip()

    pygame.quit()

def update_player(dt):
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_w] or keys[pygame.K_UP]: dy = -1; player.dir = 0
    if keys[pygame.K_s] or keys[pygame.K_DOWN]: dy = 1; player.dir = 2
    if keys[pygame.K_a] or keys[pygame.K_LEFT]: dx = -1; player.dir = 1
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: dx = 1; player.dir = 3

    player.moving = dx != 0 or dy != 0
    if player.moving:
        spd = 0.06 * dt
        nx = player.x + dx * spd
        ny = player.y + dy * spd
        cx = int(nx + (0.4 if dx > 0 else -0.4 if dx < 0 else 0))
        cy = int(ny + (0.4 if dy > 0 else -0.4 if dy < 0 else 0))
        if dx != 0 and not tile_solid(tile_at(cx, int(player.y))):
            player.x = nx
        if dy != 0 and not tile_solid(tile_at(int(player.x), cy)):
            player.y = ny
        player.frame_timer += dt
        if player.frame_timer > 200:
            player.frame_timer = 0
            player.frame = (player.frame + 1) % 2
    else:
        player.frame = 0

def interact():
    # Check NPCs
    for npc in npcs:
        if abs(npc.x - player.x) < 2 and abs(npc.y - player.y) < 2:
            # Face player
            if player.x < npc.x: npc.dir = 1
            elif player.x > npc.x: npc.dir = 3
            elif player.y < npc.y: npc.dir = 0
            else: npc.dir = 2
            fn = NPC_DIALOGUES.get(npc.name)
            if fn:
                dlg.start(fn())
            return
    # Check well
    if abs(player.x - 15.5) < 2 and abs(player.y - 15.5) < 2:
        dlg.start(make_well_dialogue())

if __name__ == '__main__':
    main()
