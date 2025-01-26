from collections import defaultdict
from copy import copy


class PrintQueue:
    def __init__(self, input: str):
        self.rules: defaultdict[list] = defaultdict(list)
        self.jobs: list[list[int]] = []
        # parse input
        at_rules = True
        for line in input.split("\n"):
            if line == "":
                at_rules = False
            elif at_rules:
                before, after = line.split("|")
                self.rules[int(before)].append(int(after))
            else:
                self.jobs.append([int(i) for i in line.split(",")])

    def _check_job(self, job: list[int]) -> bool:
        """Check to see if job passes all rules."""
        return all(
            all(n not in self.rules[job[i]] for n in job[0:i])
            for i in range(1, len(job))
        )

    @property
    def correct_jobs(self) -> list[list[int]]:
        return [j for j in self.jobs if self._check_job(j)]

    @property
    def incorrect_jobs(self) -> list[list[int]]:
        return [j for j in self.jobs if not self._check_job(j)]

    def fix_job(self, job: list[int]) -> list[int]:
        """Fix a job so that job is correctly ordered."""
        # works like a bubble sort, keep swapping till nothing happens
        changed = True
        new_job = copy(job)
        while changed:
            changed = False
            for i in range(1, len(new_job)):
                for n in new_job[0:i]:
                    if n in self.rules[new_job[i]]:
                        # found a problem, swap i and i-1
                        changed = True
                        new_job[i - 1], new_job[i] = new_job[i], new_job[i - 1]
        return new_job


def middle(l: list[int]) -> int:
    """Get the middle number in a list of ints."""
    return l[len(l) // 2]


def pt1(input: str) -> str:
    return str(sum(middle(j) for j in PrintQueue(input).correct_jobs))


def pt2(input: str) -> str:
    pq = PrintQueue(input)
    return str(sum(middle(pq.fix_job(j)) for j in pq.incorrect_jobs))


if __name__ == "__main__":
    with open("day05/input.txt", "r") as fin:
        input = fin.read().strip()
        print(pt1(input))
        print(pt2(input))
