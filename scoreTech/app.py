from flask import Flask, render_template, url_for, flash, redirect 
from forms import RegistrationForm, LoginForm, OTPForm, CreateUserForm, ForgotForm, ResetForm
from wtforms_sqlalchemy.fields import QuerySelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

posts = [
	{
		'author':'Abhishek',
		'title':'First week',
		'content':'lorem is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electroni',
		'date_of_publish':'20-02-1998'
	},
	{
		'author':'Akanksha',
		'title':'Testimony',
		'content':'lorem is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electroni',
		'date_of_publish':'21-02-1998'
	},
	{
		'author':'Jone doe',
		'title':'Experience',
		'content':'lorem is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electroni',
		'date_of_publish':'20-02-1998'
	},
	{
		'author':'Abhishek',
		'title':'Second week',
		'content':'lorem is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electroni',
		'date_of_publish':'20-02-1998'
	},
	{
		'author':'Akanksha',
		'title':'Testimony',
		'content':'lorem is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electroni',
		'date_of_publish':'21-02-1998'
	},
	{
		'author':'Jone doe',
		'title':'Experience',
		'content':'lorem is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electroni',
		'date_of_publish':'20-02-1998'
	}	
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('Account created', 'success')
		return redirect(url_for('check'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data =="abhi@gmail.com" and form.password.data =="abhi@123":
			flash('You have been Logged In', 'success')
			return redirect(url_for('home'))
		else:
			flash('please check youe email and password','danger')
	return render_template('login.html', title='Login', form=form)

@app.route('/check', methods=['GET', 'POST'])
def check():
	form = OTPForm()
	if form.validate_on_submit():
		flash('correct otp', 'success')
		return redirect(url_for('home'))
	return render_template('verify.html', title='verify', form=form)

@app.route('/createUser', methods=['GET','POST'])
def createUser():
	form = CreateUserForm()
	if form.validate_on_submit():
		flash('New user created', 'success')
		return redirect(url_for('loginOrCreate'))
	return render_template('create_user.html', title='Create User', form=form)

@app.route('/loginOrCreate', methods=['GET','POST'])
def loginOrCreate():
	return render_template('LoginOrCreate.html')

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
	form = ForgotForm()
	if form.validate_on_submit():
		flash('Mail has been sent to the provided email address','success')
		return redirect(url_for('reset'))
	return render_template('forgot.html', title='Forgot Password', form=form)

@app.route('/reset', methods=['GET', 'POST'])
def reset():
	form = ResetForm()
	if form.validate_on_submit():
		flash('Password is restored','success')
		return redirect(url_for('login'))
	return render_template('reset.html', title='Reset password', form=form)


if __name__ == '__main__':
	app.run(debug=True)

