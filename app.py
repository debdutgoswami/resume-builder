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
        exp, skills, edu = list(), list(), list()

        # extracting experience
        for cname, cpos, cstart, cend, cdescription, clocation in zip(request.form.getlist('cname'),request.form.getlist('cpos'),request.form.getlist('cstart'),request.form.getlist('cend'),request.form.getlist('cdescription'),request.form.getlist('clocation')):
            exp.append(dict({
                'cname': cname, 'cpos': cpos, 'cstart': cstart, 'cend': cend, 'cdescription':cdescription, 'clocation':clocation
            }))
        # extracting skills
        for skill in request.form.getlist('skill'):
            skills.append(skill)
        # extracting education
        for clg, degree, gpa, start, end in zip(request.form.getlist('clg'), request.form.getlist('degree'), request.form.getlist('gpa'), request.form.getlist('start'), request.form.getlist('end')):
            edu.append({
                'clg':clg, 'degree': degree, 'gpa': gpa, 'start': start, 'end': end
            })
        return render_template('resume.html', skills=skills,len_skills=len(skills) , data=data, experience=exp, len_exp=len(exp), edu=edu, len_edu=len(edu))

@app.route('/howtouse')
def howtouse():
    return render_template('howtouse.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)