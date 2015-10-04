from app import app
from forms import NumberForm
from flask import render_template, request
import reddit
import texting
import nyt
import stockList

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    try:
        reddit.postSubmissions(nyt.getArticles(stockList.stocks))
    except Exception:
        pass
    reddit.updateUsers()
    users, karma, gold = reddit.startGold()
    reddit.checkGold(users, karma, gold)
    message = ''
    for link, title in reddit.getTwenty():
        message = message + title + ". "
    texting.sendTexts(message)

    form = NumberForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            texting.addNumber(form.number.data)
        else:
            flash('Invalid number')
    else:
        return render_template('index.html', form = form, news = reddit.getTwenty())
