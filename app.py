from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with link to Fortune page."""
    return render_template('index.html')


@app.route('/fortune')
def fortune():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_favorite_game = request.args.get("type")

    if users_favorite_game == 'Standard':
        fortune = "You choose a Standart game. Good Luck!"
    elif users_favorite_game == "Untimed":
        fortune = "You choose a Untimed game. Good Luck!"
    elif users_favorite_game == 'Wild':
        fortune = "You choose a Wild game. Good Luck!"
    else:
        fortune = "You choose a Blitz game. Good Luck!"

    return render_template('fortune_results.html', fortune=fortune)
