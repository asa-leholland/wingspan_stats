TOTAL_CARD_COUNT = 365

from functools import reduce
import pandas as pd

class GoalDetails:
    def __init__(self, name: str, frequency_percent: int, low_card_count: int, low_points: int, high_card_count: int, high_points: int):
        self.name = name
        self.frequency_percent = frequency_percent
        self.low_card_count = low_card_count
        self.low_points = low_points
        self.high_card_count = high_card_count
        self.high_points = high_points

    def calculate_score_of_n_matching_cards(self, n_card_count: int) -> int:
        if n_card_count >= self.high_card_count:
            return self.high_points
        elif n_card_count >= self.low_card_count:
            return self.low_points
        else:
            return 0

    def get_list_of_possible_scores(self, min_card_count: int=0, max_card_count: int=15) -> list:
        return [self.calculate_score_of_n_matching_cards(n_card_count) for n_card_count in range(min_card_count, max_card_count + 1)]

    def calculate_number_of_matching_cards(self) -> float:
        return round(((TOTAL_CARD_COUNT*self.frequency_percent)/100))

    def calculate_likelihood_of_n_matching_cards(self, n: int) -> float:
        if n == 0:
            return 0
        number_of_matching_cards = self.calculate_number_of_matching_cards()
        all_possible_scores = [(number_of_matching_cards - i) / (TOTAL_CARD_COUNT - i) for i in range(n)]
        return reduce(lambda x, y: x * y, all_possible_scores)

score_worths = []
goal_output = pd.read_csv('goal_output.csv', sep='\t')
for row in goal_output.iterrows():
    goal_details = GoalDetails(row[1]['Bonus card'], row[1]['%'], row[1]['Low Number'], row[1]['Low Score'], row[1]['High Number'], row[1]['High Score'])
    likely_score = 0
    for possible_bird_count in range(16):
        frequency = goal_details.calculate_likelihood_of_n_matching_cards(possible_bird_count)
        score = goal_details.calculate_score_of_n_matching_cards(possible_bird_count)
        likely_score += frequency * score
    score_worths.append((likely_score, goal_details.name))

for score, name in sorted(score_worths, key = lambda x: x[0]):
    print(f"{score:.0%}, {name}")

