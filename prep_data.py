' Script to prepare data from csv to be stored in SQLite database '

#!/usr/bin/env

from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, UnicodeText, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import sys
import logging

#---------------------------------------------------------------------------------------------------------------------------------------#


def load_data(file_name):
    ' Returns a list from csv data '
    csv_data = []
    with open(file_name, 'rb') as f:
        data = csv.reader(f)
        for d in data:
            csv_data.append(d)

    return csv_data

#---------------------------------------------------------------------------------------------------------------------------------------#

Base = declarative_base()


class FB_Data(Base):
    ' Model of data for names and categories '

    __tablename__ = 'FB_POSTS_DATA'

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String(100))
    message = Column(String(100))
    category = Column(String(100))
    author = Column(String(50))

    like = Column(Integer)
    share = Column(Integer)
    comment = Column(Integer)
    ctr = Column(Float)

    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    hour = Column(Integer)
    mins = Column(Integer)

    no_of_images = Column(Integer)
    no_of_videos = Column(Integer)
    head_len = Column(Integer)
    no_of_abusive_words = Column(Integer)


class Key_Data(Base):

    ' Model of data for keywords'

    __tablename__ = 'KEYWORDS_DATA'

    id = Column(String(100))
    keywords = Column(String(100), primary_key=True)
    like = Column(Integer)
    share = Column(Integer)
    comment = Column(Integer)
    ctr = Column(Float)

#---------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    t = time()

    # creating a log file
    logging.basicConfig(filename='api.log', level=logging.DEBUG)

    engine = create_engine('sqlite:///myData.sqlite')

    Base.metadata.create_all(engine)

    # Start of the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    ids = []

    print dir(FB_Data.__table__)

    file_name1 = "fb_posts_data.csv"
    file_name2 = "keywords_data.csv"

    fb_data = load_data(file_name1)
    key_data = load_data(file_name2)

    s.close()
    print "1"
    sys.exit()

    # Prefetch existing IDs
    for dt in s.query(FB_Data):
        ids.append(str(dt.id))

    file_name1 = "fb_posts_data.csv"
    file_name2 = "keywords_data.csv"

    fb_data = load_data(file_name1)
    key_data = load_data(file_name2)

    # Adding only those data in the original file which are not already
    # present.
    for i in range(len(fb_data)):
        if i > 0:
            if fb_data[i][0] not in ids:
                ids.append(fb_data[i][0])
            else:
                # Pick the existing ID and delete it.
                dat1 = s.query(FB_Data).filter_by(id=fb_data[i][0]).first()
                s.delete(dat1)

            # Add/update data
            fb_record = FB_Data(**{
                'id': fb_data[i][0],
                'name': fb_data[i][1],
                'message': fb_data[i][2],
                'category': fb_data[i][3],
                'author': fb_data[i][4],
                'like': fb_data[i][5],
                'share': fb_data[i][6],
                'comment': fb_data[i][7],
                'ctr': fb_data[i][8],
                'year': fb_data[i][9],
                'month': fb_data[i][10],
                'day': fb_data[i][11],
                'hour': fb_data[i][12],
                'mins': fb_data[i][13],
                'no_of_images': fb_data[i][14],
                'no_of_videos': fb_data[i][15],
                'head_len': fb_data[i][16],
                'no_of_abusive_words': fb_data[i][17]
            })
            s.add(fb_record)

    keys = []

    for dt in s.query(Key_Data):
        keys.append(str(dt.keywords))

    # Adding only those data in the original file which are not already
    # present.
    for i in range(len(key_data)):
        if i > 0:
            if key_data[i][1] not in keys:
                keys.append(key_data[i][1])
            else:
                # Pick the existing ID and delete it.
                dat2 = s.query(Key_Data).filter_by(
                    keywords=key_data[i][1]).first()
                s.delete(dat2)

            # Add/update data
            key_record = Key_Data(**{
                'id': key_data[i][0],
                'keywords': key_data[i][1],
                'like': key_data[i][2],
                'share': key_data[i][3],
                'comment': key_data[i][4],
                'ctr': key_data[i][5]
            })

            s.add(key_record)

    s.commit()  # Attempt to commit all the records

    s.close()  # Close the connection

    logging.debug("Time elapsed: " + str(time() - t) + " s.")
