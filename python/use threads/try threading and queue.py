from multiprocessing import Queue
import threading
import logging
import time
logging.basicConfig(level=logging.INFO)


def loggerHandler(data):
    time.sleep(5)
    logging.info("proceses by handler{}".format(data))


class Manager:
    def __init__(self, queue):
        self.queue = queue
        self.handlers = {}
        self.threads = []

    def bind(self, event, handler):
        self.handlers[event] = handler

    def run(self):
        self.run_thread = threading.Thread(target=self.listen, args=(self, ))
        self.run_thread.start()

    def listen(self, manager):
    # def listen(self):
        print('listening is on')
        logging.info('try this')
        while True:
            data = manager.queue.get()
            print('received in listening while cycle: ', data)
            event, package = data
            if event in manager.handlers:
                logging.info('launch {} processing thread'.format(event))
                new_thread = threading.Thread(target=manager.handlers[event], args=(package,))
                new_thread.start()
                manager.threads.append(new_thread)
            else:
                logging.info("{} is not binded".format(event))
            time.sleep(0.1)

def main():
    queue = Queue()
    manager = Manager(queue)
    manager.bind('logthis', loggerHandler)
    manager.run()
    print('all run')
    time.sleep(2)
    print("after 2 secs")
    queue.put(('logthis', 'some strings'))
    queue.put(('strangeEvent', 'some strange strings'))
    time.sleep(10)
    print('last message')

if __name__ == '__main__':
    main()