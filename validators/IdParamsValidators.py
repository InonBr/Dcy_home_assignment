from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, UUID


class BlogIdParamsValidators(FlaskForm):
    blog_id = StringField('blog_id', validators=[DataRequired(), UUID()])

    @classmethod
    def from_dict(cls, data):
        if 'blog_id' not in data:
            raise ValueError('blog_id not found in data')
        return cls(blog_id=data['blog_id'])
