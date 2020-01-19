import json

from flask import Flask, render_template, request

app = Flask(__name__)


# home route
@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = request.form # assigning request.form to data for better readability
        
        exp, skills, edu = list(), list(), list()

        # extracting experience
        for cname, cpos, cstart, cend, cdescription, clocation in zip(data.getlist('cname'),data.getlist('cpos'),data.getlist('cstart'),data.getlist('cend'),data.getlist('cdescription'),data.getlist('clocation')):
            exp.append(dict({
                'cname': cname, 'cpos': cpos, 'cstart': cstart, 'cend': cend, 'cdescription':cdescription, 'clocation':clocation
            }))

        # extracting skills
        for skill in data.getlist('skill'):
            skills.append(skill)

        # extracting education
        for clg, degree, gpa, start, end in zip(data.getlist('clg'), data.getlist('degree'), data.getlist('gpa'), data.getlist('start'), data.getlist('end')):
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