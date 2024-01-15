##Pig_Dice_Game 입니다##

import random

# 초기화
player1_score = 0
player2_score = 0
current_player = 1

# 주사위 굴리기 함수
def roll_dice():
    return random.randint(1, 6)

