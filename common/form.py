from django import forms


class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), required=True, error_messages={"required": "Username不能为空！"})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), max_length=20, required=True, error_messages={'required': "Password不能为空！"})


class UserReisterForm(UserForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=20, required=True, error_messages={"required": "Username不能为空！"})
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), max_length=20, required=True, error_messages={"required": "Email不能为空！"})
    conf_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), max_length=20, required=True, error_messages={"required": "Placeholder不能为空！"})

