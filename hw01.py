from queue import Queue
import time
import random

queue = Queue()
request_counter = 0

def generate_request():
    global request_counter
    request_counter += 1
    request = {'name': f'order #{request_counter}'}
    queue.put(request)
    print(f'✅ Created: {request["name"]}')
    time.sleep(1)

def process_request():
    if queue.empty():
        print('No requests to process.')
        return
    request = queue.get()
    print(f'✅ Processed: {request["name"]}\n')
    time.sleep(0.5)

def main():
    random_num = random.randrange(2, 5)
    
    print('\nPRE-FILLING THE QUEUE:')
    print('-' * 50)
    for i in range(random_num):
        generate_request()
    
    print(f'\n📊 There are {queue.qsize()} requests in the queue\n')
    
    iteration = 1
    
    try:
        while True:
            print(f'ITERATION {iteration}:')
            print('-' * 50)
            
            generate_request()
            process_request()
            
            iteration += 1
    
    except KeyboardInterrupt:
        print('\n*** Process interrupted by user ***\n')

if __name__ == '__main__':
    main()
