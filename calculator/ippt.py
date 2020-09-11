from .age import get_age_group
from .static import get_static_score, Station
from .run import get_run_score
from .data.awards import awards


def get_score(age, pushups, situps, run_secs):
    age_group = get_age_group(age)

    puhsups_score, pushups_next_score = get_static_score(
        Station.pushup,
        age_group,
        pushups,
    )
    situps_score, situps_next_score = get_static_score(
        Station.situp,
        age_group,
        situps,
    )
    run_score, run_next_score = get_run_score(
        age_group,
        run_secs,
    )

    total = puhsups_score + situps_score + run_score

    # find awards
    for award in awards:
        if total >= award.min_score:
            result = award

    return {
        "pushups": {
            "score": puhsups_score,
            "next": pushups_next_score,
        },
        "situps": {
            "score": situps_score,
            "next": situps_next_score,
        },
        "run": {
            "score": run_score,
            "next": run_next_score,
        },
        "age_group": age_group,
        "total": total,
        "result": result.to_dict(),
    }
