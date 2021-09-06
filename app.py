from flask_wtf import CSRFProtect

from compsci235flix_app import main

app = main()
app.config.from_object('config.Config')
app.run()