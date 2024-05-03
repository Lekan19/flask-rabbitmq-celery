from tasks import add

# Send a task to the queue
result_1 = add.delay(4, 6)
result_2= add.apply_async((2, 2))
# Wait for the result
print('Waiting for result...')
print('Result:', result_1.get())
print('Result:', result_2.get())

