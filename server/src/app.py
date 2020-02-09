import os

from flask import Flask, render_template, request, make_response

app = Flask(__name__)


# home route
@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        # caching the content for 10 min
        template = render_template('home.html')
        response = make_response(template)
        response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'

        return response
    else:
        data = request.form # assigning request.form to data for better readability
        
        exp, skills, edu, projects, interests = list(), list(), list(), list(), list()

        # extracting experience
        for cname, cpos, cstart, cend, cdescription, clocation in zip(data.getlist('cname'),data.getlist('cpos'),data.getlist('cstart'),data.getlist('cend'),data.getlist('cdescription'),data.getlist('clocation')):
            exp.append({
                'cname': cname, 'cpos': cpos, 'cstart': cstart, 'cend': cend, 'cdescription':cdescription, 'clocation':clocation
            })

        # extracting skills
        for skill in data.getlist('skill'):
            skills.append(skill)

        # extracting education
        for clg, degree, gpa, start, end in zip(data.getlist('clg'), data.getlist('degree'), data.getlist('gpa'), data.getlist('start'), data.getlist('end')):
            edu.append({
                'clg':clg, 'degree': degree, 'gpa': gpa, 'start': start, 'end': end
            })

        # extracting projects
        for pname, pstart, pend, pdescription, plink in zip(data.getlist('pname'), data.getlist('pstart'), data.getlist('pend'), data.getlist('pdescription'), data.getlist('plink')):
            projects.append({
                'pname': pname, 'pstart': pstart, 'pend': pend, 'pdescription': pdescription, 'plink': plink
            })
        
        # extracting interests
        for interest in data.getlist('interest'):
            interests.append(interest)

        return render_template('resume.html', skills=skills, len_skills=len(skills) , data=data, experience=exp, len_exp=len(exp), edu=edu, len_edu=len(edu), projects=projects, len_projects=len(projects), interests=interests, len_interests=len(interests))



@app.route('/howtouse')
def howtouse():
    return render_template('howtouse.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',8080)), debug=True)