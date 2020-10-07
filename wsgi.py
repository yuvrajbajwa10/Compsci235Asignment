"""App entry point."""
from compsci235flix_app import main

app = main()
app.config.from_object('config.Config')

if __name__ == "__main__":
    app.run(host='localhost', port=5000, threaded=False)


