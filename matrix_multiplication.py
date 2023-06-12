from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    # Program to multiply two matrices using nested loops

    # 3x3 matrix
    X = [[10,5,2],
        [3 ,6,7],
        [6 ,7,8]]
    # 3x4 matrix
    Y = [[6,9,2,1],
        [7,7,3,0],
        [5,5,8,5]]
    # result is 3x4
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

    # iterate through rows of X
    for i in range(len(X)):
     # iterate through columns of Y
     for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

    return result


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

