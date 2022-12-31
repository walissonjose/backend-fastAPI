from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GenericBase(Base):
    __abstract__ = True
