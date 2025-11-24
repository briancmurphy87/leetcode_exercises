# class Solution:
#     def climbStairs(self, n: int) -> int:
#         pass

def climb_stairs_impl(n: int, tally: int) -> int:
    t1 = 1, n-1
    t2 = 2, n-2
    for (step_size, steps_remaining) in (t1, t2):
        if steps_remaining <= 2:
            tally += 1
        # if steps_remaining >= 2:
        else:
            climb_stairs_impl(steps_remaining, tally)

    return tally


def climb_stairs(n: int) -> int:
    return climb_stairs_impl(n, 0)


if __name__ == '__main__':
    print(climb_stairs(3))