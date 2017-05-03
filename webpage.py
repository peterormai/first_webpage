from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def profile():
    return render_template("main.html")


@app.route('/postform', methods=['POST'])
def profile_result():
    title = request.form['title']
    story = request.form['story']
    criteria = request.form['criteria']
    estimation = request.form['estimation']
    status = request.form['status']
    with open('result.txt') as data:
        data_str = data.read().splitlines()
        story_id = str(len(data_str) + 1)
    with open('result.txt', 'a') as file:
        file.write('\n' + str(story_id + ','))
        file.write(str(title + ','))
        file.write(str(story + ','))
        file.write(str(criteria + ','))
        file.write(str(estimation + ','))
        file.write(str(status))
    return render_template('solution.html', data_list=data_str)
    # return render_template('main.html', name="Thank you, your story has been saved")


@app.route('/result')
def result():
    with open('result.txt') as data:
        data_str = data.read().splitlines()
        data_list = [item.split(',') for item in data_str]
        return render_template('solution.html', data_list=data_list)


if __name__ == '__main__':
    app.run(debug=None)
