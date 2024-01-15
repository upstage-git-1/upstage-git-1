##Pig_Dice_Game 입니다##

## part 2 - while loop
while player1_score < 100 and player2_score < 100:
    print(f"Player {current_player}'s turn")
    input("Press Enter to roll the dice...")

    dice_result = roll_dice()
    print(f"Rolled a {dice_result}")

    if dice_result == 1:
        print("You rolled a 1, no points earned this turn.")
    else:
        if current_player == 1:
            player1_score += dice_result
        else:
            player2_score += dice_result

        print(f"Player 1's score: {player1_score}")
        print(f"Player 2's score: {player2_score}")

    # 다음 플레이어로 넘어가기
    current_player = 3 - current_player  # 1을 2로, 2를 1로 변경


