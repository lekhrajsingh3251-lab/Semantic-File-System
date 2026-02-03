import sys
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("File Created,", event.src_path)
        return super().on_created(event)
    def on_modified(self,event):
        print ("File modified:", event.src_path)
        return super().on_modified(event)

path = sys.argv[1] if len(sys.argv) > 1 else '.'
observer = Observer()
handler  = MyHandler()
observer.schedule(handler,path,recursive = True)
observer.start()
while True:
    cmd = input("> ")
    if cmd == "q":break
observer.stop()
observer.join()

