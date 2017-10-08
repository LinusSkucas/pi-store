from django import forms
from captcha.fields import ReCaptchaField
from .models import Package

class PackageForm(forms.ModelForm):
	
	class Meta:
		model = Package
		fields = ['name', 'description', 'catagory', 'software', 'shot']
		labels = {'name':'Name of the package', 'description':"Description of the package", 'catagory':"The catagory of your package", 'software':"The software package (must be zip file)", 'shot':"Screen shot"}
	captcha = ReCaptchaField(public_key='6LdHkjMUAAAAABiskMwbzRI-kup-ZGzDIdLESh-v', private_key='6LdHkjMUAAAAACaKJ8QtctlVmKhsxFQoRcuZJjIf')
