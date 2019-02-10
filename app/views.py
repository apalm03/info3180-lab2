"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
import datetime
from flask import render_template, request, redirect, url_for, flash



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Aaron Myrie")
    
@app.route('/profile/')
def profile():
    userInfo ={
        'displaypic' :url_for('static', filename='image/acm.jpg'),
        'fullname': 'Aaron Myrie',
        'username': 'acmyrie',
        'location': 'Kingston, Jamaica',
        'joined_date': format_date_joined(2018,12,22),
        'bio': "I am brilliant, talented young man who enjoys doing software and web development. If you wish to work on a new project, you can contact me." ,
        'num_of_posts': '20',
        'num_of_followers': '200',
        'num_following': '100'
    }
    return render_template('profile.html', userinfo = userInfo);
    
    
    
##now = datetime.datetime.now() # today's date
def format_date_joined(year,month,day):
    date_joined = datetime.date(year, month, day) # a specific date
    return "Joined " + date_joined.strftime("%B, %Y") 
    


###
# The functions below should be applicable to all Flask apps.
###

 
    
    


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
