import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init():
    global entries
    global next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        ids = []
        for e in entries:
            ids.append(e['id'])
        next_id = max(ids)+1
    except:
        entries = []

def get_entries():
    # This is important because the entries variable is stored in this file, and
    # to get it needs to be returned.
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    # time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id":next_id}
    entries.insert(0, entry) ## add to front of list
    next_id += 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(id_d):
    #print('\n\n\nID to delete:',id_d,'\n\n\n')
    global entries, GUESTBOOK_ENTRIES_FILE
    for i,e in enumerate(entries):
        #print('\n\n\n',e['id'],'\n\n\n')
        if str(e['id']) == str(id_d):
            index_to_delete = i
    del entries[index_to_delete]
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file after deleting.")
