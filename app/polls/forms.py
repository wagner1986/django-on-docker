from django import forms



class ItemForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)

    def send_mail(self):
        print("salva item")
        nome = self.cleaned_data['nome']        