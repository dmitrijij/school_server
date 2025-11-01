import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OVER_DATA_DIR = os.path.join(BASE_DIR, "over_data")

os.makedirs(OVER_DATA_DIR, exist_ok=True)

def get_database_url(db_index=None):
    if db_index is not None:
        db_name = f"{db_index}.db"
    
    DB_PATH = os.path.join(OVER_DATA_DIR, db_name)
    return f"sqlite:///{DB_PATH}"

Base = declarative_base()

engine = None
SessionLocal = None

def init_db(db_index=None):
    global engine, SessionLocal
    
    DATABASE_URL = get_database_url(db_index)
    
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    Base.metadata.create_all(bind=engine)

def get_db():
    if SessionLocal is None:
        raise RuntimeError("База данных не инициализирована. Сначала вызовите init_db()")
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def switch_database(db_index):
    global engine, SessionLocal
    
    if engine:
        engine.dispose()
    
    DATABASE_URL = get_database_url(db_index)
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    Base.metadata.create_all(bind=engine)