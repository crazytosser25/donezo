"""Database connection"""

from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase  # , Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
