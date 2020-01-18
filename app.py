import json

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = dict(request.form)
        exp = list()
        for cname, cpos, cstart, cend, cdescription in zip(request.form.getlist('cname'),request.form.getlist('cpos'),request.form.getlist('cstart'),request.form.getlist('cend'),request.form.getlist('cdescription')):
            exp.append(dict({
                'cname': cname, 'cpos': cpos, 'cstart': cstart, 'cend': cend, 'cdescription':cdescription
            }))
        data['skills'] = data['skills'].split(', ')
        return render_template('cv.html',len_skills=len(data['skills']) , data=data, experience=exp, len_exp=len(exp))

@app.route('/howtouse')
def howtouse():
    return render_template('howtouse.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)