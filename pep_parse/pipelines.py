from sqlalchemy import create_engine, Column, Date, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from scrapy.exceptions import DropItem

from itemadapter import ItemAdapter

Base = declarative_base()


class MondayPost(Base):
    __tablename__ = 'pep'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(50))

class PepParsePipeline:
    def process_item(self, item, spider):
        return item
