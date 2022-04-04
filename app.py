import flask
from flask.views import MethodView
from wtforms import Form, StringField
from flask import Flask, render_template, request, redirect
from wtforms.fields.simple import SubmitField
from calorie_app.calorie import  Calorie
from calorie_app.temperature import Temperature

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return redirect("/calorie_form_page")


class CalorieFormPage(MethodView):

    def get(self):
        calorieform = CalorieForm()
        return(render_template('calorie_form_page.html', 
        calorieform = calorieform))

    def post(self):
        calorieform = CalorieForm(request.form)
        weight = calorieform.weight.data
        height = calorieform.height.data
        age = calorieform.age.data
        city = calorieform.city.data
        country = calorieform.country.data

        temperature = Temperature(country, city)
        try:
            calories = Calorie(weight, height, age, temperature.get())
        
            return(render_template('calorie_form_page.html', result = True, 
            calorieform = calorieform, amount1 = calories.calculate()))
        
        except:
            return(render_template('calorie_form_page.html', 
            calorieform = calorieform))





class CalorieForm(Form):
    weight = StringField('Weight: ')
    height = StringField('Height: ')
    age = StringField('Age: ')
    city = StringField('City: ')
    country = StringField('Country: ')
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie_form_page', 
view_func=CalorieFormPage.as_view('calorie_form_page'))

#app.run(debug=True)