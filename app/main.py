from fastapi import FastAPI, HTTPException, Depends
import models
import schemas
from database import engine, SessionLocal


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
         db.close()


# routes

@app.get('/')
async def home():
    """
    render the template of the website 
    where we will have the registration button, login button
    some beautiful images how it's working
    """
    pass

# auth routes

@app.post('/sign_up')
async def sign_up():
    pass

@app.post('/sign_in')
async def sign_in():
    pass

# routes that will be visible after registration and login

@app.get('/profile/{int:user_id}')
async def user_profile(user_id):
    """
    shows the user profile where user
    can sign in into his telegram profile

    Args:
        user_id (_type_): _description_
    """
    pass


@app.get('/subscription_categories')
async def subscription_list():
    """
    the list of categories for subscribe
    """
    pass

@app.route('/subscription_categories/{int:categorie_id}', methods=['GET', 'POST'])
async def subscribe(categorie_id):
    """
    user choose the categorie and subscribe to it 
    in the form where he can put the time when he want to receive news

    Args:
        categorie_id (_type_): _description_
    """
    pass