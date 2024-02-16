from django import forms

class CreateNewTask(forms.Form):
    titulo = forms.CharField(label="Titulo de la tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'text'}))
    descripcion = forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea(attrs={'class':'text'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200,widget=forms.TextInput(attrs={'class':'text'}))