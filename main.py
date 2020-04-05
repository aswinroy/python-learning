from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'aswin roy',
        'title': 'blog post 1',
        'content': 'first blog post',
        'date_posted': 'april 5, 2020'
    },
    {
        'author': 'akhil mohan',
        'title': 'blog post 2',
        'content': 'second blog post',
        'date_posted': 'april 6, 2020'
    }

]


@app.route("/")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
