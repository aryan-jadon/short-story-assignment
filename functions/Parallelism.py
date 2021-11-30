import ray
import time

# start Ray
ray.init()

@ray.remote
def f(x):
    time.sleep(3)
    return x

# start 5 tasks in parallel
result_ids = []
for i in range(5):
    result_ids.append(f.remote(i))

# Wait for the tasks to complete and retrieve the results
results = ray.get(result_ids)
print(results)
# [0, 1, 2, 3, 4]
