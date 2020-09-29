from flask import Flask, render_template
from parser import Parser
from config import Config

app = Flask(__name__)
cfg = Config()
p = Parser(cfg.USERNAME)


@app.route('/')
def index():
    projects = p.parse_repos()
    return render_template('index.html',
                            name = 'Kirill',
                            projects = projects)


if __name__ == '__main__':
    app.run()