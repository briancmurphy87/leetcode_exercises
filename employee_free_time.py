class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def employee_free_time(schedule: list[list[Interval]]) -> list[Interval]:
    return employee_free_time_impl(schedule)

    # input: list[list[tuple[int, int]]] = []
    # for employee_intervals in schedule:
    #     input.append([
    #         (work_interval.start, work_interval.end)
    #         for work_interval in employee_intervals
    #     ])
    #
    # results_as_list_of_tuples: list[tuple[int, int]] = employee_free_time_impl(input)
    #
    # return [
    #     Interval(interval_start, interval_finish)
    #     for (interval_start, interval_finish) in results_as_list_of_tuples
    # ]


def get_time_bucket_range(schedule: list[list[Interval]]) -> tuple[int, int]:
    import itertools

    accumulated = itertools.accumulate(
        (
            interval
            for employee_intervals in schedule
            for interval in employee_intervals
        ),
        lambda tracked_interval, this_interval: Interval(
            min(tracked_interval.start, this_interval.start),
            max(tracked_interval.end, this_interval.end)
        )
    )

    accumulated_interval: Interval
    *_, (accumulated_interval) = accumulated
    return accumulated_interval.start, accumulated_interval.end


# def employee_free_time_impl(schedule: list[list[tuple[int, int]]]) -> list[tuple[int, int]]:
def employee_free_time_impl(schedule: list[list[Interval]]) -> list[Interval]:

    (min_start, max_finish) = get_time_bucket_range(schedule=schedule)

    employee_count = len(schedule)

    all_common_free_times = []
    current_common_free_time_start = -1

    employee_time_bucket_codes: tuple[int, ...]
    employee_interval_indices_current: tuple[int, ...] = tuple([0] * employee_count)
    for time_bucket in range(min_start, max_finish + 1):

        employee_time_bucket_codes, employee_interval_indices_current = zip(*[
            employee_free_at_time_bucket(
                time_bucket=time_bucket,
                employee_intervals=employee_intervals,
                employee_interval_index=employee_interval_indices_current[employee_index],
            )
            for employee_index, employee_intervals in enumerate(schedule)
        ])

        if -1 in employee_time_bucket_codes:
            assert current_common_free_time_start == -1

        elif 0 in employee_time_bucket_codes:
            if current_common_free_time_start >= 0:
                # finalize the free-time interval
                all_common_free_times.append(Interval(current_common_free_time_start, time_bucket))
                # reset
                current_common_free_time_start = -1

        elif all(elt == 1 for elt in employee_time_bucket_codes):
            if current_common_free_time_start == -1:
                current_common_free_time_start = time_bucket

    return all_common_free_times


def employee_free_at_time_bucket(
        time_bucket: int,
        employee_intervals: list[Interval],
        employee_interval_index: int,
) -> tuple[int, int]:
    # BEFORE first work interval start time?
    if employee_interval_index == 0 and time_bucket < employee_intervals[0].start:
        return 1, 0

    # AFTER final work interval end time?
    if employee_interval_index >= len(employee_intervals):
        return 1, employee_interval_index

    interval = employee_intervals[employee_interval_index]
    if time_bucket == interval.start:
        return 0, employee_interval_index

    if interval.start < time_bucket < interval.end:
        return -1, employee_interval_index

    if time_bucket >= interval.end:
        return 1, (employee_interval_index + 1)
    else:
        return 1, employee_interval_index






if __name__ == '__main__':
    # res = employee_free_time_impl(
    #     schedule=[
    #         [
    #             Interval(1, 2),
    #             Interval(5, 6),
    #         ],
    #         [
    #             Interval(1, 3),
    #         ],
    #         [
    #             Interval(4, 10),
    #         ],
    #     ]
    # )
    # x=  0
    res = employee_free_time_impl(
        schedule=[
            [
                Interval(1, 3),
                Interval(6, 7),
            ],
            [
                Interval(2, 4),
            ],
            [
                Interval(2, 5),
                Interval(9, 12),
            ],
        ]
    )
    x = 0