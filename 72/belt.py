scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()
HONORS = zip(scores, belts)


def get_belt(user_score):
    prev_score, prev_belt = 0, None
    for score, belt in zip(scores, belts):

        if prev_score <= user_score < score:
            return prev_belt

        prev_score, prev_belt = score, belt
    else:
        return prev_belt
