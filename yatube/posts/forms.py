from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image',)
        labels = {
            'text': 'Текст поста',
            'group': 'Группа',
            'image': 'Прикрепите изображение',
        }
        help_texts = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относиться пост',
        }

        def clean_text(self):
            data = self.cleaned_data['text']
            if data == '':
                raise forms.ValidationError('Заполните эту форму!')
            return data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Текст комментария',
        }
        help_texts = {
            'text': 'Текст нового комментария',
        }
