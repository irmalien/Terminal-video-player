import sys
import re


def update_config(config):
    if len(sys.argv) == 2:
        if bool(re.match(r"(http|https)", sys.argv[1])):
            config['source']['localFile'] = False
            config['source']['youtubeUrl'] = sys.argv[1]
            config['source']['webcam'] = False
        else:
            config['source']['localFile'] = sys.argv[1]
            config['source']['youtubeUrl'] = False
            config['source']['webcam'] = False
    return config
