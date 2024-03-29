"""App entry point."""
from flask_wtf import CSRFProtect

from compsci235flix_app import main

app = main()
app.config.from_object('config.Config')
csrf = CSRFProtect(app)

if __name__ == "__main__":
    app.run()
    csrf.init_app(app)

