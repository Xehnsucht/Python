from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse
import urllib.request
import feedparser

# Установка некоторых глобальных переменных
num_fetch_threads = 2
enclosure_queue = Queue()
# В реальном приложении вы не будете задавать данные в коде...
feed_urls = [
    'https://talkpython.fm/episodes/rss',
             ]

def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))

def download_enclosures(q):
    while True:
        message('looking for the next enclosure')
        url1 = q.get()
        filename = url1.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.request.urlopen(url1)
        data = response.read()
        # Сохранить загруженный файл в текущем каталоге
        message('writing to {}'.format(filename))
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        q.task_done()

for i in range(num_fetch_threads):
    worker = threading.Thread(
        target=download_enclosures,
        args=(enclosure_queue,),
        name='worker-{}'.format(i),
    )
    worker.setDaemon(True)
    worker.start()

for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries'][:5]:
        for enclosure in entry.get('enclosures', []):
            parsed_url = urlparse(enclosure['url'])
            message('queuing {}'.format(
                parsed_url.path.rpartition('/')[-1]
            ))
            enclosure_queue.put(enclosure['url'])
# Дождаться исчерпания очереди, что будет свидетельствовать
# о завершении обработки всех закачек
message('*** main thread waiting')
enclosure_queue.join()
message('*** done')
