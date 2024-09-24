from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed

from wtforms import BooleanField, FileField, PasswordField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo

from app.models.user import User


class RegistrationForm(FlaskForm):
    name = StringField('ФИО', validators=[
                       DataRequired(), Length(min=2, max=100)])
    login = StringField('Логин', validators=[
        DataRequired(), Length(min=2, max=20)], render_kw={
        'class': 'form-control',
        'placeholder': 'Логин'
    })
    password = PasswordField('Пароль', validators=[
        DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[
        DataRequired(), EqualTo('password')])
    avatar = FileField('Загрузите свое фото', validators=[
                       FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Зарегистрироваться')

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError(
                "Данное имя пользователя уже занято! Пожалуйста выберите другое имя пользователя.")
        
class LoginForm(FlaskForm):
    """Form to log in users"""
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class StudentForm(FlaskForm):
    student = SelectField('student', choices=[], render_kw={'class': 'form-control'})
