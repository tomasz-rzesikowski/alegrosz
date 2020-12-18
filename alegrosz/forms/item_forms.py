from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, FloatField, TextAreaField, FileField, SelectField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Length


class ItemForm(FlaskForm):
    title = StringField('Title',
                        validators=[InputRequired('Input is required.'), DataRequired('Data is required.'),
                                    Length(min=5, max=20, message="Input mast be between 5 and 20 characters long.")])
    price = FloatField('Price')
    description = TextAreaField('Description',
                                validators=[InputRequired('Input is required.'), DataRequired('Data is required.'),
                                            Length(min=5, max=40,
                                                   message="Input mast be between 5 and 40 characters long.")])
    image = FileField('Image', validators=[FileAllowed(['jpeg', 'jpg', 'png'], message='Images only.')])


class NewItemForm(ItemForm):
    category = SelectField('Category', coerce=int)
    subcategory = SelectField('Subcategory', coerce=int)
    submit = SubmitField('Add item')


class EditItemForm(ItemForm):
    submit = SubmitField('Update item')


class DeleteItemForm(FlaskForm):
    submit = SubmitField('Delete all')
