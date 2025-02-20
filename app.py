from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.drinks import router as drinks_router
from api.users import router as users_router
from api.coasters import router as coasters_router
from api.orders import router as orders_router

app = FastAPI()

# Include routers
app.include_router(drinks_router, prefix="/api", tags=["Drinks"])
app.include_router(users_router, prefix="/api", tags=["Users"])
app.include_router(coasters_router, prefix="/api", tags=["Coasters"])
app.include_router(orders_router, prefix="/api", tags=["Orders"])

@app.get("/")
def root():
    return {"message": "Welcome to the Drinks API!"}

# Allow frontend domain to access the API
origins = [
    "https://dev.drinks.mcgeld.com",
    "http://dev.drinks.mcgeld.com" # In case you use HTTP sometimes
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)