import pytest

from calculator.age import get_age_group
from calculator.static import Station, get_static_score


@pytest.mark.parametrize(
    "input_age, input_reps, expected_score",
    [
        # age, reps, score
        (20, 1, 0),
        (20, 15, 1),
        (20, 45, 21),
        #
        (25, 1, 0),
        (25, 15, 4),
        (25, 45, 21),
        #
        (40, 1, 0),
        (40, 15, 11),
        # different results on score table and MINDEF website
        # (40, 45, 23),
    ],
)
def test_pushups_score(input_age, input_reps, expected_score):
    age_group = get_age_group(input_age)

    score = get_static_score(Station.pushup, age_group, input_reps)[0]

    assert expected_score == score
