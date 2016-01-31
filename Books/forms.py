from django import forms
from datetime import *

class edit_user_form(forms.Form):
    UserName = forms.CharField(max_length = 100)#user name.
    FirstName = forms.CharField(max_length = 100)# first name.
    LastName = forms.CharField(max_length = 100)# last name.
    Image = forms.ImageField(required=False)

class change_password_form (forms.Form):
    CurrentPassWord = forms.CharField(max_length = 100,widget=forms.PasswordInput)
    NewPassWord = forms.CharField(max_length = 100,widget=forms.PasswordInput)
    RepeatPassWord = forms.CharField(max_length = 100,widget=forms.PasswordInput)

class new_user_form(forms.Form):
    UserName = forms.CharField(max_length = 100)#user name.
    FirstName = forms.CharField(max_length = 100)# first name.
    LastName = forms.CharField(max_length = 100)# last name.
    Email = forms.EmailField() # email address.
    PassWord = forms.CharField(max_length = 100,widget=forms.PasswordInput )
    Image = forms.ImageField(required=False)


class login(forms.Form):
    Email = forms.EmailField()
    PassWord = forms.CharField(max_length = 100, widget=forms.PasswordInput )

Q_CHOICES = (
    (4,'New'),
    (3,'Like new'),
    (2,'Good'),
    (1,'Worn'),
    (0,'Old')
)

Date_Choices =(
    (1,'1 day 1 point'),
    (2,'1 week 5 points'),
    (3,'1 month 25 points')
)

Rating_Choices = (
    (1,'1 star'),
    (2,'2 stars'),
    (3,'3 stars'),
    (4,'4 stars'),
    (5,'5 stars')
)

Points_Choices = (
    (20, '15 points $20'),
    (40, '35 points $40'),
    (60, '55 points $60'),
    (80, '75 points $80'),
    (100, '95 points $100')
)

class new_book_form(forms.Form):
    Title = forms.CharField(max_length = 100)
    Author = forms.CharField(max_length = 100)
    Publisher = forms.CharField(max_length = 100)
    Genre = forms.CharField(max_length = 100)
    Abstract = forms.CharField(widget=forms.Textarea)
    Quality = forms.IntegerField(widget = forms.Select(choices = Q_CHOICES))
    FrontImage = forms.ImageField()
    BackImage = forms.ImageField(required=False)

class auction_form(forms.Form):
    BuyOutPrice = forms.IntegerField()
    BaseBidPrice = forms.IntegerField()
    MinBidInc = forms.IntegerField()
    EndTime = forms.IntegerField(widget = forms.RadioSelect(choices = Date_Choices))

class sale_form(forms.Form):
    SalePrice = forms.IntegerField()

class bid_form(forms.Form):
    Bid = forms.IntegerField()

class rate_form(forms.Form):
    rating = forms.IntegerField(widget = forms.Select(choices = Rating_Choices))

class text_form(forms.Form): # text form for Comments and complaints.
    Text = forms.CharField(widget=forms.Textarea)

class points_form(forms.Form):
    Amount = forms.IntegerField(widget = forms.Select(choices = Points_Choices))
    CardNumber = forms.IntegerField(required = False)
    SecurityCode = forms.CharField(required = False)
    Address = forms.CharField(widget = forms.Textarea, required = False)
