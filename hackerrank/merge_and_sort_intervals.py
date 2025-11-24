# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/merge-and-sort-intervals/problem?isFullScreen=true

#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def merge_high_def_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Given an array of intervals [startTime, endTime],
    merge all overlapping intervals
    and return a sorted array of non-overlapping intervals

    :param intervals:
    :return:
    """
    intervals.sort(key=lambda x: x[0])

    output_intervals: list[list[int]] = [intervals[0]]
    for interval in intervals[1:]:
        i_start, i_finish = interval[0], interval[1]
        # no overlap? append to output
        if i_start > output_intervals[-1][1]:
            output_intervals.append(interval)

        # overlap with increase in 'end time'
        elif i_finish > output_intervals[-1][1]:
            output_intervals[-1] = [
                output_intervals[-1][0],
                i_finish
            ]
    return output_intervals

if __name__ == '__main__':
    pass
    # intervals_rows = int(input().strip())
    # intervals_columns = int(input().strip())
    #
    # intervals = []
    #
    # for _ in range(intervals_rows):
    #     intervals.append(list(map(int, input().rstrip().split())))
    #
    # result = mergeHighDefinitionIntervals(intervals)
    #
    # print('\n'.join([' '.join(map(str, x)) for x in result]))
