# =======> Creating File Handlers and Modules for Retrieving Information about Insulin ======>
import json
def readJsonFile(filename):
    data = ""
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data