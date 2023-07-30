from django import forms
class slform(forms.Form):
    num=forms.CharField(max_length=80,label='Seller Full Name',widget=forms.TextInput(attrs={'class':'custom'}))
    eml=forms.EmailField(label="Email")
    pno=forms.IntegerField(label='Phone Number')
    pname=forms.CharField(max_length=50,label='Product Name')
    prc=forms.IntegerField(label="Product price")
    cnt=forms.IntegerField(label="Quantity")
    Product_description=forms.CharField(widget=forms.Textarea(attrs={'row':5,'col':10}))
    #imag=forms.ImageField(label='Image of Product')
class verif(forms.Form):
    value=forms.CharField(max_length=11,label="Verify OTP")
class medi(forms.Form):
    imag=forms.ImageField(label="Submit images of product(atleat 3)")
class buyf(forms.Form):
    bnm=forms.CharField(label="Full Name",max_length=30)
    gml=forms.EmailField(label="Gmail")
    pn=forms.IntegerField(label="Phone Number")
    dob=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
class login(forms.Form):
    code=forms.CharField(label="Key")