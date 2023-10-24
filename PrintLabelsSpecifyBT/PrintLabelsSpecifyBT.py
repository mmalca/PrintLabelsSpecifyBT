path_to_watch = "your/path"
print('Your folder path is"',path,'"')
previous_files_capture = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
        current_files_capture = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in current_files_capture if not f in previous_files_capture]
        if added:
            #create a new file with the relevant info in another location (for the printer)
                ###print("Added: ", ", ".join (added))
                break
        else:
             previous_files_capture = current_files_capture
