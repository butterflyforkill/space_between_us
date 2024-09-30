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

@app.route('/subscription_categories/{int:categorie_id}/subscribe', methods=['GET', 'POST'])
async def subscribe(categorie_id):
    """
    user choose the categorie and subscribe to it 
    in the form where he can put the time when he want to receive news

    Args:
        categorie_id (int): _description_
    """
    pass


@app.delete('/subscription_categories/{int:categorie_id}/unsubscribe')
async def unsubscribe(categorie_id):
    """
    user insubscribes from the news categorie
    (it'll delete it from the table UserSubscription and UserNotification)

    Args:
        categorie_id (int): _description_
    """
    pass




# it will be availble for the admin
# create the categorie
# delete the categorie
# update the categorie

@app.route('/admin/create_catogory', methods=['GET', 'POST'])
async def create_category():
    """
    availble only for the admin
    going to the form to create the catogory and send it to database
    """
    pass


@app.patch('/admin/update_category/{int:categorie_id}')
async def update_catogory(categorie_id):
    """
    getting the catogory by provided id and updates it, getting the values from the form

    Args:
        categorie_id (int): _description_
    """
    pass


@app.delete('/admin/delete_category/{int:categorie_id}')
async def delete_category(categorie_id):
    """
    getting the catogorie by provided id and delete it

    Args:
        categorie_id (int): _description_
    """
    pass
