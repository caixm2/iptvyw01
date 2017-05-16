from django import forms

class AddForm(forms.Form):
	a = forms.IntegerField()
	b = forms.IntegerField()

IPLEN_CHOICES = (
	('64C','64C'),('128C','128C'),('1B','1B'),('2B','2B'),('4B','4B'),('8B','8B'),('16B','16B')
	,('32B','32B'),('64B','64B'),('128B','128B')
)
DAY_CHOICES = (
	('1','1天内'),('31','31天内')
)
PLAT_CHOICES = (
	('HW','华为'),('ZTE','中兴')
)

class UsrInPoolForm(forms.Form):
	iplen = forms.CharField(widget = forms.Select(choices=IPLEN_CHOICES), initial=IPLEN_CHOICES[2][1])
	daylength = forms.CharField(widget = forms.Select(choices=DAY_CHOICES))
	plat = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=PLAT_CHOICES, label='查询平台')
	sip = forms.GenericIPAddressField(protocol = 'IPv4',required = True, label="单个IP：")
