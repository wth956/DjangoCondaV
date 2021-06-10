from django import forms



from django.forms import ModelForm, Textarea
from .models import Rating

class RatingForm( ModelForm ):
	class Meta:
		model = Rating
		#fields = {'user', 'rating', 'comment'}
		fields = {'rating', 'comment'}
		widgets = {'comment': Textarea(attrs={'cols': 20, 'rows': 3}), }





'''
1. 閃靈
2. 亂彈
3. 南拳媽媽
4. 脫拉庫
5. 旺福
6. 四分衛
7. 信樂團
8. FIR 飛兒
9. 蘇打綠
10.五月天

'閃靈'
'亂彈'
'南拳媽媽'
'脫拉庫'
'旺福'
'四分衛'
'信樂團'
'飛兒'
'蘇打綠'
'五月天'

'''

'''
"Angelica"
"Bill"
"Chan"
"Dan"
"Hailey"
"Jordyn"
"Sam"
"Veronica"
'''
movies=['Alien','Alien']

similarity_choices=(('0','Female'),('1','Male'))

movie_choices=(
      ('Alien','Alien'),
      ('Alien','Avatar'),
      ('Blade Runner','Blade Runner'),
      ('Braveheart','Braveheart'),
      ('Dodgeball','Dodgeball'),
      ('Forest Gump','Forest Gump'),
      ('Gladiator','Gladiator'),
      ('Jaws','Jaws'),
      ('Kazaam' ,'Kazaam'),
      ('Lord of the Rings','Lord of the Rings'),
      ('Napolean Dynamite','Napolean Dynamite'),
      ('Old School','Old School'),
      ('Pootie Tang','Pootie Tang'),
      ('Pulp Fiction','Pulp Fiction'),
      ('Scarface','Scarface'),
      ('Shawshank Redemption','Shawshank Redemption'),
      ('Snakes on a Plane','Snakes on a Plane'),
      ('Spiderman','Spiderman'),
      ('Star Wars','Star Wars'),
      ('The Dark Knight','The Dark Knight'),
      ('The Happening','The Happening'),
      ('The Matrix','The Matrix'),
      ('Toy Story','Toy Story'),
      ('Village','Village'),
      ('You Got Mail','You Got Mail')
      )

name_choices=(
	("Aaron","Aaron"),
	("Amy","Amy"),
	("Ben","Ben"),
	("Bob","Bob"),
	("Brian","Brian"),
	("Bryan","Bryan"),
	("Chris","Chris"),
	("Erin","Erin"),
	("Gary","Gary"),
	("Greg","Greg"),
	("Heather","Heather"),
	("Jeff","Jeff"),
	("Jessica","Jessica"),
	("Jonathan","Jonathan"),
	("Josh","Josh"),
	("Katherine","Katherine"),
	("Matt","Matt"),
	("Patrick C","Patrick C"),
	("Patrick T","Patrick T"),
	("Stephen","Stephen"),
	("Thomas","Thomas"),
	("Valerie","Valerie"),
	("Vanessa","Vanessa"),
	("Zak","Zak"),
	("Zwe","Zwe")
	)


number_choices=(
	(-1,'-1'),
	(1,'1'),
	(2,'2'),
	(3,'3'),
	(4,'4'),
	(5,'5'))



class MovieUserInputForm(forms.Form):	
	movie1 = forms.ChoiceField(label='Alien',  choices = number_choices, required=False)
	movie2 = forms.ChoiceField(label='Avatar',   choices = number_choices, required=False)
	movie3 = forms.ChoiceField(label='Blade Runner',choices = number_choices, required=False)
	movie4 = forms.ChoiceField(label='Braveheart',  choices = number_choices, required=False)
	movie5 = forms.ChoiceField(label='Dodgeball',   choices = number_choices, required=False)
	movie6 = forms.ChoiceField(label='Forest Gump', choices = number_choices, required=False)
	movie7 = forms.ChoiceField(label='Gladiator', choices = number_choices, required=False)
	movie8 = forms.ChoiceField(label='Jaws',   choices = number_choices, required=False)
	movie9 = forms.ChoiceField(label='Kazaam',  choices = number_choices, required=False)
	movie10 = forms.ChoiceField(label='Lord of the Rings', choices = number_choices, required=False)
	movie11 = forms.ChoiceField(label='Napolean Dynamite', choices = number_choices, required=False)
	movie12 = forms.ChoiceField(label='Old School', choices = number_choices, required=False)
	movie13 = forms.ChoiceField(label='Pootie Tang', choices = number_choices, required=False)
	movie14 = forms.ChoiceField(label='Pulp Fiction', choices = number_choices, required=False)
	movie15 = forms.ChoiceField(label='Scarface', choices = number_choices, required=False)
	movie16 = forms.ChoiceField(label='Shawshank Redemption', choices = number_choices, required=False)
	movie17 = forms.ChoiceField(label='Snakes on a Plane', choices = number_choices, required=False)
	movie18 = forms.ChoiceField(label='Spiderman', choices = number_choices, required=False)
	movie19 = forms.ChoiceField(label='Star Wars', choices = number_choices, required=False)
	movie20 = forms.ChoiceField(label='The Dark Knight', choices = number_choices, required=False)
	movie21 = forms.ChoiceField(label='The Happening', choices = number_choices, required=False)
	movie22 = forms.ChoiceField(label='The Matrix', choices = number_choices, required=False)
	movie23 = forms.ChoiceField(label='Toy Story', choices = number_choices, required=False)
	movie24 = forms.ChoiceField(label='Village', choices = number_choices, required=False)
	movie25 = forms.ChoiceField(label='You Got Mail', choices = number_choices, required=False)



class MovieUserNameForm(forms.Form):
	user_name = forms.ChoiceField(label='輸入姓名', choices = name_choices)

class MovieSelectForm(forms.Form):
	movie_name = forms.ChoiceField(label='選擇這個電影',choices = movie_choices)
