from django import forms 
from blog.models import Post,Comment


# Form for new posts which is linked to Posts and The fields that can be edited are who the author is maybe multiple users, Post title, and Text content 
class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {

            # class are connected to css to edit them 
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

        # class': 'form-control'
# connect it to comments field they can edit when posting a comment 

class CommentForm(forms.ModelForm):


    class Meta():
        model = Comment
        fields = ('author','text')

        # these widget's are coneted to css. widgets as dictionary and you have the fields along with widget type. Attributes alog with the class that will go to the css
        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }