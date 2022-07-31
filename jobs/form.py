from django import forms

jobtype = (
    (None, '--Please Choose--'),
    ('full-time', 'Full-Time'),
    ('part-time', 'Part-Time'),
    ('contract', 'Contract')
)

days = (
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
)


class JobApplicationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)
    employment_type = forms.ChoiceField(choices=jobtype)
    start_date = forms.DateField(
        help_text="The earliest date you can start working.")
    available_days = forms.MultipleChoiceField(
        choices=days, help_text="Select all the days that you can work.")
    desired_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(
        label="I certify that the information I have provided is true.")
