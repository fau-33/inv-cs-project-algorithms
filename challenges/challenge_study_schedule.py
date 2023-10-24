def study_schedule(permanence_period, target_time):
    if target_time is None or permanence_period is None:
        return None
    students = 0

    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None
        if period[0] <= target_time <= period[1]:
            students += 1
    return students
