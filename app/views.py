from app import app
from forms import NumberForm
import texting

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            texting.addNumber(form.number.data)
        else:
            flash('Invalid number')
    else:
        return render_template('index.html', form = form)
