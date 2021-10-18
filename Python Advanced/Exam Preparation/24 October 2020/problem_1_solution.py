from collections import deque

jobs_queue = deque(int(x) for x in input().split(', '))
wanted_job_index = int(input())

wanted_job = jobs_queue[wanted_job_index]
total_cycles = 0
count = -1
while jobs_queue:
    count += 1
    job = jobs_queue.popleft()
    if job < wanted_job:
        total_cycles += job
    elif job == wanted_job and count <= wanted_job_index:
        total_cycles += job

print(total_cycles)