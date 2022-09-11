from flask import Flask, render_template
import random
# import string

app = Flask(__name__)

thoughtList = [{
    'thought': 'When you start to doubt yourself the real world will eat you alive.',
    'speaker': 'Henry Rollins'
}, {
    'thought': 'Strength is the product of struggle, you must do what others don\'t to achieve what others won\'t.',
    'speaker': 'Henry Rollins'
}, {
    'thought': 'You need a little bit of insanity to do great things.',
    'speaker': 'Henry Rollins'
}, {
    'thought': 'No such thing as spare time, no such thing as free time, no such thing as down time. All you got is life time. Go.',
    'speaker': 'Henry Rollins'
}, {
    'thought': 'Do not waste time with normal people. They are a plague and will only slow you down.',
    'speaker': 'Henry Rollins'
}, {
    'thought': 'It\'s sad when someone you know becomes someone you knew.',
    'speaker': 'Henry Rollins'
}, {
    'thought': 'Being an artist is dragging your innermost feelings out, giving a piece of yourself, no matter in which art form, in which medium.',
    'speaker': 'Henry Rollins'
}, {
    'thought': 'I believe that one defines oneself by reinventionn. To not be like your parents. To not be like your friends. To be yourself. To cut yourself out of stone.',
    'speaker': 'Henry Rollins'
}]

randomThought = random.choice(thoughtList)


@app.route("/", methods=['GET'])
def base():
    return render_template('index.html', data=randomThought)


# @app.route("/", methods=['POST'])
# def get_thought():
#     if request.method == 'POST':
#         data = 'click'
#         return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
