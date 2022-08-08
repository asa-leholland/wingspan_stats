TOTAL_CARD_COUNT = 10

from functools import reduce


def calculate_average_score(frequency_percent: int, low_card_count: int, low_points: int, high_card_count: int, high_points: int) -> float:
    cards_of_total = (TOTAL_CARD_COUNT*frequency_percent)/100
    low_odds = [cards_of_total - i / TOTAL_CARD_COUNT - i for i in range(low_card_count, high_card_count)]
    low_frequency = reduce((lambda x, y : x * y), low_odds) * low_points / TOTAL_CARD_COUNT
    print(low_frequency)
    high_frequency = (cards_of_total - low_card_count / TOTAL_CARD_COUNT - low_card_count) * high_points / TOTAL_CARD_COUNT
    print(high_frequency)
    return round((low_frequency + high_frequency), 1)

data_rows = (

    {
        'frequency_percent': 50,
        'low_card_count': 1,
        'low_points' : 1,
        'high_card_count': 3,
        'high_points': 2,
    },

    {
        'frequency_percent': 21,
        'low_card_count': 4,
        'low_points' : 3,
        'high_card_count': 7,
        'high_points': 6,
    },

    {
        'frequency_percent': 31,
        'low_card_count': 4,
        'low_points' : 4,
        'high_card_count': 6,
        'high_points': 7,
    }
)


for data_row in data_rows:
    print(calculate_average_score(
        frequency_percent=data_row['frequency_percent'],
        low_card_count=data_row['low_card_count'],
        low_points=data_row['low_points'],
        high_card_count=data_row['high_card_count'],
        high_points=data_row['high_points']))