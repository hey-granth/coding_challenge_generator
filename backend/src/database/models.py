from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm.session import sessionmaker


engine = create_engine("sqlite:///database.db", echo=True)
Base = declarative_base()


class Challenge(Base):
    __tablename__ = "challenges"

    id: int = Column(Integer, primary_key=True)
    difficulty: str = Column(String, nullable=False)
    created_by: str = Column(String, nullable=False)
    title: str = Column(String, nullable=False)
    options: str = Column(String, nullable=False)
    correct_answer_id: int = Column(Integer, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now)
    explanation: str = Column(String, nullable=False)


class ChallengeQuota(Base):
    __tablename__ = "challenge_quotas"

    id: int = Column(Integer, primary_key=True)
    user_id: str = Column(String, nullable=False, unique=True)
    remaining_quota: int = Column(Integer, nullable=False, default=50)
    last_reset_date: datetime = Column(DateTime, default=datetime.now)


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# autocommit=False: Changes are not committed to the database until explicitly done.
# autoflush=False: Changes are not flushed to the database before a query is executed.
# bind=engine: The engine to which the session is bound, allowing it to interact with the database.


# generator function to get a database session
# yield statements are mostly used in generator functions to produce a series of values over time
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Ensure the session is closed after use
