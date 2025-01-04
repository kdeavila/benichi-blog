from django import forms
from .models import Comment

class BaseForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'w-full px-4 py-2 mt-1 text-sm border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-white'
            field.widget.attrs['widget_container'] = 'div'
            field.widget.attrs['widget_container_attrs'] = {'class': 'flex flex-col space-y-1 mb-4'}

class EmailPostForm(BaseForm, forms.Form):
    name = forms.CharField(
        max_length=25,
        label='Nombre',
        widget=forms.TextInput(attrs={
            'placeholder': 'Tu nombre',
            'class': 'w-full px-4 py-2 mt-1 text-sm border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none bg-white'
        })
    )
    to = forms.EmailField(
        label='Destinatario',
        widget=forms.EmailInput(attrs={
            'placeholder': 'correo@ejemplo.com',
            'class': 'w-full px-4 py-2 mt-1 text-sm border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none bg-white'
        })
    )
    comments = forms.CharField(
        required=False,
        label='Comentarios',
        widget=forms.Textarea(attrs={
            'placeholder': 'Escribe tus comentarios aquí...',
            'rows': 4,
            'class': 'w-full px-4 py-2 mt-1 text-sm border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none bg-white resize-none'
        })
    )

class CommentForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        labels = {
            'name': 'Nombre',
            'email': 'Correo electrónico',
            'body': 'Comentario'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Tu nombre',
                'class': 'w-full px-4 py-2 mt-1 text-sm border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent focus:outline-none bg-white'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'correo@ejemplo.com',
                'class': 'w-full px-4 py-2 mt-1 text-sm border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent focus:outline-none bg-white'
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'Escribe tu comentario aquí...',
                'rows': 6,
                'class': 'w-full px-4 py-2 mt-1 text-sm border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent focus:outline-none bg-white resize-none'
            })
        }

class SearchForm(BaseForm, forms.Form):
    query = forms.CharField(
        label='Búsqueda',
        widget=forms.TextInput(attrs={
            'placeholder': 'Buscar...',
            'class': 'w-full px-4 py-2 text-sm border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent focus:outline-none bg-white'
        })
    )