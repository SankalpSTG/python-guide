from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.post("/is-logged-in")
def isLoggedIn():
    return {
        "message": "hello world"
    }


@auth_router.post("/sign-in-with-google")
def signIn():
    return {
        "message": "hello world"
    }