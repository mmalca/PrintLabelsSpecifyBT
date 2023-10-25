import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


if __name__ == "__main__":
    print("Starting program...")
    patterns = ["*.csv"]
    ignore_patterns = None
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def created_new_file(event):
    #create a new file with the relevant info on another location
    print("New file created!")

def create_BT_CSV_file(src_file, dst_file, dst_path):
    pass

my_event_handler.on_created = created_new_file

path_file_from_specify = "." #"your/path", "." is the current directory
go_recursively = False #only on the current directory, not sub dirs
my_observer = Observer()
my_observer.schedule(my_event_handler, path_file_from_specify, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(30)
except KeyboardInterrupt:
    my_observer.sleep()
    my_observer.join()
