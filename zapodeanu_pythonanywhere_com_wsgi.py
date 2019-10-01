
import sys
import os

path = '/home/zapodeanu/simple_webhook_receiver'
if path not in sys.path:
    sys.path.append(path)

from flask_receiver import app as application  # noqa
