from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    
    a = []

    for e in range(1,40,1):
        if (e%2) == 0:
            a.append(e)
    return a


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

