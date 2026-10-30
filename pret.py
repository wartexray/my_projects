from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

com = 0
per = 0
nich = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    
    global com 
    global per
    global nich
    g = ["камень", "ножницы", "бумага"]
    comp = random.choice(g)
    result = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'button1':
            if comp == "бумага":
                result = "вы проиграли, бот выбрал бумагу"
                com += 1
            elif comp == "камень":
                result = "ничья, бот выбрал тоже, что и вы"
                nich += 1
            else:
                result = "вы выйграли, бот выбрал ножницы"
                per += 1
        elif action == 'button2':
            if comp == "бумага":
                result = "вы выйграли, бот выбрал бумагу"
                per += 1
            elif comp == "камень":
                result = "вы проиграли, бот выбрал камень"
                com += 1
            else:
                result = "ничья, бот выбрал тоже, что и вы"
                nich += 1
        elif action == 'button3':
            if comp == "бумага":
                result = "ничья, бот выбрал тоже, что и вы"
                nich += 1
            elif comp == "камень":
                result = "победа, бот выбрал камень"
                per += 1
            else:
                result = "вы проиграли, бот выбрал ножницы"
                com += 1
        if per == 10:
            result = "вы выйграли"
            com = 0
            per = 0
            nich = 0
        if com == 10:
            result = "вы проиграли"
            com = 0
            per = 0
            nich = 0
        if nich == 10:
            result = "ничья"
            com = 0
            per = 0
            nich = 0
            
    return render_template('index.html', result=result, com=com, per=per, nich=nich)


if __name__ == '__main__':
    app.run(debug=True)