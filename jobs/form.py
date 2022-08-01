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
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False, widget=forms.URLInput(
        attrs={'placeholder': 'https://www.example.com', 'size': '50'}))
    employment_type = forms.ChoiceField(choices=jobtype)
    start_date = forms.DateField(
        help_text="The earliest date you can start working.",
        widget=forms.SelectDateWidget(
            years=('2022', '2023'),
            empty_label=("Choose Year", "Choose Month", "Choose Day")
        )
    )
    available_days = forms.MultipleChoiceField(
        choices=days, help_text="Select all the days that you can work.", widget=forms.CheckboxSelectMultiple,
        initial=("monday", "tuesday", "wednesday", "thursday", "friday"))
    desired_hourly_wage = forms.DecimalField(widget=forms.NumberInput(
        attrs={'min': '10.00', 'max': '100.00', 'step': '.25'}))
    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '75', 'rows': '5'}))
    confirmation = forms.BooleanField(
        label="I certify that the information I have provided is true.")
