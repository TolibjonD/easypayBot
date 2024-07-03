from sqlalchemy import create_engine, Column, Integer, String, Double, Boolean, delete, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

# Create SQLite database
engine = create_engine('sqlite:///data/mydb.db')
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column("fullname", String)
    username = Column("username", String)
    is_admin = Column(Boolean)
    date_joined = Column("date_joined", String)
    

class Services(Base):
    __tablename__ = 'services'
    id = Column("id",Integer, primary_key=True, autoincrement="auto")
    name = Column("name", String)
    percent = Column("percent", Double)
    date_joined = Column("date_joined", String)

class Currency(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    usd_to_try = Column("usd_to_try", Double)
    usd_to_uzs = Column("usd_to_uzs", Double)
    amount = Column("amount", Double)
    updated_at = Column("updated_at", String)

class Channels(Base):
    __tablename__ = "channels"
    id = Column(String, primary_key=True)
    name = Column("name", String)
    date = Column(String)

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

async def get_today_currency_by_date():
    return session.query(Currency).all()[-1]

async def get_all_channels_info():
    return session.query(Channels).all()

async def get_all_channels_id():
    return [channel.id for channel in session.query(Channels).all()]

async def check_user_existence(session, User, user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        return True
    else:
        return False
async def check_service_existence(name):
    service = session.query(Services).filter(Services.name == name).first()
    if service:
        return True
    else:
        return False
async def check_service_existence_by_id(ID):
    service = session.query(Services).filter(Services.id == ID).first()
    if service:
        return True
    else:
        return False
    
async def delete_service_by_id(ID):
    service = session.query(Services).filter_by(id=ID).first()
    session.delete(service)
    session.commit()
    
async def delete_channel_by_id(ID):
    item = session.query(Channels).filter_by(id=ID).first()
    session.delete(item)
    session.commit()

    
def select_admins_off():
    users = session.query(User).filter_by(is_admin=True)
    return [admin.id for admin in users]

async def select_admins():
    users = session.query(User).filter_by(is_admin=True).all()
    return [admin.id for admin in users]

async def count_users():
    users = session.query(User).all()
    return len(users)

async def count_admins():
    users = session.query(User).filter_by(is_admin=True)
    return len([users])

async def select_users_id():
    users = session.query(User).all()
    return [user.id for user in users]
# # Insert data
# # new_user = User(name='Alice', age=30)
# session.add(new_user)
# session.commit()

# Select data
async def selection(ModelName,admins=False):
    if admins:
        if session.query(ModelName).all():
            admins = session.query(ModelName).filter_by(is_admin=True).all()
            return admins
        else:
            return
    return session.query(ModelName).all()

async def makeAdmin(userID, status):
    user = session.query(User).filter_by(id=userID).first()
    user.is_admin = status
    session.commit()
    return user
# # Update data
# user = session.query(User).filter_by(name='Alice').first()
# user.age = 31
# session.commit()

# # Delete data
# user = session.query(User).filter_by(name='Alice').first()
# session.delete(user)
# session.commit()

# # Filter data
# users = session.query(User).filter(User.age > 25).all()
# for user in users:
#     print(user.name, user.age)
