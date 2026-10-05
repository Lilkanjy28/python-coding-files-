import numpy as np
import time

now = time.strftime('%H:%M %p')
def log_time():
    with open('holder_list', 'a') as file:
        file.write(f'\nThis file was opened/accessed at: {now}')

    with open('holder_list', 'r') as file:
        content = file.read()

    print(content)

log_time()
