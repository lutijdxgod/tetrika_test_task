def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals["lesson"]
    pupil = intervals["pupil"]
    tutor = intervals["tutor"]

    lesson_start, lesson_end = lesson
    lesson_duration_set = set(range(lesson_start, lesson_end))

    pupil_presence = set()
    for i in range(0, len(pupil), 2):
        pupil_presence.update(range(pupil[i], pupil[i + 1]))

    tutor_presence = set()
    for i in range(0, len(tutor), 2):
        tutor_presence.update(range(tutor[i], tutor[i + 1]))

    total_time_together_on_lesson = lesson_duration_set.intersection(
        pupil_presence.intersection(tutor_presence)
    )
    return len(total_time_together_on_lesson)
