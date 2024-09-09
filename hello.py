from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Amrit',
        'title': 'Test_1',
        'content': 'First post content',
        'date_posted': 'August 20, 2024'
    },
    {
        'author': 'Adrian',
        'title': 'Test_2',
        'content': 'Second post content',
        'date_posted': 'August 20, 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='New York Parliamentary Debate League')


@app.route("/about")
def about():
    return render_template('about.html', title='New York Parliamentary Debate League')

@app.route("/dropdown")
def drop():
    return render_template('dropdown.html')

@app.route('/test')
def test():
    return render_template('Bottom.html')
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        school = request.form.get('school')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Process form data (e.g., save to database, send an email, etc.)
        
        return redirect(url_for('thank_you'))  # Redirect after successful form submission
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return "Thank you for contacting us!"