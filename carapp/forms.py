from django import forms


# from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #  widget=forms.PasswordInput用于指定该字段在form表单里表现为<input type='password' />，也就是密码输入框。
    # captcha = CaptchaField(label='验证码')


class RegisteForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    passwd = forms.CharField(label='用户密码', max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    passwd2 = forms.CharField(label='确认密码', max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='邮箱', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='电话', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    img = forms.ImageField(label='头像', allow_empty_file=True, required=False)
