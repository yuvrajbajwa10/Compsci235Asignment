from flask_wtf import CSRFProtect

from compsci235flix_app import main

CSRFProtect(main().config.from_object('config.Config'))
