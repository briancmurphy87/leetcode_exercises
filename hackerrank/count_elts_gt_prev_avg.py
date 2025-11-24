
#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#


def count_response_time_regressions(response_times: list[int]) -> int:
    if not response_times or len(response_times) == 1:
        print(f"early exit; |response_times={response_times}")
        return 0

    count = 0
    prefix_sum = response_times[0]
    for i in range(1, len(response_times)):
        if response_times[i] > (prefix_sum / i):
            count += 1
        prefix_sum += response_times[i]
    return count
    # print(f"start recursion; |len(response_times)={len(response_times)}")
    # print()
    #
    # return count_response_time_regressions_iter(
    #     response_times=response_times,
    #     curr_index=1,
    #     curr_sum=response_times[0],
    #     out_count=0,
    # )

def count_response_time_regressions_iter(
    response_times: list[int],
    curr_index: int,
    curr_sum: int,
    out_count: int,
) -> int:
    # check for stopping condition
    if curr_index >= len(response_times):
        return out_count

    curr_elt = response_times[curr_index]
    curr_avg = curr_sum / curr_index

    # check if increment counter
    if curr_elt > curr_avg:
        out_count += 1

    print(f"|curr_index={curr_index} |curr_elt={curr_elt} |counter={out_count} |curr_avg={curr_avg} |curr_sum={curr_sum}")

    # update for next eval
    return count_response_time_regressions_iter(
        response_times=response_times,
        curr_index=curr_index + 1,
        curr_sum=curr_sum + response_times[curr_index],
        out_count=out_count,
    )


if __name__ == "__main__":
    # map_sum = MapSum()
    print(count_response_time_regressions([100, 200, 150,300]))