from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    numbers = [38, 33, 12, 27, 87, 45, 67, 57]
 
    #Sorting list of Integers
    numbers.sort(reverse=True)
    return "Second largest number :"+ str(numbers[1])


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)