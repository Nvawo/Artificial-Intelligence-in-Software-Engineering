from typing import List, Optional
from sqlalchemy import String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

# 1. Declarative Base Model
class Base(DeclarativeBase):
    pass

# 2. User Model Mapping
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

# 3. Database Repository Class
class UserDataRepository:
    def __init__(self, db_url: str = "sqlite:///example_db.db"):
        self.engine = create_engine(db_url, echo=False)
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def create_user(self, username: str, email: str) -> Optional[User]:
        if not username or not email:
            print("Validation Error: Username and email are required.")
            return None

        with self.SessionLocal() as session:
            try:
                new_user = User(username=username, email=email)
                session.add(new_user)
                session.commit()
                session.refresh(new_user)
                print(f"User '{username}' created successfully with ID {new_user.id}.")
                return new_user
            except SQLAlchemyError as e:
                session.rollback()
                print(f"Database Error creating user '{username}': {e}")
                return None

    def get_user_by_username(self, username: str) -> Optional[User]:
        with self.SessionLocal() as session:
            return session.query(User).filter(User.username == username).first()

    def update_user_email(self, username: str, new_email: str) -> bool:
        with self.SessionLocal() as session:
            try:
                user = session.query(User).filter(User.username == username).first()
                if not user:
                    print(f"User '{username}' not found.")
                    return False
                user.email = new_email
                session.commit()
                print(f"Updated email for '{username}' to '{new_email}'.")
                return True
            except SQLAlchemyError as e:
                session.rollback()
                print(f"Error updating email for '{username}': {e}")
                return False

    def delete_user(self, username: str) -> bool:
        with self.SessionLocal() as session:
            try:
                user = session.query(User).filter(User.username == username).first()
                if not user:
                    print(f"User '{username}' not found.")
                    return False
                session.delete(user)
                session.commit()
                print(f"User '{username}' deleted successfully.")
                return True
            except SQLAlchemyError as e:
                session.rollback()
                print(f"Error deleting user '{username}': {e}")
                return False

    def list_users(self) -> List[User]:
        with self.SessionLocal() as session:
            return session.query(User).all()

# --- local Test Execution ---
if __name__ == "__main__":
    repo = UserDataRepository()

    print("--- Testing Create ---")
    repo.create_user("johndoe", "john@example.com")
    repo.create_user("janedoe", "jane@example.com")

    print("\n--- Testing Read ---")
    user = repo.get_user_by_username("johndoe")
    print("Fetched User:", user)

    print("\n--- Testing Update ---")
    repo.update_user_email("johndoe", "john.doe@updated.com")

    print("\n--- Testing List All ---")
    all_users = repo.list_users()
    print("All Users:", all_users)

    print("\n--- Testing Delete ---")
    repo.delete_user("janedoe")