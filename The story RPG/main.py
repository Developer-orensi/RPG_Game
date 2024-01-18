import pygame
from pygame.constants import K_UP
import os

from random import *
######################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()
screen_width = 1280

screen_height = 720
pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("Forgotten Legend") #게임 이름

# FPS
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
################################################################################

# 1. 사용자 게임 초기화(배경화면 , 이미지 , 좌표 , 속도 , 폰트 등)


#2. 폰트 로딩



current_path =  os.path.dirname(__file__)
try:

    background_0_0 = pygame.image.load( os.path.join(current_path , 'background_0.png') )
except:
    print('배경 로딩 에러! 관리자에게 물어보세요')
background_0_1 = pygame.image.load(os.path.join(current_path , 'background_0_1.png'))
background_0_2 = pygame.image.load(os.path.join(current_path , 'background_0_2.png' ))
background_0_3 = pygame.image.load(os.path.join(current_path , 'background_0_3.png'))
background_0_4 = pygame.image.load(os.path.join(current_path , 'background_0_4.png'))
background_0_5 = pygame.image.load(os.path.join(current_path , 'background_0_5.png'))
background_1_0 = pygame.image.load(os.path.join(current_path , 'background_1_0.png'))
background_1_1 = pygame.image.load(os.path.join(current_path , 'background_1_1.png'))
background_1_2 = pygame.image.load(os.path.join(current_path , 'background_1_2.png'))
background_1_3 = pygame.image.load(os.path.join(current_path , 'background_1_3.png'))
background_1__2 = pygame.image.load(os.path.join(current_path , 'background_1_-2.png'))

background_2_0 = pygame.image.load(os.path.join(current_path , 'background_2_0.png'))
background_2_1 = pygame.image.load(os.path.join(current_path , 'background_2_1.png'))
background_2_2 = pygame.image.load(os.path.join(current_path , 'background_2_2.png'))
background_2_3 = pygame.image.load(os.path.join(current_path , 'background_2_3.png'))
background_2_4 = pygame.image.load(os.path.join(current_path , 'background_2_4.png'))
background_2__2 = pygame.image.load(os.path.join(current_path , 'background_2_-2.png'))


backgrounds0 = [  background_0_0 , background_0_1 , background_0_2 , background_0_3, background_0_4, background_0_5]

backgrounds1 = [  background_1_0, background_1_0 , background_1_0, background_1__2 , background_1_0, background_1_0 , background_1_1 , background_1_2, background_1_3 ]

backgrounds2 = [None, None, None, background_2__2, background_2_0, background_2_0, background_2_1, background_2_2, background_2_3, background_2_4, None]






# 캐릭터

character = pygame.image.load(os.path.join(current_path , 'character.png'))

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character_canmove = True


character_xpos = 600
character_ypos = screen_height - 149

tox = 0
toy = 0


# 점프 처리
jump_cnt = 0   # 점프 0번
max_jump_cnt = 3 # 1단 점프까지
dojumped = False

starttick =0
t = 0


characrer_speed = 5

speedup = 0
speeddown = 0

##### 스테이지

stage = 0
sector = -5
max_sector = [  0 , 3 , 5 , 7 ]
player_sector = 5
sectortext = ""
quest_progress = 0

# 각 스테이지마다 섹터 존재
# 0섹터 스폰
# -1섹터는 휴식 구역
# -2 섹터는 상점 구역
# -5 섹터 ~ 맥스 섹터까지 존재함.

# Shop

tutorial_buyer = 1


shop_name = { 0 : None, 1 : '최하급 체력 포션' , 2: '최하급 마력 포션' , 3: '하급 체력 포션', 4: '하급 마력 포션' , 5 : None, 6:None, 7 : None, 8 : None }

shop_have ={0: None, 1 : 0 , 2: 0 , 3 : 0, 4:0, 5:0, 6: 0 , 7 : 0 , 8 : 0 }


shop_price = {0: 0 ,1 : 50 , 2 : 50 , 3 : 150, 4:150, 5: 200, 6:0, 7:0, 8:0}


shop_description = {0 : "" , 1 : '설명 : 질이 낮은 포션이다. 마시면 체력을 15 회복해준다.' ,\
                     2 : "설명 : 질이 낮은 포션이다. 마시면 마력을 8 회복해준다."\
                        ,3 : "설명 : 상점제 흔한 체력 포션. 마시면 체력을 60 회복해준다."
                        , 4 : '설명 : 상점제 흔한 마력 포션. 마시면 마력을 20 회복해준다.', 5 : None, 6:None, 7 : None, 8 : None
                        }


shop_showing = 1

shop_buylimit = {0 : 0,1: -1 , 2: -1 , 3: 1, 4:0, 5: 0 , 6 : 0 , 7 : 0 , 8 : 0 }






items = {'오크의 핵' : 1, '슬라임의 핵' : 0}

items_code = {0 : '오크의 핵', 1 : '슬라임의 핵'}


shop_button_buy = pygame.image.load(os.path.join(current_path, 'shop_button_1.png'))

shop_button_pos = (850, 450)
shop_button_pos_max = (850+80, 450+80)


slot1 = 0
slot2 = 0
slot3 = 0 
slot4 = 0

















iselite = False






# 스테이터스

###########################

# 힘 , 방어력 ,  체력 , 지능 
# 4대 스탯 + a

strength = 1

hpp = 1

max_hp = 100

hp = 100

defense = 1

dmgreduction = 1

intelligence = 1

max_hp = 100

mp = 10
max_mp = 10

level = 1

exp = 0

coin = 5000

dimension_int = 1  # 차원 간섭력

dimnesion_activated = True # 차원 간섭력 활성화?


state_abnormality = {'구속' : 0, '신속' : 0, '독' : 0 }

state_duration = {'구속' : 0, '신속' : 0, '독' : 0}


texty = ''
self_restore = True

isbloody = False

slotshowing = False





# 스테이터스 메시지
life = 5

message_activated = False

message_text = ''









levelup_exp = [ 0 , 2 , 5 , 7 , 10 , 15 , 18 , 30 , 35 , 40  # 10 레벨                 
               , 47 ,55 , 67 , 70 , 82 , 88 , 90 , 94 , 100,100, # 20 레벨
                 105 , 120 , 135 , 140 , 155 , 160 , 177 , 180 , 188 , 200, # 30 레벨
                    250, 300, 380 , 400, 440, 480, 550, 580 , 600, 700, # 40 레벨
                        800, 850,875 , 900, 920, 940, 960, 980, 999, 1500, # 50 레벨
                            900, 910, 930, 950, 960, 980, 1000, 1020, 1050, 1200] # 60레벨




# 잔여 스탯 P
remain_statpoint = 0



#퀘스트

quest_text = ''




# 플레이서 발사체

character_atk = pygame.image.load( os.path.join( current_path ,"character_atk.png"))


character_atk_size = character_atk.get_rect().size

character_atk_width = character_atk_size[0]
character_atk_height = character_atk_size[1]



character_atk_xpos = character_atk_ypos = 0
character_atk_current_xpos = character_xpos
character_tox = 5

character_atk_do_exist = False

character_atk_direction = 0

character_skill1_level = 1

character_skill1_exp = 0
character_skill1_exp_require = [0, 2, 8, 15, 20, 32, 90, 120, 240, 900, 300, 380]

blitingskill1 = False


################################## 킬카운트 ##############

stage1_killcount = {'고블린': 0 , '홉고블린': 0}

############################### 적들

heosuabi = pygame.image.load( os.path.join( current_path ,"허수아비.png"))
heosuabi_hp = 5
heosuabi_do_exist = True

###########################stage 1##############

################################################# 대화 창

conversation = pygame.image.load( os.path.join( current_path ,"conversation.png"))
conversation_text = None
isconversation = False

conversation_progress = 0





################################ 섹터 I. 슬라임 #############

slime = pygame.image.load(os.path.join(current_path , 'enemy_1_slime.png'))

slime_clear = False

# NPC

npc_stage1 = pygame.image.load(os.path.join(current_path , 'npc_1.png'))


############################# 섹터2
# 섹터2에 가보았다.
stage1_dovisitsector_2 = False


#### 섹터2 적

goblin_1 = pygame.image.load(os.path.join(current_path , 'enemy_2_goblin.png'))





goblin_1_status = {  'atk' : 10 , 'mhp' : 35 , 'hp': 35 , 'speed' : 1.5}

goblin_1_level = 2
goblin_1_xpos = 1000
goblin_1_ypos = 720 - 150
goblin_1_doexist = False

goblin_1_killcount = 0

goblin_regen_time = 0


goblintext = None

############# 섹터 III

hop_goblin = pygame.image.load(os.path.join(current_path , 'enemy_3_hopgoblin.png'))
hop_goblin_state = {'hp' : 1280 , 'atk' : 45 , 'dmgreduction' : 0.5 , 'speed' : 2.3 , 'doexist' : True}

hop_goblin_xpos = 1100


# 히든피스 (Stage 1)

#/* 힌트 발동 조건 : 에단에게 말 걸기 5회[1]  >> -2구역에서 상자 구매 >> 0 구역에서 에단에게 말걸기 
# >> 고블린 킬카운트 40 >> -3구역에서 연구실 열쇠 생성 >> -5 구역 진입시 미니게임('리듬게임') >> 클리어시 에단
#에게 가서 보상 수령하기..

# 보상 : 영구적으로 올스탯 + 20 , [에단의 풋볼] 아이템 획득(착용시 MP 10% 증폭)

hiddenpiece_1_progress = 0 # 8

hiddenpiece_1_1_count = 0 # 말걸기
hiddenpiece_1_5_key = False
hiddenpiece_1_6_rhythm_clear = False 




#









# 포탈

portal = pygame.image.load(os.path.join(current_path , 'portal.png'))


portal_activated = False



# Stage II

# NPC_2

npc_stage2 = pygame.image.load(os.path.join(current_path , 'npc_2.png'))


# 오크

oak_2 = pygame.image.load(os.path.join(current_path , 'enemy_4_oak.png'))

oak_state = { 'max_hp' : 980 , 'hp' : 980 , 'atk' : 75, 'doexist' : True , 'speed' : 2, 'killed' : 9}

oak_xpos = 1100
# 120 * 200

oak_respawnevent = pygame.event.Event(pygame.USEREVENT + 1)

oak_attackevent = pygame.event.Event(pygame.USEREVENT + 2)

# ** 오크와 관련한 이벤트




# Sector III - stage II

# 일단은 '슬라임' 
slime_2 = pygame.image.load(os.path.join(current_path, 'enemy_5_crackslime.png'))


# 슬라임 기본 스탯

slime_2_state = {  'xpos' : 800  , 'ypos' : 720-61 ,'max_hp' : 640 , 'atk' : 30 , 'flyeratk' : 60, 'doexist' : True, 'speed' : 2 , 'slowcnt' : 0, 'killed' : 0,'hp' : 640}

slime_2_active = True


slime_2_flyer = pygame.image.load(os.path.join(current_path , 'enemy_flyer_5_slimeflyer.png'))

slime_2_flyer_state = {'xpos' : 800 , 'ypos' : 500 , 'dowxist' : False, 'direction' : 0}




kingslime = pygame.image.load(os.path.join(current_path, 'enemy_6_kingslime.png'))



kingslime_state = {'doexist' : True, 'xpos' : 1280-50, 'ypos' : 200 , 'atk' : 120 , 'hp' : 120 , 'life' : 2, 'killed' : 0,'hitcount' : 0}


kingslime_laser_slow = pygame.image.load(os.path.join(current_path , 'enemy_laser_1_slow.png'))
kingslime_laser_heal = pygame.image.load(os.path.join(current_path , 'enemy_laser_1_heal.png'))


kingslime_laser_xpos = 0

kingslime_laser_count = 0

kingslime_laser_exist = False

kingslime_laser_damage = False


laser_type = 0


space_time = pygame.time.get_ticks()

conversation_progress =0


#Sound 설정







# Font 설정



errfont = pygame.font.Font(None, 40)


try:
    font = pygame.font.Font(os.path.join(current_path , 'UnGraphicBold.ttf') , 30)




except :
    print("알수 없는 에러!  텍스트가 깨질 수 었습니다!")
    font = errfont


else:
    print('폰트 로딩중..... 성공!')
    









def backgroundblit():
    global character_xpos , character_ypos , stage , sector

    if stage == 0:


        screen.blit(backgrounds0[sector+5] , (0,0))


    if stage == 1:
        screen.blit(backgrounds1[sector+5], (0,0))


    if stage == 2:
        screen.blit(backgrounds2[sector+5] , (0,0))




    screen.blit(character , (character_xpos , character_ypos))


def char_moveto():
    global character_xpos , character_ypos , tox , toy

    

    character_xpos += tox
    character_ypos -= toy
    

def char_jumpcode():
    global character_xpos , character_ypos , tox , toy, jump_cnt , max_jump_cnt, space_time,t,dojumped,starttick
    if jump_cnt < max_jump_cnt:
        jump_cnt += 1
        

        space_time = pygame.time.get_ticks()

      
        space_time = pygame.time.get_ticks()
        t = pygame.time.get_ticks()
        dojumped = True
        starttick = pygame.time.get_ticks()









def char_jumpto():
    global character_xpos , character_ypos , tox , toy, jump_cnt , max_jump_cnt , space_time , t, dojumped
    if  dojumped == True:

        t_last = (space_time - starttick)/ 1000


        t = (pygame.time.get_ticks() - starttick) / 1000
        space_time = pygame.time.get_ticks() 

        toy  =   ((30*t - 40*(t**2)) - (30*t_last - 40*(t_last**2))) * 50



        
# 화면 나감 처리 함수
def sectorleft():
    global sector , stage , max_sector , character_xpos, character_width

    if sector > -5 :
        sector -= 1  # -5 섹터까지
        character_xpos = screen_width -  character_width - 0.1  


    else:
        character_xpos = 0

    
def sectorright():
    global sector ,slime_2_active, stage , max_sector , character_xpos, character_width, player_sector , sectortext, stage1_dovisitsector_2
    if stage == 0:
        if sector < player_sector and sector < max_sector[stage]:
            sector += 1
            character_xpos = 0

        elif sector == player_sector and sector == max_sector[stage] and heosuabi_do_exist == False:
            sector = 0
            stage = 1
            character_xpos = 1280 / 2 + character_width / 2
            player_sector = 1
        
        else:
            character_xpos = screen_width - character_width
    
    elif stage == 1:
        ####################### 스테이지 1

        if sector < 0:
            sector += 1
            character_xpos = 0


        elif sector == 0:
            sector = 1
            character_xpos = 0

        elif sector == 1 and player_sector > 1:
            sector = 2
            stage1_dovisitsector_2 = True
            character_xpos = 0
        elif sector == 2 and player_sector > 2:
            sector = 3

            character_xpos = 0
        

        

        else:
            character_xpos = screen_width - character_width
  
    elif stage == 2:

        if sector < 0:
            sector += 1
            character_xpos = 0


        elif sector == 0:
            sector += 1
            character_xpos = 1
            if player_sector == 1:
                player_sector = 2

        elif sector == 1 and player_sector > 1:
            sector += 1
            character_xpos = 1
        
        elif sector == 2 and player_sector > 2:
            sector += 1
            character_xpos = 1
            slime_2_active = True


        elif sector == 3 and player_sector > 3:
            sector = 4
            character_xpos = 1
            

            
            



    
        else:
            character_xpos = screen_width - character_width



def charatk():  # 공격
    global character_xpos , character_atk_current_xpos, character_atk_do_exist , character_atk_xpos , character_atk_direction , character_atk_ypos , character_ypos

    character_atk_xpos += 8 * character_atk_direction
    character_atk_ypos = character_ypos

    # 나감 처리
    if abs(character_atk_current_xpos - character_atk_xpos) >= 140:
        character_atk_do_exist = False







def stage0_enemy():
    global heosuabi_hp, heosuabi_do_exist , player_sector
    if heosuabi_hp <= 0:
        heosuabi_do_exist = False
        player_sector = 0
    
    


def buy():

    global tutorial_buyer , hp ,mp , hpp , intelligence , strength


    if stage == 0:
        if tutorial_buyer == 1:
            tutorial_buyer = 0
            intelligence += 1
            print("지능 + 1")



    if stage != 0:

        pass





def statebar():
    global hp, mp, max_hp, max_mp , level, self_restore, isbloody

    if self_restore:

        if hp >= max_hp / 5 and hp < max_hp+50:  # 체력 20% 이상일때

            statusbar = font.render(  '[Lv. {}] HP : {} / {} , MP : {} / {}  [미분배 스탯 포인트: {}]'.format(level,int(hp), max_hp , int(mp),max_mp,remain_statpoint) , True ,(0,0,0)   )
            screen.blit(statusbar, (10,0))
            isbloody = False
        
        if hp < max_hp /5  :
            statusbar = font.render(  '[경고!!] HP : {} / {} , MP : {} / {}  [미분배 스탯 포인트: {}]'.format( int(hp), max_hp,int(mp),max_mp,remain_statpoint) , True ,(255,0,0)   )
            screen.blit(statusbar , (10,0))
            isbloody = True


        if hp>= max_hp+50:
            statusbar = font.render(  '[Lv. {}] HP : {} / {} , MP : {} / {}  [미분배 스탯 포인트: {}]'.format(level,int(hp), max_hp , int(mp),max_mp,remain_statpoint) , True ,(255,255,0)   )
            screen.blit(statusbar, (10,0))
            isbloody = False 





    else:
        if hp < max_hp /5 :
            statusbar = font.render(  '[경고!!] HP : {} / {} , MP : {} / {}  [미분배 스탯 포인트: {}]'.format( int(hp), max_hp,int(mp),max_mp,remain_statpoint) , True ,(255,0,0)   )
            screen.blit(statusbar , (10,0))
        else:
            statusbar = font.render(  '[Lv. {}] HP : {} / {} , MP : {} / {}  [미분배 스탯 포인트: {}]'.format(level,int(hp), max_hp , int(mp),max_mp,remain_statpoint) , True ,(0,0,0)   )
            screen.blit(statusbar, (10,0))
            isbloody = False







def statusbar():
    global hpp, intelligence , defense , strength , exp , levelup_exp, dimnesion_activated, dimension_int
    if not dimnesion_activated:
        statusbar = font.render('힘 : {} ,  방어력 : {} , 체력 : {} , 마력 : {}, 경험치 : {} / {}'.format(strength , defense , hpp , intelligence, exp , levelup_exp[level]) , True, (0,0,0) )
        screen.blit(statusbar , (10, 40))
    if dimnesion_activated:
        statusbar = font.render('힘 : {} ,  방어력 : {} , 체력 : {} , 마력 : {}, 경험치 : {} / {}, [차원 간섭력 : {}]'.format(strength , defense , hpp , intelligence, exp , levelup_exp[level],dimension_int) , True, (0,0,0) )
        screen.blit(statusbar , (10, 40))



def message(string):
    global message_activated, message_text
    message_text = string
    message_activated = True
    pygame.time.set_timer(pygame.USEREVENT + 7, 2000 , 1)








quest_progress  =  0
conversation_progress = 0


def quest():
    global quest_progress,exp, conversation_progress, conversation_text,max_jump_cnt, isconversation , stage1_dovisitsector_2 , goblin_1_killcount
    global player_sector , portal_activated, hiddenpiece_1_1_count,hiddenpiece_1_5_key,hiddenpiece_1_6_rhythm_clear,hiddenpiece_1_progress
    global items, items_code, oak_state, iselite
    global coin, level, message_activated, message_text, dimension_int, dimnesion_activated, speedup, speeddown, state_duration, state_abnormality
    
    
    if stage == 1:
        if quest_progress == 0:

            if conversation_progress == 0:
                conversation_progress += 1
                conversation_text = '혹시 모험가니? [LShift로 진행]'
            elif conversation_progress == 1:
                conversation_progress += 1
                conversation_text = '반가워, 나는 이곳을 돌아다니는 주민 중 한명인 에단이야.'
        
            elif conversation_progress == 2:
                conversation_progress += 1
                conversation_text = '근데 요즘 1구역에서 슬라임 하나가 난동을 부린다고 하더라고'
            elif conversation_progress == 3:
                conversation_text = '그래서 그 슬라임을 잡아줬으면 좋겠어'
                conversation_progress += 1
            elif conversation_progress == 4:
                conversation_progress = 0
                quest_progress = 1
                # 퀘스트 프로그레스 1개 늘리기, 대회 끝
                isconversation = False


        if quest_progress == 1 and slime_clear == False :
            k = randint(1,6)
            if k == 1:
                conversation_text = '슬라임을 잡고 날 불러줘'
                
            elif k == 2:
                conversation_text = '갑자기 슬라임이 나타난 것은 뭐 때문일까?'
            
    
            elif k == 3:
                conversation_text = '...'
                
            
            elif k == 4 or k == 5:
                conversation_text = '......'
                
            
            elif k == 6:
                conversation_text = '열쇠가 어디 있더라..?'

            pygame.time.set_timer(pygame.USEREVENT , 3000, 1)
            


        if slime_clear == True and quest_progress == 1:
            
            if conversation_progress == 0:
                stage1_dovisitsector_2 = False
                conversation_text = '고마워! 슬라임을 박멸했구나![Lshift]'
                conversation_progress += 1
            elif conversation_progress == 1:
                conversation_text = '그런데 너는 왜 슬라임이 출몰하는지 알아?'
                conversation_progress += 1
            elif conversation_progress == 2:
                conversation_text = '음... 나는 약해서 1구역 이상 가본적이 없는데..'
                conversation_progress += 1

            elif conversation_progress == 3:
                conversation_text = '혹시 2구역에 한번 가 볼수 있어?'
                conversation_progress += 1
            elif conversation_progress == 4:
                conversation_text = '이제 너도 자격이 되어 2구역에 갈 수 있을거야'
                conversation_progress += 1

            elif conversation_progress == 5:

                isconversation = False
                conversation_progress = 0
                quest_progress += 1


        if quest_progress == 2 and stage1_dovisitsector_2 == False:
            k = randint(1,7)

            if k == 1:
                conversation_text = '그나저나 내 열쇠는 대체 어디로 간거지...?'

            elif k == 2:
                conversation_text = '2구역에 갔다 온거야?? 아니라고...?'

            elif k == 2:
                conversation_text = '2구역에는 원래 고블린이 살고 있었는데..'
            elif k == 3:
                conversation_text = '다른 친구들은 어떻게 될려나..?'
            elif k == 4:
                conversation_text = '고블린....'
            elif k >4 and k <= 7:
                conversation_text = '2구역에 갔다 온거야?? 아니라고...?'

            pygame.time.set_timer(pygame.USEREVENT , 2500 , 1)
        if quest_progress == 2 and stage1_dovisitsector_2 == True:
            if conversation_progress == 0:
                conversation_text = '2구역에 갔다 왔구나![Lshift]'
                conversation_progress += 1
            elif conversation_progress == 1:
                conversation_text = '너가 슬라임을 잡아주면서 내 기억도 조금 돌아온것 같아'
                conversation_progress += 1
            elif conversation_progress == 2:
                conversation_text = '2구역에 있는 고블린을 잡아줄 수 있어?'
                conversation_progress += 1
            elif conversation_progress == 3:
                conversation_text = '그나저나 앞으로의 여정에는 2단 점프가 필요할 거야'
                conversation_progress += 1
            elif conversation_progress == 4:
                conversation_text = '이제부터 2단 점프를 할 수 있을 거야!'
                conversation_progress += 1
                max_jump_cnt = 2
            elif conversation_progress == 5:
                isconversation = False
                conversation_progress = 0
                quest_progress += 1
        

        if quest_progress == 3 and goblin_1_killcount < 7:
            if goblin_1_killcount == 0:
                conversation_text = '혹시 스탯 분배를 못하는거야? 1,2,3,4로 분배할 수 있어!'

            elif goblin_1_killcount != 0:
                conversation_text = F'{7 - goblin_1_killcount}마리의 고블린을 더 잡아줘!'

            pygame.time.set_timer(pygame.USEREVENT , 2500 , 1 )
        if quest_progress == 3 and goblin_1_killcount >= 7:
            if conversation_progress == 0:
                conversation_progress += 1
                conversation_text = '고블린을 잡아왔구나![Lshift]'
                exp += 8

            elif conversation_progress == 1:
                conversation_progress += 1
                conversation_text = '혹시 고블린이 좀 더 흉포해진걸 봤어?'
            
            elif conversation_progress == 2:
                conversation_progress += 1
                conversation_text = '원래 고블린은 동족 7마리가 잡히면 더 강해지는 습성이 있어'

            elif conversation_progress == 3:
                conversation_progress += 1
                conversation_text = '이젠 너가 여기 있을 시간도 얼마 남지 않았네...'
            elif conversation_progress == 4:
                conversation_progress += 1
                conversation_text = '좀더 흉포한 고블린을 잡아 줄 수 있어?'
            elif conversation_progress == 5:
                conversation_progress = 0
                quest_progress += 1
                isconversation = False
        if quest_progress == 4 and goblin_1_killcount < 15:
            k = randint(1,5)
            if k == 1:

                conversation_text = '생각이... 날것같은데..'

            elif k == 2:
                conversation_text = '그 아이템이 있었지...'

            elif k == 3:
                conversation_text = '뭐였더라...?'
            else:
                conversation_text = '......'

            pygame.time.set_timer(pygame.USEREVENT, 1500, 1)
        
        if quest_progress == 4 and goblin_1_killcount >= 15:
            if conversation_progress == 0:
                conversation_progress += 1
                conversation_text = '잘했어! [Shift 로 진행]'
                exp += 40
                player_sector = 3
            elif conversation_progress == 1:
                conversation_progress += 1
                conversation_text = '이제 진짜 얼마 남지 않았어'
            elif conversation_progress == 2:
                conversation_progress += 1
                conversation_text = '사실 이곳에는 구역이 한곳 더 있어'
            elif conversation_progress == 3:
                conversation_progress += 1
                conversation_text = '지금까지는 너가 너무 약해서 보내지 않은 거지만...'
            elif conversation_progress == 4:
                conversation_progress += 1
                conversation_text = '이 정도면 충분할 것 같네'
            elif conversation_progress == 5:
                conversation_progress += 1
                conversation_text = '고블린의 상위종인 홉고블린이라고 들어봤어?'
            elif conversation_progress == 6:
                conversation_progress += 1
                conversation_text = '고블린보다 월등히 강하고, 불리하면 조금씩 도망칠 줄도 알지'

            elif conversation_progress == 7:
                conversation_progress += 1
                conversation_text = '아마 홉고블린이 원인이지 않을까?'
            elif conversation_progress == 8:
                conversation_progress += 1
                conversation_text = '고블린을 20마리정도 처치하면 다음으로 갈 수 있는 길이 열릴거야'
            elif conversation_progress == 9:
                conversation_progress += 1
                conversation_text = '이게 내가 너한테 주는 마지막 임무야'
            elif conversation_progress == 10:
                conversation_progress += 1
                conversation_text = '나중에 다시 만날수도 있겠지'
            elif conversation_progress == 11:
                conversation_progress += 1
                conversation_text = '그럼 마지막 임무를 수행해 줘!'
            elif conversation_progress == 12:
                conversation_progress = 0
                isconversation = False
                quest_progress += 1
        if quest_progress == 5 and hop_goblin_state['doexist'] == True:
            conversation_text = '......'
            pygame.time.set_timer(pygame.USEREVENT , 1000 , 1)
        if quest_progress == 5 and hop_goblin_state['doexist'] == False:
            if conversation_progress == 0:
                conversation_text = '홉 고블린을 처치했구나!'
                conversation_progress += 1
                exp += 300

            elif conversation_progress == 1:
                conversation_text = '너도 이제 어느정도 성장한 것 같네'
                conversation_progress += 1
            elif conversation_progress == 2:
                conversation_text = '이 구역에서는 홉고블린이 제일 강해'
                conversation_progress += 1
            elif conversation_progress == 3:
                conversation_text = '너도 더 성장하려면 다른 구역을 가야지'
                conversation_progress += 1
            elif conversation_progress == 4:
                conversation_text = '2스테이지로 향하는 차원문을 열어줄게'
                conversation_progress += 1
            elif conversation_progress == 5:
                conversation_text = '그곳에 나 말고 다른 누가 있을거야'
                conversation_progress += 1
            elif conversation_progress == 6:
                conversation_text = '나도 그곳을 가본 적은 없지만 그곳이 더 위험하다고'
                conversation_progress += 1
            elif conversation_progress == 7:
                conversation_text = '맞다! 그곳에 가면 주의해야 할게 있어!'
                conversation_progress += 1
            elif conversation_progress == 8:
                conversation_text = '다음 스테이지에 나오는 몬스터부터는 투사체를 던지기 시작해'
                conversation_progress += 1
        
            elif conversation_progress == 9:
                conversation_text = '지금처럼 쉽지는 않다는 말이지'
                conversation_progress += 1
        
            elif conversation_progress == 10:
                conversation_text = '그럼 다음으로 가는 포탈을 열어줄게'
                conversation_progress += 1
        
            elif conversation_progress == 11:
                quest_progress = 6
                conversation_text = ''
                conversation_progress = 0
                portal_activated = True
                ############ 1스테이지 종료 #############
            
        if quest_progress == 6 and stage == 1:
            if hiddenpiece_1_1_count < 5:
                conversation_text = '왜 자꾸 부르는 거야? 포탈을 타고 2스테이지로 넘어가!'
                pygame.time.set_timer(pygame.USEREVENT , 1000 , 1)
                hiddenpiece_1_1_count += 1
            if hiddenpiece_1_1_count == 5:
                conversation_text = '궁금한게 있니?'
                pygame.time.set_timer(pygame.USEREVENT , 1000 , 1)
                hiddenpiece_1_1_count += 1
            if hiddenpiece_1_1_count == 6:
                conversation_text = '왼쪽 구역은 괜찮을려나..?'
                pygame.time.set_timer(pygame.USEREVENT , 1000 , 1)
                quest_progress = 7
                

        if quest_progress == 7 and stage == 1 and shop_have[3] == 1:
            if conversation_progress == 0:
                conversation_text = '왜 아직도 안가고있....어?'
                conversation_progress += 1
            
            elif conversation_progress == 0:
                conversation_text = '혹시 그거 열쇠 아니야?'
                conversation_progress += 1  
    ################ 이곳부터는 스테이지 2 입니다.
    if stage == 2:
        if quest_progress < 10:
            if conversation_progress == 0:
                conversation_text = '이곳은 무슨 일이니? [Lshift]'
                conversation_progress += 1  


            elif conversation_progress == 1:
                conversation_text = "혹시 '차원 간섭력'에 대해 들어 보았니?"
                conversation_progress += 1


            elif conversation_progress == 2:
                conversation_text = '차원 간섭력은 말 그대로 간섭을 할수 있는 것이지.'
                conversation_progress += 1
                            
            elif conversation_progress == 3:
                conversation_text = '차원 간섭력은 스탯이기도 하지만, 소모하면 영구히 사라지는 스탯이야.'
                conversation_progress += 1

            elif conversation_progress == 4:
                conversation_text = '...'
                conversation_progress += 1

            elif conversation_progress == 5:
                conversation_text = '너가 지나쳐온 곳과 이곳은 완전히 다르다고 보면 돼.'
                conversation_progress += 1

            elif conversation_progress == 6:
                conversation_text = '이곳부터는 위험도가 말 그대로 급상승한다고.'
                conversation_progress += 1

            elif conversation_progress == 7:
                conversation_text = '아무튼... 너가 할 일을 알려줄게'
                conversation_progress += 1

            elif conversation_progress == 8:
                conversation_text = '일단 바로 옆에 있는 균열의 흔적이라도 보고 와. 나머지 얘기는 나중에 해줄게'
                conversation_progress += 1

            elif conversation_progress == 9:
               
                conversation_progress = 0
                quest_progress = 11
                isconversation = False


        elif quest_progress == 11 and player_sector < 2:
            conversation_text = '설마 아직도 못간거야?'
            
            pygame.time.set_timer(pygame.USEREVENT , 3000 , 1)

        elif quest_progress == 11 and player_sector >= 2:
            if conversation_progress == 0:
                conversation_text = '너가 가본 그곳은...'
                conversation_progress += 1
            elif conversation_progress == 1:
                conversation_text = '차원의 균열이 시작되려고 하는 중인 곳이야.'
                conversation_progress += 1
            elif conversation_progress == 2:
                conversation_text = '그중에서도 그정도면 상황이 양호한 편에 속하지'
                conversation_progress += 1
            elif conversation_progress == 3:
                conversation_text = '차원의 균열은 메인 균열을 중심으로 해서 전개되는거야'
                conversation_progress += 1
            elif conversation_progress == 4:
                conversation_text = '너가 지나쳐 온 곳은 균열이 아예 발생하지 않았던 곳이고..'
                conversation_progress += 1
            elif conversation_progress == 5:
                conversation_text = '지금 여기도 메인 균열로부터는 멀리 떨어져 있지'
                conversation_progress += 1
            elif conversation_progress == 6:
                conversation_text = '메인 균열은 또 입구와 최상층부부터 최하층부, 심층부, 중심으로 이루어져 있어'
                conversation_progress += 1
            elif conversation_progress == 7:
                conversation_text = '지금까지는 2단점프만으로 충분했다면...'
                conversation_progress += 1
            elif conversation_progress == 8:
                conversation_text = '앞으로 너가 몬스터들과 싸우려면 2단 점프만으로는 부족할거야'
                conversation_progress += 1
            elif conversation_progress == 9:
                conversation_text = '3단 점프를 할수 있게 해줄게'
                conversation_progress += 1
                max_jump_cnt = 3
            
            elif conversation_progress == 9:
                conversation_text = '2구역에서 오크를 8마리정도 잡아줘, 그리고 오크의 핵을 하나 구해줘'
                conversation_progress += 1

            elif conversation_progress == 10:
                conversation_text = '맞다, 아이템에 대한 설명을 아직 안 해줬구나'
                conversation_progress += 1
            
            elif conversation_progress == 11:
                conversation_text = '여기서부터는 몬스터를 잡으면 가끔 아이템이 나와'
                conversation_progress += 1
            elif conversation_progress == 12:
                conversation_text = '오크의 핵은 오크를 잡다보면 나올거니까 걱정하지마'
                conversation_progress += 1
            
            elif conversation_progress == 13:
                conversation_text = ''
                conversation_progress = 0
                isconversation = False
                quest_progress = 12

        elif quest_progress == 12 and not(oak_state['killed'] >=8 and items['오크의 핵'] >= 1):
            print('ln ')
            




        elif quest_progress == 12 and oak_state['killed'] >=8 and items['오크의 핵'] >= 1:
          
            if conversation_progress == 0:
                
                if oak_state['killed'] >= 16 and items['오크의 핵'] >= 2:
                    conversation_text = '훌륭해! 시킨 것보다 너가 더 많이 할줄은 몰랐네'
                    coin += 1000
                    exp += 2000
                    message_text = '         퀘스트를 훌륭하게 완수해, 1000코인과 2000 경험치를 얻었습니다.'
                    message_activated = True
                    pygame.time.set_timer(pygame.USEREVENT + 7, 2000, 1)
                    
                    iselite = True
                    


                else:
                    conversation_text = '진짜 핵을 가져왔네'
                   
                    coin += 400
                    exp += 500
                    message(' 퀘스트를 완료하여, 400 코인과 500 경험치를 얻었습니다.')

                    iselite = False
                
                conversation_progress += 1
            elif conversation_progress == 1:
                conversation_text = '차원 간섭력이라고 내가 전에 얘기했는데...'
                conversation_progress += 1

            elif conversation_progress == 2:
                conversation_text = '사실 그것을 오픈하려면 핵이 필요하거든'
                conversation_progress += 1
            
            elif conversation_progress == 3:
                if iselite:
                    conversation_text = '너가 핵을 많이 가져와서 너는 시작 스탯이 높을거야'
                else:
                    conversation_text = '핵을 가져왔으니 차원 간섭력으로 바꿔 줄게'
                conversation_progress += 1
            
            elif conversation_progress == 4:
                if iselite and items['오크의 핵'] <= 5:
                    conversation_text = '너의 시작 스탯은.... {}야'.format(items['오크의 핵'])
                    message('특수 스탯, [차원 간섭력]이 해금됩니다! 당신의 시작 스탯은 {}입니다.'.format(items['오크의 핵']))
                    dimnesion_activated = True
                    dimension_int = items['오크의 핵']

                    items['오크의 핵'] = 0
                    conversation_progress += 1


                elif iselite and items['오크의 핵'] > 5:
                    conversation_text = '너의 시작 스탯은... 6이야. 더이상으로는 내가 올리지 못해'
                    dimnesion_activated = True
                    dimension_int = 6
                    message('특수 스탯, [차원 간섭력]이 해금됩니다! 당신의 시작 스탯은 6입니다.')
                    items['오크의 핵'] -= 6
                    conversation_progress += 1
                
                else:
                    conversation_text = '너의 시작 스탯은 1이야.'
                    dimnesion_activated = True
                    dimension_int = 1
                    message('특수 스탯, [차원 간섭력]이 해금됩니다. 당신의 시작 스탯은 1입니다.')
                    items['오크의 핵'] -= 1
                
                    conversation_progress += 1
                quest_progress += 1



        elif quest_progress == 13:

            if conversation_progress == 5:
            
                conversation_text = '이제 [차원 간섭력] 부여가 끝났어.'
                conversation_progress += 1
                
            elif conversation_progress == 6:
                conversation_text = '[차원 간섭력]은 궁극기를 쓸때 필요한 기술이야.'
                conversation_progress += 1
            elif conversation_progress == 7:
                conversation_text = 'R 버튼을 누르면 궁극기를 쓸 수 있어'
                conversation_progress += 1
                
            elif conversation_progress == 8:
                conversation_text = '사용할 때 마다 차원 간섭력은 영구적으로 소멸하니 신중히 써줘!'
                conversation_progress += 1
                
            elif conversation_progress == 9:
                conversation_text = '그럼 이제 궁극기도 배웠으니까... 그 다음 구역으로 가볼래?'
                conversation_progress += 1

            elif conversation_progress == 10:
                conversation_text = '그 다음에 있는 구역은 균열 슬라임과 킹슬라임이 살아'
                conversation_progress += 1
            elif conversation_progress == 11:
                conversation_text = '슬라임은 느려지는 디버프가 성가신 편이지.'
                conversation_progress += 1
            elif conversation_progress == 12:
                conversation_text = '그리고 슬라임킹한테는 다가가지 않는것을 추천할게'
                conversation_progress += 1
            elif conversation_progress == 13:
                conversation_text = '지금 너의 상태로는 1도 데미지를 주기 힘들어'
                conversation_progress += 1
            elif conversation_progress == 14:
                conversation_text = '대신에, 킹슬라임은 부하 슬라임이 처치되었을 때 생명력을 소진해'
                conversation_progress += 1
            elif conversation_progress == 15:
                conversation_text = '그리고 저번처럼 슬라임을 잡다 보면, 슬라임의 핵이 나올거야'
                conversation_progress += 1
            elif conversation_progress == 16:
                conversation_text = '그걸 가지고 오면 될거야'
                conversation_progress += 1
            elif conversation_progress == 17:
                conversation_text = '...'
                conversation_progress = 0
                isconversation = False
                quest_progress = 14    

        elif quest_progress == 14 and items['슬라임의 핵'] < 2:
            conversation_text = '...'
            pygame.time.set_timer(pygame.USEREVENT + 6, 2000, 1)
            
        elif quest_progress == 14 and items['슬라임의 핵'] >= 2:
            pass
            
            




   

def questbar(R,G,B):
    global sectortext
    secbar = font.render(sectortext, True, (R,G,B))
    screen.blit(secbar, (10,120))


def sectortext_():
    global stage, sector, stage1_killcount, sectortext
    global items, items_code, oak_state

    if stage == 1:
        if sector == 0:

            sectortext = ' [Stage 1] 휴식 구역 '
            questbar(0,0,0)

        if sector == 1:
            sectortext = '[Stage 1 - 1] 슬라임 출몰 구역'
            questbar(0,0,0)

        if sector == 2:
            sectortext = '[Stage 1 - 2] 고블린 부락'
            questbar(0,0,0)

        if sector == 3:
            sectortext = '[Stage 1 - 3] 홉고블린의 숲'
            questbar(0,0,0)

        if sector == -1:
            sectortext = '[Stage 1] 자유 구역'
            questbar(0,0,0)
        if sector == -2:
            sectortext = '[상점] 상점 구역'
            questbar(0,0,0)
        if sector == -3:
            sectortext = '[Stage 1] 잊힌 어느 한 구역'
            questbar(0,0,0)
        if sector == -4:
            sectortext = '[Stage 1] 수상한 지하실'
            questbar(0,0,0)

        if sector == -5:
            sectortext = '[Stage 1..?] ??? '
            questbar(0,0,0)



    if stage == 2:
        
        if sector == 0:
            sectortext = '[Stage 2] 휴식 구역 - 안전지대 '
            questbar(0,0,0)
        if sector == 1:
            sectortext = '[Stage 2 - 1] 균열이 생기고 있는 곳'
            questbar(60,0,0)
        if sector == 2:
            sectortext = '[Stage 2 - 2] 누구도 살지 않는 오크의 숲'
            questbar(100,0,0)
        if sector == 3:
            sectortext = '[Stage 2 - 3] 소균열 슬라임 서식지'
            questbar(150,0,0)      
        if sector == 4:
            sectortext = '[Stage 2 - 4] 소균열 심층부'
            questbar(200,0,0)
        if sector == 5:
            sectortext = '[Stage 2 - Final] 소균열 중심부'
            questbar(255,0,0)
        if sector == -1:
            sectortext = '[Stage 2] 평화로운 중립 지대'
            questbar(0,0,255)
        if sector == -2:
            sectortext = '[Lv.1 Shop] 차원 상점'
            questbar(0,0,255)






def regen():
    # 체력 회복
    global hp , mp , max_hp , max_mp , intelligence , hpp , defense, self_restore, isbloody, sector
   
    if sector != 0:
        if self_restore == True:

    
            if hp < max_hp / 5:
                hp -= 0.000005 * max_hp

            if hp>= max_hp/5 and hp <= max_hp * 0.50:
                hp += 0.00005 * max_hp

            if hp > max_hp /2 and hp <= max_hp:
                hp += 0.00003 * max_hp

            if hp > max_hp+50:
                hp -= 0.000008 * max_hp


    if sector == 0:
        if hp < max_hp /5:
            hp += 0.03 * max_hp

        if hp>= max_hp/5 and hp <= max_hp * 0.50:
            hp += 0.005 * max_hp

        if hp > max_hp /2 and hp < max_hp:
            hp += 0.0008 * max_hp



    # 마력 회복
    if sector != 0:

        if mp < max_mp * 0.1:
            mp += 0.0005 * max_mp

        if mp >= max_mp * 0.1 and mp< max_mp:
            mp += 0.0003* max_mp

    if sector == 0:
        if mp < max_mp * 0.1:
            mp += 0.007 * max_mp

        if mp >= max_mp * 0.1 and mp< max_mp:
            mp += 0.005* max_mp



def skilldamage():
    global strength, intelligence ,character_skill1_level, character_skill1_exp

    if character_skill1_level == 1:
        return strength* 2 + intelligence * 1
    
    if character_skill1_level == 2:
        return strength * 2.5 + intelligence * 1.2
    
    if character_skill1_level == 3:
        return strength * 3 + intelligence * 1.4

    if character_skill1_level == 4:
        return strength * 3.33 + intelligence * 1.7
    
    if character_skill1_level == 5:
        return strength * 3.66 + intelligence * 2.0
    
    if character_skill1_level == 6:
        return strength * 4 + intelligence * 2.4
    
    if character_skill1_level == 7:
        return strength * 4.2 + intelligence * 2.5
    
    if character_skill1_level == 8:
        return strength * 4.5 + intelligence * 2.7
    
    if character_skill1_level == 9:
        return strength * 4.8 + intelligence * 2.9
    
    if character_skill1_level == 10:
        return strength * 20 + intelligence * 10
    if character_skill1_level == 11:
        return strength * 21 + intelligence * 11



def skill1_levelup():
    global strength, intelligence ,character_skill1_level, character_skill1_exp, character_skill1_exp_require, blitingskill1
    
    # 레벨업!
    if character_skill1_exp >= character_skill1_exp_require[character_skill1_level]:
        blitingskill1 = True

        character_skill1_exp -= character_skill1_exp_require[character_skill1_level]
        character_skill1_level += 1
        # 레벨 업



        message('[충격파]가 숙련도를 모두 채워 레벨이 오릅니다!(현재 Lv {})'.format(character_skill1_level))
        
        if character_skill1_level % 10 == 0:
            message(f'[충격파]가 {character_skill1_level}레벨에 도달하여, 스킬의 격이 상승합니다!')


def skill1_blit():

    global blitingskill1,font, strength, intelligence ,character_skill1_level, character_skill1_exp, character_skill1_exp_require

    if blitingskill1:


        proficiency_percentage = character_skill1_exp / character_skill1_exp_require[character_skill1_level] * 100   # 퍼센트 단위

        proficiency_percentage_text = font.render('[충격파 Lv.{}] 숙련도 : {:.3}%'.format(character_skill1_level, proficiency_percentage), True, (0,0,255))

        screen.blit(proficiency_percentage_text, (10, 500))








class Slime:
    def __init__(self, s_level , s_hp , s_atk, slime_xpos, slimedoexist):
        self.s_level = s_level
        self.s_hp = s_hp
        self.s_atk = s_atk
        self.slime_xpos = slime_xpos
        self.slimedoexist = slimedoexist
      




    def slimemove(self):
        global character_xpos
        if self.slimedoexist == True:
            if self.slime_xpos < character_xpos:
                self.slime_xpos += 1

            if self.slime_xpos >= character_xpos:
                self.slime_xpos -= 1
        
    
        
    def slimeattack(self):
        global hp, character_xpos 
        hp -= self.s_atk
        if character_xpos > self.slime_xpos:
            character_xpos += 80
        
        if character_xpos <= self.slime_xpos:
            character_xpos -= 80
        
    def slimedamaged(self):
        global character_atk, character_xpos
        self.s_hp -= 1
        if character_xpos > self.slime_xpos:
            self.slime_xpos -= 80
        
        if character_xpos <= self.slime_xpos:
            self.slime_xpos += 80
    

    def slimeregen():
        pass

    def slimeblit(self):
        global slime1
        if self.slimedoexist:

            screen.blit(  slime ,  (self.slime_xpos, 720-90))

    
    

def npc():

    global slime_clear, stage, sector, quest_progress

        
# 1. 슬라임 잡기
# 2. 고블린 방문

def questprogress():
    global quest_text , quest_progress , stage , stage1_dovisitsector_2 , slime_clear , goblin_1_killcount
    global items, items_code, oak_state
    if stage == 1:
        if quest_progress == 1 and slime_clear == False:
            quest_text = 'Quest) [난이도 : F-] 슬라임을 잡으세요!'
        
        elif quest_progress == 1 and slime_clear == True:
            quest_text = 'Quest) 완료! 에단에게 가세요! '

        elif quest_progress == 2 and stage1_dovisitsector_2 == False:
            quest_text = 'Quest) [난이도 : F-] 2구역을 방문하세요! | 보상: 2단 점프 개방 '
        elif quest_progress == 2 and stage1_dovisitsector_2 == True:
            quest_text = 'Quest) 완료! 에단에게 가세요!'
        elif quest_progress == 3 and goblin_1_killcount < 7:
            quest_text = F'Quest) [난이도 : F+] 고블린을 처치하세요! ({goblin_1_killcount}/7) | 보상: 경험치 8'
            
        elif quest_progress == 3 and goblin_1_killcount >= 7:
            quest_text = 'Quest) 완료! 에단에게 보상을 받으러 가세요!'

        elif quest_progress == 4 and goblin_1_killcount < 15:
            quest_text = F'Quest) [난이도 : E-] 강해진 고블린을 처치하세요!({goblin_1_killcount - 7} / 8) | 보상 : 경험치 20'

        elif quest_progress == 4 and goblin_1_killcount >=15:
            quest_text = 'Quest) 완료! 에단에게 보상을 받으러 가세요!'
        elif quest_progress == 5 and hop_goblin_state['doexist'] == True:
            quest_text = 'Rare Quest) [보스전 난이도 : D-] 홉 고블린을 처치하세요!'
        
        elif quest_progress == 5 and hop_goblin_state['doexist'] == False:
            quest_text = '퀘스트 클리어! 에단에게 보상을 받으러 가세요!'
        elif quest_progress == 6 and stage == 1:
            quest_text = '퀘스트가 없습니다.'
        elif shop_have[3] == 1 and stage == 1 and quest_progress < 6 and hiddenpiece_1_5_key == False:
            quest_text = 'Unique Quest)[난이도: C] 사건을 밝혀내세요!'

    if stage == 2:
        if quest_progress == 11 and player_sector <= 1:
               quest_text = 'Quest) [난이도: F-] 2구역에 가서 균열의 흔적을 보고 오세요!'

        if quest_progress == 11 and player_sector > 1:
               quest_text = 'Quest) 완료! 보상을 받으러 가세요!'

        if quest_progress == 12 and (oak_state['killed'] < 8 or items['오크의 핵'] < 1):
            quest_text = 'Quest) [난이도: D+] 오크들을 잡고 핵을 가져오세요! (오크: {} / 8마리, 핵: {} / 1개)'.format(oak_state['killed'], items['오크의 핵'])
            
        if quest_progress == 12 and oak_state['killed'] >= 8 and items['오크의 핵'] >= 1:
            quest_text = 'Quest) 완료! 보상을 받으러 가세요!(오크: {} / 8마리, 핵: {} / 1개)'.format(oak_state['killed'], items['오크의 핵'])








slime1 = Slime(1,10,1,80 , True)


def levelup():
    global exp, levelup_exp , level, remain_statpoint,hp,mp, message_activated, message_text
    cnt = 0
    # if exp >= levelup_exp[level]:
    if exp >= levelup_exp[level]:

        while exp >= levelup_exp[level+ cnt]:
            exp -= levelup_exp[level + cnt]
            cnt += 1
        level += cnt
            
        if cnt == 1:
            message_text = '[레벨업 했습니다!({} >>> {})]'.format(level-1, level)
            hp = max_hp
            mp = max_mp
            remain_statpoint += 3
            
        if cnt > 1:
            message_text = '[레벨업 했습니다!({} >>> {})] X {}'.format(level-cnt, level, cnt)
            hp = max_hp
            mp = max_mp
            remain_statpoint += 3 * cnt
            
        
        
        
        
        # exp -= levelup_exp[level]
        # level += 1
        # remain_statpoint += 3
        
        # pygame.time.set_timer(pygame.USEREVENT , 2000 , 1)
        # message_activated = True
        # message_text = '레벨업 했습니다!({} >>> {})'.format(level-1, level)
        # hp = max_hp
        # mp = max_mp








# 고블린 함수 정의하기

def goblinregen():
    global goblin_regen_time ,goblin_1_doexist , goblin_1_status , goblin_1_level, goblin_1_xpos
    if pygame.time.get_ticks() - goblin_regen_time >= 8000  and goblin_1_doexist == False:
        
        if goblin_1_killcount >= 7 and goblin_1_killcount < 14:
            goblin_1_level = 4
            goblin_1_status['mhp'] = 80
            goblin_1_status['speed'] = 1.77
            goblin_1_status['atk'] = 15
        if goblin_1_killcount >= 14 and goblin_1_killcount < 30:
            goblin_1_level = 7
            goblin_1_status['mhp'] = 160
            goblin_1_status['speed'] = 1.9
            goblin_1_status['atk'] = 20
        if goblin_1_killcount >= 30 and goblin_1_killcount < 40:
            goblin_1_status['speed'] = 2.2
            goblin_1_status['atk'] = 30
            goblin_1_level = 15
            goblin_1_status['mhp'] = 400
        
        if goblin_1_killcount < 40:
            goblin_1_doexist = True


        goblin_1_xpos = randint(400, 1000)
        
        goblin_1_status['hp'] = goblin_1_status['mhp']

def goblin_killed():
    global exp, goblin_regen_time, goblin_1_killcount , goblin_1_doexist , goblin_1_status , goblin_1_level

    if goblin_1_status['hp'] <= 0 and goblin_1_doexist == True:

        goblin_1_doexist = False
        exp += (5 + goblin_1_level)
        goblin_1_killcount += 1
        goblin_regen_time = pygame.time.get_ticks()


        

def goblinmove():
    global goblin_1_xpos , character_xpos, goblin_1_status , goblin_1_doexist , goblin_1_level

    if goblin_1_doexist:
        if character_xpos >= goblin_1_xpos:
            goblin_1_xpos += goblin_1_status['speed']


        elif character_xpos < goblin_1_xpos:
            goblin_1_xpos -= goblin_1_status['speed']

        
        screen.blit(font.render("[Lv.{} 고블린 | HP {} / {}]".format(goblin_1_level , goblin_1_status['hp'],goblin_1_status['mhp']     ), True, (0,0,0)) , (goblin_1_xpos , 720 - 150 - 40)      )

        screen.blit(goblin_1 , (goblin_1_xpos , 720-150))

    




def statup_str():
    global remain_statpoint , strength

    if remain_statpoint >= 1:
        remain_statpoint -= 1
        strength += 1

def statup_def():
    global defense, remain_statpoint
    if remain_statpoint >= 1 and defense <= 199:
        defense += 1
        remain_statpoint -= 1

def statup_hpp():
    global hpp, remain_statpoint
    if remain_statpoint >= 1:
        hpp += 1
        remain_statpoint -= 1


def statup_int():
    global intelligence, remain_statpoint
    if remain_statpoint >= 1 :
        intelligence += 1
        remain_statpoint -= 1



def calculation():
    global defense, hpp, intelligence , strength, hp, mp, max_hp, max_mp, dmgreduction

    # 1. 방어력 계산하기
    if defense <= 10:
        dmgreduction = 1 - ( defense ) / 100
    if defense <= 50 and defense >10:
        dmgreduction = 1 - (  10 +  0.5 * (  defense-10  ) )/ 100

    if defense <= 150 and defense > 50:
        dmgreduction = 1 - (0.2 * (  defense - 50  ) + 30 ) / 100

    if defense <= 190 and defense > 150:
        dmgreduction = 1 - (0.1 * (  defense - 150  ) + 50 ) / 100

    if defense <= 199 and defense > 190:
        dmgreduction = 0.46
    if defense == 200:
        dmgreduction = 0.4
    

    # 체력 계산하기

    if hpp <= 10:
        max_hp = 100 + 10*hpp

    if hpp <= 30 and hpp > 10:
        max_hp = 200 + 20*(hpp - 10)

    if hpp > 30 and hpp <= 50:
        max_hp = 600 + 30*(hpp - 30)
    
    if hpp > 50 and hpp <= 100:
        max_hp = 1200 + 40*(hpp -  50)

    if hpp > 100 and hpp <= 199:
        max_hp = 3200 + 60*(hpp - 100 )

    if hpp == 200:
        max_hp = 10000

    if hpp > 200 and hpp <= 400:
        max_hp = 10000 + 80*(hpp - 200)




    # 3. 마나 계산하기

    if intelligence < 10:
        max_mp = 9 + intelligence
    
    if intelligence >= 10 and intelligence <= 20:
        max_mp = 20 +  2 *  (intelligence - 10)

    if intelligence > 20 and intelligence <= 50:
        max_mp = 40 +  3 *  (intelligence - 20)

    if intelligence > 50 and intelligence <= 100:
        max_mp = 130 + 4*(intelligence - 50)
    if intelligence > 100:
        max_mp = 333




# 홉고블린 생성하기
def hopgoblinevent():
    global hop_goblin, hop_goblin_state , hop_goblin_xpos , exp, sector, character_xpos , character_rect, hp
    global character_atk_rect , character_atk_do_exist, font, dmgreduction
    if sector != 3 and stage == 1 and hop_goblin_state['doexist'] == True:
        hop_goblin_state['hp'] += 0.001  # 전투에서 벗어나면 회복함.

    
    if sector == 3 and stage == 1:

        # 이동( 3 구역에서만 )
        if hop_goblin_state['doexist'] == True:
            if hop_goblin_state['hp'] > 320:
                if character_xpos < hop_goblin_xpos:
                    hop_goblin_xpos -= hop_goblin_state['speed']
                elif character_xpos >= hop_goblin_xpos:
                    hop_goblin_xpos += hop_goblin_state['speed']

            elif hop_goblin_state['hp'] <= 320:
                if character_xpos < hop_goblin_xpos:
                    if hop_goblin_xpos < 1280-100 :

                        hop_goblin_xpos += hop_goblin_state['speed']/1.5
                    elif hop_goblin_xpos > 1280-100:
                        hop_goblin_xpos -= 480
                if character_xpos >= hop_goblin_xpos:
                    if hop_goblin_xpos > 0:
                        hop_goblin_xpos -= hop_goblin_state['speed']/1.5
                    elif hop_goblin_xpos <= 0:
                        hop_goblin_xpos += 480

                



           

        # 충돌처리 위한 rect 설정
        hop_rect = hop_goblin.get_rect()
        hop_rect.top = 540
        hop_rect.left = hop_goblin_xpos
        
        # 충돌처리

        if character_rect.colliderect(hop_rect) and hop_goblin_state['doexist'] == True:
            hp -= hop_goblin_state['atk'] * dmgreduction
            if character_xpos < hop_goblin_xpos:
                character_xpos -= 80
            elif character_xpos >= hop_goblin_xpos:
                character_xpos += 80
        
        if character_atk_rect.colliderect(hop_rect) and character_atk_do_exist == True and hop_goblin_state['doexist'] == True :
            hop_goblin_state['hp'] -= skilldamage() * hop_goblin_state['dmgreduction']
            character_atk_do_exist = False
        
        
        # 남은체력 0 이하면 죽기

        if hop_goblin_state['hp'] <= 0 and hop_goblin_state['doexist']:
            hop_goblin_state['doexist'] = False
            exp += 450

        if hop_goblin_state['doexist'] == True:   # 화면에 표기하기
            screen.blit(hop_goblin , (hop_goblin_xpos , 540))
            if hop_goblin_state['hp'] >= 320:
                screen.blit(font.render( F'[홉 고블린] HP : {int(hop_goblin_state["hp"])} / 1280' , True, (0,0,0)     )   ,(hop_goblin_xpos, 500)  )
            else:
                screen.blit(font.render( F'[홉 고블린] HP : {int(hop_goblin_state["hp"])} / 1280' , True, (255,0,0)     )   ,(hop_goblin_xpos, 500)  )



# 1. 오크 공격

def oakattack():
    global hp, oak_state, oak_xpos, character_xpos, oak_2, dmgreduction, defense, message_text, message_activated

    # 캐릭터가 맞음.
    if oak_state['atk'] < defense:

        message_text = '나약한 공격을 무시했습니다.'
        message_activated = True
        pygame.time.set_timer(pygame.USEREVENT, 2000, 1)
        if character_xpos < oak_xpos:
            if character_xpos >= 50:
                character_xpos -= 40
                oak_xpos += 60
            elif character_xpos <= 50:
                character_xpos -= 50
                oak_xpos += 200
        else:
            if character_xpos <= 1440 - 100:
                character_xpos += 50
                oak_xpos -= 60
            else:
                oak_xpos -= 100
         

    else:
        hp -= oak_state['atk'] * dmgreduction
        message_text = '오크에게 {} 데미지를 입었습니다.'.format(int(oak_state['atk'] * dmgreduction))
        message_activated = True
        pygame.time.set_timer(pygame.USEREVENT, 2000, 1)
        if character_xpos < oak_xpos:
            if character_xpos >= 80:
                character_xpos -= 80
                oak_xpos += 10
            elif character_xpos <= 80:
                character_xpos -= 80
                oak_xpos += 80
        
        else:
            if character_xpos <= 1440 - 100:
                character_xpos += 100
                oak_xpos -= 10
            else:
                oak_xpos -= 100
                

def oakmoveandblit():
    global oak_xpos,oak_2,oak_respawnevent,oak_state,character_xpos, oak_respawnevent,font

    if character_xpos > oak_xpos:
        oak_xpos += oak_state['speed']

    else:
        oak_xpos -= oak_state['speed']

    if oak_state['doexist']:

        screen.blit(oak_2, (oak_xpos, 720 - 200))
        screen.blit(font.render(   '[오크 Lv.13] HP {} / {}'.format(oak_state['hp'],oak_state['max_hp'] ) , True, (80,0,0) ) , (oak_xpos , 720-200 - 40))


def oakdamaged_killed(damage):
    global oak_xpos,oak_2,oak_respawnevent,oak_state,character_xpos, character_atk_do_exist, exp, items
    global hp, oak_state, oak_xpos, character_xpos, oak_2, dmgreduction, defense, message_text, message_activated

    oak_state['hp'] -= damage
    message_text = '오크에게 {} 피해를 주었습니다'.format(damage)
    character_atk_do_exist = False
    message_activated = True
    pygame.time.set_timer(pygame.USEREVENT, 2000, 1)
    if True:
        if oak_xpos > character_xpos:
            oak_xpos += 60
        else:
            oak_xpos -= 60

    if oak_state['hp'] <= 0:
        oak_state['doexist'] = False
        exp += 80
        oak_state['killed'] += 1
        message_text = '          오크를 처치하였습니다.(경험치 + 80)'

        percentage_num = randint(1, 100)
        if percentage_num >= 88:
            items['오크의 핵'] += 1
            message_text = '오크를 처치하여  아이템 [오크의 핵]을 획득하셨습니다.(경험치 + 80)'

    
        pygame.time.set_timer(pygame.USEREVENT + 2, 7000, 1)


    
        





        
def slime2_attack():
    global slime_2_state, slime_2, character_xpos, slime_2_flyer_state, hp, dmgreduction
    global message_text, message_activated, state_abnormality
    # 닿았을 경우에서 시작함.

    if stage != 2:
        return

    hp -= slime_2_state['atk'] * dmgreduction
    slime_2_state['slowcnt'] += 1

    message_text = '     차원의 슬라임에게 {} 의 피해를 받았습니다.'.format(int(slime_2_state['atk'] * dmgreduction))
    message_activated = True
    pygame.time.set_timer(pygame.USEREVENT, 1500, 1)

    if slime_2_state['slowcnt'] >= 5:
        slime_2_state['slowcnt'] = 0
        state_abnormality['구속'] = 1
        state_duration['구속'] = 2
    
    

    if character_xpos < slime_2_state['xpos'] and character_xpos >= 80:
        slime_2_state['xpos'] += 10
        character_xpos -= 70
    elif character_xpos < slime_2_state['xpos'] and character_xpos < 80:
        slime_2_state['xpos'] += 100
        character_xpos -= 80
    elif character_xpos >= slime_2_state['xpos'] and character_xpos > 1180:
        slime_2_state['xpos'] -= 90
        character_xpos += 40
    elif character_xpos >= slime_2_state['xpos'] and character_xpos <= 1180:
        slime_2_state['xpos'] -= 10
        character_xpos += 70
    

    




    
def slime2_damagedandkilled_byskill1():
    global slime_2_state, slime_2, character_xpos, slime_2_flyer_state, hp, dmgreduction,character_atk_do_exist
    global message_text, message_activated, exp, kingslime_state
    if stage != 2 or sector != 3:
        return

    slime_2_state['hp'] -= skilldamage() * 0.7  # 30% 물리내성


    message_text = '     차원의 슬라임에게 {} 의 피해를 주었습니다.'.format(int(skilldamage() * 0.7))
    message_activated = True
    pygame.time.set_timer(pygame.USEREVENT, 1500, 1)

    character_atk_do_exist = False

    if slime_2_state['hp'] <= 0:
        slime_2_state['doexist'] = False

        message_text = '     차원의 슬라임을 처치했습니다.(경험치 + 120)'
        exp += 120

        slime_2_state['killed'] += 1
        slime_2_state['slowcnt'] = 0
        if slime_2_state['hp'] <= -150:
            message('오버킬! 킹슬라임이 치명적인 피해를 입습니다!')
            kingslime_state['hp'] -= 10
        kingslime_state['hp'] -= 5
        



        if kingslime_state['hp'] <= 0:
            kingslime_state['doexist'] = False
            message("슬라임 킹을 처치하였습니다! 막대한 양의 경험치를 획득합니다!")
            exp += 1580 * abs(3 - kingslime_state['life'])
            kingslime_state['life'] -= 1
            if kingslime_state['life'] >= 1:
                pygame.time.set_timer(pygame.USEREVENT+14 , 20000, 1 )


      

        pygame.time.set_timer(pygame.USEREVENT + 3 , 8000, 1)







def slime2_specialatkemerge():
    global slime_2_state, slime_2, character_xpos, slime_2_flyer_state, hp, dmgreduction,character_atk_do_exist
    
    
    if slime_2_state['doexist'] != True or sector != 3 or stage != 2:
        return

    slime_2_flyer_state['dowxist'] = True

    
    if character_xpos < slime_2_state['xpos']:
        slime_2_flyer_state['direction'] = -5
    else:
        slime_2_flyer_state['direction'] = +5
    
    slime_2_flyer_state['xpos'] = slime_2_state['xpos']; slime_2_flyer_state['ypos'] = slime_2_state['ypos']

    pygame.time.set_timer(pygame.USEREVENT + 4 , randint(2500,5555), 1)


def slime2_slime2flyer_moveandblit():
    global font,slime_2_state, slime_2,slime_2_active, character_xpos, slime_2_flyer_state, hp, dmgreduction,character_atk_do_exist
    global slime_2_flyer
    if slime_2_state['doexist'] == False or stage != 2 or sector != 3:
            
            return
    screen.blit(slime_2 , (slime_2_state['xpos'], slime_2_state['ypos']))
    screen.blit(  font.render('[균열의 슬라임] HP : {} / {}'.format(int(slime_2_state['hp']), slime_2_state['max_hp']), True, (0,0,0)), (slime_2_state['xpos'], slime_2_state['ypos'] - 40)   )
    if slime_2_flyer_state['dowxist']:

        screen.blit(slime_2_flyer, (slime_2_flyer_state['xpos'], slime_2_flyer_state['ypos'] ))
    if slime_2_active:
        slime_2_active = False
        slime2_specialatkemerge()

    if character_xpos > slime_2_state['xpos']:
        slime_2_state['xpos'] += slime_2_state['speed']
    
    if character_xpos <= slime_2_state['xpos']:
        slime_2_state['xpos'] -= slime_2_state['speed']

    if slime_2_flyer_state['dowxist'] == True:
        slime_2_flyer_state['xpos'] += slime_2_flyer_state['direction'] * 3.5
        if slime_2_flyer_state['xpos'] < 0 or slime_2_flyer_state['xpos'] > 1280:
            slime_2_flyer_state['dowxist'] = False


    
    
    

    
def slime2_specialattacked():
    global font,slime_2_state, slime_2, character_xpos, slime_2_flyer_state, hp, dmgreduction,character_atk_do_exist
    global slime_2_flyer

    slime_2_flyer_state['dowxist'] = False
    character_xpos  +=  slime_2_flyer_state['direction'] * 25
    hp -= slime_2_state['flyeratk']

    slime_2_state['slowcnt'] += 3

    if slime_2_state['slowcnt'] >= 5:
        slime_2_state['slowcnt'] = 0
        state_abnormality['구속'] = 1
        state_duration['구속'] = 2

    

#######################################



def abnormality():    # 상태이상
    global hp,font, state_abnormality, state_duration, texty
    global speedup, speeddown
    global characrer_speed
    global self_restore
    global isbloody
    

    # 지역변수 설정하기
    cnt = 0
    texty = ''
    positivity = 0

    if isbloody:
        texty += '[출혈] , '

    if state_abnormality['구속'] != 0:
        texty += '[구속 Lv.{} ({}초)] , '.format(state_abnormality['구속'], state_duration['구속'])
        speeddown = state_abnormality['구속']
        positivity -= state_abnormality['구속']
   

    if state_abnormality['구속'] == 0:
        speeddown = 0


    if state_abnormality['신속'] != 0:
        texty += '[신속 Lv.{} ({}초)] , '.format(state_abnormality['신속'], state_duration['신속'])
        speedup = state_abnormality['신속']
        positivity += state_abnormality['신속']

    
    if state_abnormality['독'] != 0:

        self_restore = False
        texty += '[독 Lv.{} ({}초)] , '.format(state_abnormality['독'],state_duration['독'])

        if state_abnormality['독'] <= 3:   # 1~3 lvl
            hp -= state_abnormality['독'] * 3

        elif state_abnormality['독'] > 3 and state_abnormality['독'] <= 10:
            hp -= (state_abnormality['독'] - 3) * 5 + 15
        elif state_abnormality['독'] > 10 and state_abnormality['독'] <= 20:
            hp -= (state_abnormality['독'] - 10) * 10 + 50

    elif state_abnormality['독'] == 0:
        self_restore = True
    

    

    
        

            

        
    # 마지막
    if texty == '':
        texty = '상태이상 없음'
    

    

###

def coinblit():
    global coin, font

    coin_text = '보유 코인 : {:,}C'.format(coin)
    screen.blit(font.render(coin_text, True, (255,255,80)), (10, 160))



########################## Sec 03

def kingslingcolliderect():
    global hp, character_ypos, dmgreduction, kingslime_state, character_xpos, kingslime_laser_count

    kingslime_laser_count = 0




    if character_ypos < 720-150-300:
        character_ypos += 300

    if character_xpos < kingslime_state['xpos']:
        character_xpos -= 60
    elif character_xpos > kingslime_state['ypos']:
        character_xpos += 60
    
    hp -= dmgreduction * 200

    
def kingslime_specialattack():
    global kingslime_state,hp, character_ypos, dmgreduction, character_xpos, laser_type
    # 지역변수
    if kingslime_state['doexist'] == False:
        return
    

    randomint = randint(1,100)

    if randomint >= 76:
        kingslime_specialattack_1_0()
        laser_type = 2

    else:
        kingslime_specialattack_1_0()
        laser_type = 1
    

    # pygame.time.set_timer(pygame.USEREVENT + 9,randint(6000,14000), 1)






    


# Slow
def kingslime_specialattack_1_0(): # 
    global kingslime_state,hp, character_ypos, dmgreduction, character_xpos, kingslime_laser_xpos,kingslime_laser_exist
    global kingslime_laser_damage, kingslime_laser_exist
    kingslime_laser_xpos = randint(0, 1200)

    #  1 일때; 데미지X
    kingslime_laser_damage = False
    kingslime_laser_exist = True
    pygame.time.set_timer(pygame.USEREVENT + 10, 660, 1)
    




def kingslime_specialattack_1_1():
    global kingslime_state , hp , character_ypos, dmgreduction, character_xpos, kingslime_laser_xpos,kingslime_laser_exist
    global kingslime_laser_damage, kingslime_laser_exist,kingslime_laser_xpos
    kingslime_laser_damage = False
    kingslime_laser_exist = False
    pygame.time.set_timer(pygame.USEREVENT + 11, 1500, 1)

   

def kingslime_specialattack_1_2():
    global kingslime_state , hp , character_ypos, dmgreduction, character_xpos, kingslime_laser_xpos,kingslime_laser_exist
    global kingslime_laser_damage, kingslime_laser_exist,kingslime_laser_xpos
    kingslime_laser_exist = True
    kingslime_laser_damage = True
    pygame.time.set_timer(pygame.USEREVENT+ 12, 4000, 1)

def kingslime_specialattack_1_3():
    global kingslime_state , hp , character_ypos, dmgreduction, character_xpos, kingslime_laser_xpos,kingslime_laser_exist
    global kingslime_laser_damage, kingslime_laser_exist,kingslime_laser_xpos    
    kingslime_laser_exist = False
    kingslime_laser_damage = False
    pygame.time.set_timer(pygame.USEREVENT + 13, randint(6000, 15000), 1)
    

def kingslime_lasercolliderect():
    
    global kingslime_state , hp , character_ypos, dmgreduction, character_xpos, kingslime_laser_xpos,kingslime_laser_exist
    global kingslime_laser_damage, kingslime_laser_exist,kingslime_laser_xpos , character_rect, kingslime_laser_rect

    global kingslime_laser_count, slime2_rect, state_duration, state_abnormality



    if laser_type == 1 and kingslime_laser_exist== True and kingslime_laser_damage == True\
        and character_rect.colliderect(kingslime_laser_rect):
             
        
        
            kingslime_laser_count += 1
            state_duration['구속'] = 25
            state_abnormality['구속'] = 5
            state_duration['독'] = 2
            state_abnormality['독'] = 6
            message('킹 슬라임의 레이저로 인해 [구속] 디버프를 받습니다.')
            
    if laser_type == 2 and slime2_rect.colliderect(kingslime_laser_rect):
        if slime_2_state['hp'] < slime_2_state['max_hp'] and kingslime_laser_exist == True and kingslime_laser_damage == True:
            slime_2_state['hp'] += 0.5

        



            


def kingslime_moveandblit():

    global kingslime_state , hp , character_ypos, dmgreduction, character_xpos, kingslime_laser_xpos,kingslime_laser_exist
    global kingslime_laser_damage, kingslime_laser_exist,kingslime_laser_xpos , character_rect, kingslime_laser_rect
    global kingslime_laser_xpos, kingslime_laser_heal, kingslime_laser_slow
    global kingslime_laser_count, slime2_rect, state_duration, state_abnormality, kingslime, font

    if kingslime_state['life'] <= 0:
        return
    
    if kingslime_state['xpos'] > character_xpos:
        kingslime_state['xpos'] -= 0.8
    if kingslime_state['xpos'] <= character_xpos:
        kingslime_state['xpos'] += 0.8

    if kingslime_state['ypos'] <= 200 and kingslime_state['ypos'] >= 100:
        kingslime_state['ypos'] += randint(-2,2)
    if kingslime_state['ypos'] > 200:
        kingslime_state['ypos'] -= 1.5
    if kingslime_state['ypos'] < 100:
        kingslime_state['ypos'] += 0.8
    
    if kingslime_state['doexist']:
        screen.blit(kingslime, (kingslime_state['xpos'], kingslime_state['ypos']))
        screen.blit(font.render('[킹 슬라임] HP {}%'.format(int( kingslime_state['hp'] / 120 * 100  )), True, (160,0,0)), (kingslime_state['xpos'] , kingslime_state['ypos'] - 40))



    if kingslime_laser_exist == True:
        if laser_type == 1:
            screen.blit(kingslime_laser_slow, (kingslime_laser_xpos, 0))
        else:
            screen.blit(kingslime_laser_heal, (kingslime_laser_xpos, 0))




    
##############################
#### 3 섹터 업그레이드 완료


################## IMPORTANT##############
# 샵



def shop():
    global coin, items, items_code, shop_showing




# 스테이지 1당 8개
def shopmoveplus():
    global coin, items, items_code, shop_showing, stage

    if shop_showing >= (stage - 1) * 8:
        shop_showing = 1
    else:
        shop_showing += 1







def shopmoveminus():
    global coin, items, items_code, shop_showing, stage

    if shop_showing == 1:
        shop_showing = (stage-1) * 8
    else:
        shop_showing -= 1





    


def shopbuy():
    global coin, items, items_code, shop_showing, shop_price, shop_have, shop_name

    if coin >= shop_price[shop_showing] and shop_buylimit[shop_showing] != 0:
        coin -= shop_price[shop_showing]
        shop_have[shop_showing] += 1
        shop_buylimit[shop_showing] -= 1
        message('                     구매 완료')

    







def shopblit():
    global coin, items, items_code, shop_showing, font, stage, sector, shop_button_buy, shop_button_pos, shop_button_pos_max
    if stage < 2 or sector != -2:
        return

    atext = '아이템 이름 : {}'.format(shop_name[shop_showing])
    btext = '현재 보유 수량 : {}'.format(shop_have[shop_showing])
    ctext = '가격 : {}C'.format(shop_price[shop_showing])
    r = 0
    b = 0
    u=0 ; v=255
    if shop_buylimit[shop_showing] == 0:
        dtext = '구매 불가'
        r = 255
    if shop_buylimit[shop_showing] > 0:
        dtext = '남은 구매 횟수 : {}'.format(shop_buylimit[shop_showing])
       
    if shop_buylimit[shop_showing] < 0:
        dtext = '구매 제한 없음'
        b = 255

    e = '구매 : Y '
    if shop_price[shop_showing] > coin:
        e = '코인이 부족합니다(부족한 코인 : {}C)'.format(shop_price[shop_showing] - coin)
        u = 255
        v = 0
    else:
        screen.blit(shop_button_buy, shop_button_pos)
    

    f = ''
    if shop_have[shop_showing] != 0:
        f = '장착하기 : C/V/B/N'




    af = font.render(atext, True, (0,0,0))
    bf = font.render(btext, True, (0,0,0))
    cf = font.render(ctext, True, (0,0,0))
    df = font.render(dtext, True, (r,0,b))
    ef = font.render(e, True, (u,0,v))
    ff = font.render(f, True, (0,0,255))

    screen.blit(af, (60, 360))
    screen.blit(bf, (60, 400))
    screen.blit(cf, (60, 440))
    screen.blit(df, (60, 480))
    screen.blit(ef, (60, 520))
    screen.blit(ff, (60, 560))




def item_c():
    global coin, items, items_code, shop_showing, font, stage, sector, shop_button_buy, shop_button_pos, shop_button_pos_max
    global slot1
    if shop_have[shop_showing] >= 1:
        slot1 = shop_showing
        
        

def item_v():
    global coin, items, items_code, shop_showing, font, stage, sector, shop_button_buy, shop_button_pos, shop_button_pos_max
    global slot1, slot2
    if shop_have[shop_showing] >= 1:
        slot2 = shop_showing



def item_b():
    global coin, items, items_code, shop_showing, font, stage, sector, shop_button_buy, shop_button_pos, shop_button_pos_max
    global slot1, slot3
    if shop_have[shop_showing] >= 1:
        slot3 = shop_showing


def item_n():
    global coin, items, items_code, shop_showing, font, stage, sector, shop_button_buy, shop_button_pos, shop_button_pos_max
    global slot4
    if shop_have[shop_showing] >= 1:
        slot4 = shop_showing


def slotshow():
    global shop_name, shop_have, slot1, slot2, slot3, slot4, slotshowing
    if not slotshowing:
        return
    
    

    a = font.render('C : {} ({}개)'.format(shop_name[slot1], shop_have[slot1]), True, (0,0,0))
    b = font.render('V : {} ({}개)'.format(shop_name[slot2], shop_have[slot2]), True, (0,0,0))
    c = font.render('B : {} ({}개)'.format(shop_name[slot3], shop_have[slot3]), True, (0,0,0))
    d = font.render('N : {} ({}개)'.format(shop_name[slot4], shop_have[slot4]), True, (0,0,0))
    if slotshowing == True:

        screen.blit(a, (10, 320))
        screen.blit(b, (10, 360))
        screen.blit(c, (10, 400))
        screen.blit(d, (10, 440))






    
    

def itemuse_c(slot):
    global shop_name, shop_have, slot1, slot2, slot3, slot4, slotshowing
    global hp, mp, hpp, intelligence, defense, characrer_speed
    global state_duration, state_abnormality, max_mp

    if slot1 == 0 or shop_have[slot] <= 0:
        message('사용 할 수 없습니다.')
        return

    if  slot == 1 and hp < max_hp - 15: # 만약에, 1번 아이템
        hp += 15
        shop_have[slot1] -= 1
        message('최하급 회복 포션을 사용하여 HP를 15 회복했습니다.')
   
   
   
    elif slot ==2:
        if mp < max_mp:
            mp += 8
            shop_have[slot] -= 1
            message('최하급 마력 포션을 사용해 마력을 8 회복했습니다.')

        else:
            message('포션을 쓸 수 없습니다.')

        
    elif slot == 3:
        if hp <= max_hp - 60:
            hp += 60
            shop_have[slot] -= 1
            message('하급 체력 포션을 사용해 체력을 60 회복했습니다.')
        else:
            message('체력이 충분합니다.')

    elif slot == 4:
        if mp <= max_mp - 20:
            mp += 20
            shop_have[slot] -= 1
            message('하급 마력 포션을 사용해 마력을 20 회복했습니다.')
        else:
            message('mp가 충분합니다.')



















print(shop_description)
    










pygame.time.set_timer(pygame.USEREVENT + 5, 1000)
pygame.time.set_timer(pygame.USEREVENT + 9, 1000, 1)


# 이벤트 루프
running = True
while running:
    clock.tick(150)  # 게임화면 초당프레임설정
    dongdong = 0
    
    # 2. 이벤트 처리
    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:    # 창이 닫히는 이벤트 발생하였는가
            running = False # 게임 진행중이 아님
        
        if event.type == pygame.USEREVENT:
            isconversation = False
            message_activated = False

        if event.type == oak_attackevent:
            pass


        if event.type == pygame.USEREVENT + 2:
      
            oak_state['doexist'] = True
            oak_state['hp'] = oak_state['max_hp']
            oak_xpos = randint(500, 1100)
                     

        if event.type == pygame.USEREVENT + 3:
            if kingslime_state['doexist']:

    
                slime_2_state['doexist'] = True
                slime_2_state['xpos'] = randint(300,1000)
                if slime_2_state['max_hp'] < 1680:
                    slime_2_state['max_hp'] += 40
                if slime_2_state['atk'] < 60:
                    slime_2_state['atk'] += 3
                if slime_2_state['flyeratk'] < 180:
                    slime_2_state['flyeratk'] += 10
                if slime_2_state['speed'] <= 3.65:
                    slime_2_state['speed'] += 0.05
                slime_2_state['hp'] = slime_2_state['max_hp']
                pygame.time.set_timer(pygame.USEREVENT + 4, 2500, 1)
            

        if event.type == pygame.USEREVENT + 4:
            if slime_2_state['doexist']:

                slime2_specialatkemerge()

        
        if event.type == pygame.USEREVENT + 5:
            for l in state_duration.keys():
                abnormality()
                
                if state_duration[l] <= 0:
                    if state_abnormality[l] == 0:
                        continue
                    else:
                        state_abnormality[l] = 0
                        continue
                
                state_duration[l] -= 1
                print(state_duration)
                print('rr')


        if event.type == pygame.USEREVENT + 6:
            isconversation = False

        if event.type == pygame.USEREVENT + 7:
            message_activated = False

        if event.type == pygame.USEREVENT + 8:
            blitingskill1 = False

        if event.type == pygame.USEREVENT + 9 and kingslime_state['life'] > 0:
            kingslime_specialattack()


        if event.type == pygame.USEREVENT + 10 and kingslime_state['life'] > 0:
            kingslime_specialattack_1_1()
        if event.type == pygame.USEREVENT + 11:
            kingslime_specialattack_1_2()
        if event.type == pygame.USEREVENT + 12:
            kingslime_specialattack_1_3()

        if event.type == pygame.USEREVENT + 13:
            kingslime_specialattack()

        if event.type == pygame.USEREVENT + 14: #1회성
            if kingslime_state['life'] > 0 and kingslime_state['doexist'] == False:
                
                kingslime_state['doexist'] = True
                kingslime_state['hp'] = 240
                print('r')
                pygame.time.set_timer(pygame.USEREVENT + 9, 2000, 1)
                pygame.time.set_timer(pygame.USEREVENT + 3, 2000, 1)
                pygame.time.set_timer(pygame.USEREVENT + 4, 3000, 1)

    

        
        if event.type == pygame.USEREVENT + 15:
            slotshowing = False
       















        if event.type == pygame.KEYDOWN:
            if character_canmove == True:
                if event.key == pygame.K_d:
                    tox += 2 +characrer_speed + 0.2*speedup - 0.2*speeddown

                if event.key == pygame.K_a:
                    tox -= 2 +characrer_speed + 0.2*speedup - 0.2*speeddown

                if event.key == pygame.K_SPACE or  event.key == pygame.K_w :
                    char_jumpcode()

            if sector == -2:     # 물건 사기
                if event.key == pygame.K_y:
                    if stage == 0:

                        buy()



                    if stage != 0:
                        shopbuy()

                




                if event.key == pygame.K_RIGHT:
                    shopmoveplus()
                if event.key == pygame.K_LEFT:
                    shopmoveminus()

            if sector == -2 and stage >1:
                if event.key == pygame.K_c:
                    item_c()
                if event.key == pygame.K_v:
                    item_v()
                if event.key == pygame.K_b:
                    item_b()
                if event.key == pygame.K_n:
                    item_n()

            if sector != -2 and stage >1:
                if event.key == pygame.K_c:
                    itemuse_c(slot1)
                if event.key == pygame.K_v:
                    itemuse_c(slot2)
                if event.key == pygame.K_b:
                    itemuse_c(slot3)
                if event.key == pygame.K_n:
                    itemuse_c(slot4)








            
            if stage != 0:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_LSHIFT:
                    if conversation_progress!= 0:
                        quest()


            if stage != 0: # 스탯 업 (1: 힘, 2; 방, 3; 체, 4: 지능)
                if event.key == pygame.K_1:
                    statup_str()
                if event.key == pygame.K_2:
                    statup_def()
                if event.key == pygame.K_3:
                    statup_hpp()
                if event.key == pygame.K_4:
                    statup_int()
                    # goblin_1_killcount += 1
                if event.key == pygame.K_e:
                    slotshowing = True
                    pygame.time.set_timer(pygame.USEREVENT + 15, 2000, 1)







        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: ### 공격(근접)
                       


                        if character_atk_do_exist == False and mp >= 1:
                            if character_skill1_level <= 3:
                                mp -= 1
                            if character_skill1_level > 3:
                                mp -= character_skill1_level
                            mp -= character_skill1_level
                            character_skill1_exp += 1
                            blitingskill1 = True
                            pygame.time.set_timer(pygame.USEREVENT + 8, 2000, 1)
                            
                            character_atk_do_exist = True
                            character_atk_current_xpos = character_xpos + 10
                            character_atk_xpos =  character_xpos + 10
                            character_atk_ypos = character_ypos
                            #character_atk_direction
                            # print(pyautogui.position())
                            
                            if pygame.mouse.get_pos()[0] >= character_xpos + character_width/2:
                                character_atk_direction = 1
                         

                            else:
                                character_atk_direction = -1


                if event.button == 3: # 오른쪽 클릭
                    pass







        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                tox = 0

      















    # 이동 처리

    char_moveto()
    char_jumpto()

    # 스킬 레벨업 처리
    skill1_levelup()

    # 화면 나감 처리

    if character_ypos > screen_height - character_height :
            dojumped = False
            jump_cnt =0
            character_ypos = screen_height - character_height
        
    
            toy = 0


    
    if character_xpos < 0:
        sectorleft()

    if character_xpos > screen_width - character_width:
        sectorright()
        
    
    # 리젠
    regen()


    # 레벨업
    levelup()

    # 퀘 진행
    questprogress()

    # HP , MP, Def 계산
    calculation()

    


    ######## 스테이지 처리하기 ########

    ####### 스테이지 0 ######
    if stage == 0:

        stage0_enemy()




    ########## 스테이지 1 #########################
    
    # 섹터 1
    
    

    if slime1.slimedoexist == True:
        slime1.slimemove()
        if slime1.s_hp <= 0 and slime_clear == False:
            slime1.slimedoexist = False
            slime_clear = True
            exp += 2
            player_sector += 1


    
    # 섹터 II
    














    
    backgroundblit()  # 배경 그리기
    if stage != 0:

        statebar()     # HP, MP 그리기

        statusbar()   # 스탯 그리기

        

        screen.blit(font.render(quest_text , True, (0,0,0)) , (10,80)  )  ## 

    if sector == 0 and portal_activated == True:
        screen.blit(portal ,(800 , 60))




    if stage == 1 and sector == 2:
        goblinregen()
        goblin_killed()
        goblinmove()
        



   














    # Life 감소 처리!
    if hp <= 0:
        hp = max_hp * 0.1
        life -= 1
        message_text = '[시스템] 사망하셨습니다. 휴식 구역에서 부활합니다. 남은 생명명은 {}개 입니다.'.format(life)
        message_activated = True
        sector = 0
        pygame.time.set_timer(pygame.USEREVENT , 2000 , 1)

    if life <= 0:
        running = False
        print('[시스템] 생명이 0이 되었습니다. Game Over')
        
        print('게임이 종료되어, 시스템을 종료합니다. 모든 데이터를 초기화합니다.')
        print('사용자님의 최종 레벨은 {}, 최종 도달한 스테이지는 {} 입니다.'.format(level, stage))
        if stage == 0:
            print('버그를 어떻게 찾았는지 모르겠군요.')
        if stage == 1:
            print('사용자님은 이 세계의 아주 조금만을 엿보았을 뿐입니다...')
        if stage == 2:
            print('사용자님은 이 세계의 조금만을 여행했을 뿐입니다.')
        print('만든이: 대대일 고등학교 - Orensi ')
        print('디자인 : Orensi')
        print('음악 : Plum')
        print('사용 언어 : Python')
        print('사용 코드 : 3,375 줄')
        print('다음 모험을 기다리고 있겠습니다...')
        



    

    ######## 충돌 처리_ 충돌 변수 만들기


    character_rect = character.get_rect()
    character_rect.top = character_ypos
    character_rect.left = character_xpos


    character_atk_rect = character_atk.get_rect()
    character_atk_rect.left = character_atk_xpos
    character_atk_rect.top = character_atk_ypos



    heosuabi_rect = heosuabi.get_rect()
    heosuabi_rect.top = 720-80
    heosuabi_rect.left = 600


    slime1_rect = slime.get_rect()
    slime1_rect.top = 720 - 90
    slime1_rect.left = slime1.slime_xpos

    npc_stage1_rect = npc_stage1.get_rect()
    npc_stage1_rect.top = 720 - 150
    npc_stage1_rect.left = 200

    npc_stage2_rect = npc_stage2.get_rect()
    npc_stage2_rect.top = 720 - 150
    npc_stage2_rect.left = 200

    goblin_1_rect = goblin_1.get_rect()
    goblin_1_rect.top = 720 - 150
    goblin_1_rect.left = goblin_1_xpos

    portal_rect = portal.get_rect()
    portal_rect.top = 80
    portal_rect.left = 800


    oak_rect = oak_2.get_rect()
    oak_rect.top = 520
    oak_rect.left = oak_xpos

    slime2_rect = slime_2.get_rect()
    slime2_rect.top = slime_2_state['ypos']
    slime2_rect.left = slime_2_state['xpos']

    slime_2_flyer_rect = slime_2_flyer.get_rect()
    slime_2_flyer_rect.top = slime_2_flyer_state['ypos']
    slime_2_flyer_rect.left = slime_2_flyer_state['xpos']

    kingslime_rect = kingslime.get_rect()
    kingslime_rect.left = kingslime_state['xpos']
    kingslime_rect.top = kingslime_state['ypos']

    kingslime_laser_rect = kingslime_laser_slow.get_rect()
    kingslime_laser_rect.left = kingslime_laser_xpos
    kingslime_laser_rect.top = 0





















    ############## 충돌 처리 ( 스테이지 0 )

    if heosuabi_do_exist == True and character_atk_do_exist == True \
        and character_atk_rect.colliderect(heosuabi_rect) and sector == -1 and stage == 0:
        heosuabi_hp -= 1
        character_atk_do_exist = False



    if slime1_rect.colliderect(character_rect) and stage == 1 and sector == 1 and slime1.slimedoexist == True:
        slime1.slimeattack()

    if slime1_rect.colliderect(character_atk_rect) and stage == 1 and sector == 1 and slime1.slimedoexist == True and character_atk_do_exist== True:
        slime1.slimedamaged()


    if stage == 1 and sector == 0:
        if character_rect.colliderect(npc_stage1_rect) and conversation_progress == 0 and isconversation == False:
            quest()
            isconversation = True

    if stage == 2 and sector == 0:
        if character_rect.colliderect(npc_stage2_rect) and conversation_progress == 0 and isconversation == False:
            quest()
            isconversation = True
            

           


    if stage == 1 and sector == 2:
        if character_rect.colliderect(goblin_1_rect) and goblin_1_doexist == True:
            hp -= goblin_1_status['atk'] * dmgreduction
            
            if character_xpos > goblin_1_xpos :
                character_xpos  += 80
            elif character_xpos <= goblin_1_xpos :
                character_xpos -= 80


        if character_atk_rect.colliderect(goblin_1_rect) and character_atk_do_exist:
            character_atk_do_exist = False
            goblin_1_status['hp'] -= skilldamage()

    if sector == 0 and portal_activated == True:
        if character_rect.colliderect(portal_rect):
            stage += 1
            portal_activated = False
            sector = 0
            player_sector = 1










    # 충돌 처리(섹터= 2, 오크)
    if oak_state['doexist'] and character_rect.colliderect(oak_rect) and stage == 2 and sector == 2:
        oakattack()

    if oak_state['doexist'] and character_atk_rect.colliderect(oak_rect) and stage == 2 and sector == 2 and character_atk_do_exist:
        oakdamaged_killed(skilldamage())
        character_atk_do_exist = False

    if oak_state['doexist'] and stage == 2 and sector == 2:
        oakmoveandblit()


    # 충돌처리(섹터 = 3, 슬라임)
    if slime2_rect.colliderect(character_rect) and stage == 2 and sector == 3 and slime_2_state['doexist']:
        slime2_attack()
    if slime2_rect.colliderect(character_atk_rect) and sector == 3 and stage == 2 and character_atk_do_exist and slime_2_state['doexist']:
        slime2_damagedandkilled_byskill1()
    if slime_2_flyer_rect.colliderect(character_rect) and slime_2_flyer_state['dowxist']:
        slime_2_flyer_state['dowxist'] = False
        slime2_specialattacked()


    # 출돌처리(킹슬라임, 레이절)

    if character_rect.colliderect(kingslime_rect) and kingslime_state['life'] > 0 and kingslime_state['doexist'] and stage == 2 and sector == 3:
        kingslingcolliderect()


    # 이건 그냥
    if stage == 2 and sector ==3:
        kingslime_lasercolliderect()










    # 섹터 텍스트
    sectortext_()

    # 샵

    shopblit()
    slotshow()

    # 섹터 3
    if stage == 2 and sector == 3:

        kingslime_moveandblit()




    # 스킬 숙련도 표시하기

    if stage >= 1:
        skill1_blit()


    # 상태이상
    if stage >= 2:
        coinblit()

        screen.blit(font.render(texty, True, (255,0,0)), (10, 200))


    # 메시지 텍스트
    if message_activated:
        screen.blit(font.render(message_text, True, (255,0,0) ) , (150 , 440))


    # 발사체 먼저 , 캐릭은 나중에
    # 캐릭터 발사체 처리

    if isconversation:
        cv_b = font.render(conversation_text , True , (0,0,0))
        screen.blit(conversation , (320 , 480))
        screen.blit(cv_b , (360 , 520))

        


    if character_atk_do_exist:

        charatk()
        screen.blit(character_atk , (character_atk_xpos , character_atk_ypos))

    if character_atk_do_exist == True:
        screen.blit(character_atk , (character_atk_xpos , character_atk_ypos))

    


        


    # screen.blit(character , (character_xpos, character_ypos))


    


    ##### 스테이지 blit 처리
    if stage == 0 and sector == -1 and heosuabi_do_exist == True:
        screen.blit(heosuabi , (600 , 720 - 80))


    if stage == 1 and sector == 1 and slime1.slimedoexist == True:
        slime1.slimeblit()

    
    if stage == 1 and sector == 0:
        screen.blit(npc_stage1 , (200,720-150))

    if stage == 1:
        hopgoblinevent()


    if stage == 2 and sector == 0: # 2S NPC
        screen.blit(npc_stage2 , (200, 720 - 150))



    if stage == 2 and sector == 3 and slime_2_state['doexist']:
        slime2_slime2flyer_moveandblit()
        






    
    pygame.display.update()

pygame.quit()