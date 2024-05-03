from tasks import add

res = add.apply_async((10, 10))
task = add.AsyncResult(res)
print("response: ", res)
print("task_id: ", res.id)
print("result_task: ", task.get())
print("result_task: ", task.result)
print("result_task: ", task.state)
print("result_task: ", task.status)
print("result_task: ", task.ready())

