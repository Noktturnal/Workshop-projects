from flask import Flask, render_template, request

app = Flask(__name__)

# Possible dice
POSSIBLE_DICE = {"3", "4", "6", "8", "10", "12", "20", "100"}


def roll_the_dice(dice_code):
    import random
    import re

    DICE_PATTERN = re.compile(r"^(\d*)D(\d+)([+-]\d+)?$")

    match = DICE_PATTERN.match(dice_code)
    if not match:
        return 0

    multiply, dice, modifier = match.groups()

    if dice not in POSSIBLE_DICE:
        return 0

    multiply = int(multiply) if multiply else 1
    dice = int(dice)
    modifier = int(modifier) if modifier else 0

    roll_sum = sum(random.randint(1, dice) for _ in range(multiply))
    return roll_sum + modifier


def simulate_npc_roll():
    import random

    dice1 = random.choice(list(POSSIBLE_DICE))
    dice2 = random.choice(list(POSSIBLE_DICE))

    roll_result1 = roll_the_dice(f"1D{dice1}")
    roll_result2 = roll_the_dice(f"1D{dice2}")

    return roll_result1 + roll_result2


def apply_rules(score, roll_result):
    score += roll_result
    if roll_result == 7:
        score = score // 7
    elif roll_result == 11:
        score *= 11
    return score


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        player_dice1 = request.form.get('player_dice1')
        player_dice2 = request.form.get('player_dice2')
        player_score = int(request.form.get('player_score', 0))
        npc_score = int(request.form.get('npc_score', 0))

        if player_dice1 in POSSIBLE_DICE and player_dice2 in POSSIBLE_DICE:
            player_roll_result1 = roll_the_dice(f"1D{player_dice1}")
            player_roll_result2 = roll_the_dice(f"1D{player_dice2}")
            player_roll_result = player_roll_result1 + player_roll_result2

            player_score = apply_rules(player_score, player_roll_result)

            if player_score >= 2001:
                return render_template('result.html', winner="Player", score=player_score)

            npc_roll_result = simulate_npc_roll()
            npc_score = apply_rules(npc_score, npc_roll_result)

            if npc_score >= 2001:
                return render_template('result.html', winner="NPC", score=npc_score)

            return render_template('index.html', player_score=player_score, npc_score=npc_score,
                                   dice_options=POSSIBLE_DICE)

    return render_template('index.html', player_score=0, npc_score=0, dice_options=POSSIBLE_DICE)


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
