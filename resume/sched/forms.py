"""Forms to render HTML input & validate request data."""

from wtforms import Form, BooleanField, DateTimeField, PasswordField
from wtforms import TextAreaField, TextField
from wtforms.validators import Length, required, Required, EqualTo
from flask_security.forms import RegisterForm


class ExtendedRegisterForm(RegisterForm):
    name = TextField('Name', [Required()])
    company = BooleanField('Company account',)


# # Custom validators to check if user or email already exists
# def validate_user(form, field):
#   if db.session.query(User).filter_by(username=form.username.data).count() > 0:
#     raise validators.ValidationError('Username already exists')
#
# def validate_email(form, field):
#   if db.session.query(User).filter_by(email=form.email.data).count() > 0:
#     raise validators.ValidationError('Email already in use')
#
#
# class SignupForm(Form):
#   username = TextField('username', validators = [Required(), validate_user])
#   password = PasswordField('password', [
#     Required(message='Password cannot be empty'),
#     EqualTo('confirm', message='Passwords did not match'),
#     Length(min=8, max=100, message='Password too short')
#   ])
#   confirm = PasswordField('Repeat password', validators = [Required()])

class ResumeForm(Form):
  
    """Render HTML input for Resume model & validate submissions.

    This matches the models.Resume class very closely. Where
    models.Resume represents the domain and its persistence, this class
    represents how to display a form in HTML & accept/reject the results.
    """

    name = TextField('Name', [Length(max=255)])
    email = TextField('Email', [Length(max=100)])
    phone = TextField('Phone', [Length(max=255)])
    city = TextField('City', [Length(max=100)])
    zip = TextField('Zip', [Length(max=50)])
    country = TextField('Country', [Length(max=255)])
    url = TextField('Url', [Length(max=255)])
    citizenship = TextField('Country of Birth', [Length(max=255)])

    summary_title = TextField('Summary Title', [Length(max=255)])
    summary_text = TextField('Summary Text', [Length(max=500)])

    company_name = TextField('Company Name', [Length(max=255)])
    company_summary = TextField('Company Summary', [Length(max=255)])
    role = TextField('Role', [Length(max=255)])
    role_description = TextAreaField('Role Description')
    
    
    start = TextField('Start')
    end = TextField('End')
    currently = BooleanField('Currently')
    location = TextField('Location', [Length(max=255)])


    company_name_two = TextField('Company Name', [Length(max=255)])
    company_summary_two = TextField('Company Summary', [Length(max=255)])
    role_two = TextField('Role', [Length(max=255)])
    role_description_two = TextAreaField('Role Description')
    
    
    start_date = TextField('Start')
    end_date = TextField('End')
    currently_two = BooleanField('Currently')
    location_two = TextField('Location', [Length(max=255)])

    school_name_one = TextField('School Name One')
    degree_description = TextField('Degree Description')
    grading = TextField('Grading')
    start_date_school = TextField('Start')
    end_date_graduation = TextField('End')
    currently_three = BooleanField('Currently')
    location_school = TextField('Location School')
    city_school = TextField('City')
    country_school = TextField('Country')

    school_name_two = TextField('School')
    degree_description_two = TextField('Degree Description')
    grading_two = TextField('Grading')
    start_date_one = TextField('Start')
    end_date_two = TextField('End')
    currently_four = BooleanField('Currently')
    location_school_two = TextField('Location')
    city_school_two = TextField('City')
    country_school_two = TextField('Country')

    skills_one = TextField('Skills')
    skills_two = TextField('Skills')
    skills_three = TextField('Skills')
    skills_four = TextField('Skills')
    skills_five = TextField('Skills')
    skills_six = TextField('Skills')
    skills_seven = TextField('Skills')
    skills_eight = TextField('Skills')
    skills_nine = TextField('Skills')
    skills_ten = TextField('Skills')




class PositionForm(Form):
    position_title = TextField('Position title', [Length(max=255)])
    company_name = TextField('Company name', [Length(max=255)])
    location = TextField('Location', [Length(max=255)])
    company_website = TextField('Company website', [Length(max=255)])
    description = TextAreaField('Description')
    required_skill_one = TextField('Required skill', [Length(max=255)])
    required_skill_two = TextField('Required skill', [Length(max=255)])
    required_skill_three = TextField('Required skill', [Length(max=255)])
    required_skill_four = TextField('Required skill', [Length(max=255)])
    required_skill_five = TextField('Required skill', [Length(max=255)])
    required_skill_six = TextField('Required skill', [Length(max=255)])
    required_skill_seven = TextField('Required skill', [Length(max=255)])
    required_skill_eight = TextField('Required skill', [Length(max=255)])
    required_skill_nine = TextField('Required skill', [Length(max=255)])
    required_skill_ten = TextField('Required skill', [Length(max=255)])
    pub_date = DateTimeField('Publication start date')



class RegisteCompanyForm(Form):
    first_name = TextField('First name', [Length(max=255), Required()])
    last_name = TextField('Last name', [Length(max=255), Required()])
    email = TextField('E-mail', [Length(max=255), Required()])
    website = TextField('Website', [Length(max=255)])
    company_name = TextField('Company name', [Length(max=255), Required()])
    company_adress = TextAreaField('Company adress', [Required()])
    phone_number = TextField('Phone number', [Length(max=255), Required()])

class ContactForm(Form):
    subject = TextField('Message subject', [Length(max=255), Required()])
    text = TextAreaField('Message text', [Required()])


# class LoginForm(Form):
#     """Render HTML input for user login form.
#
#     Authentication (i.e. password verification) happens in the view function.
#     """
#     username = TextField('Username', [required()])
#     password = PasswordField('Password', [required()])
