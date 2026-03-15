from fastapi import FastAPI
app = FastAPI()

# decorator: is a line of code that calls a function but with a specific logic
# this decorator: calls the function but if the user enters the URL/welcome
@app.get("/welcome")
# a normal fuction that return a dic
def welcome():
    return {
        "message": "Hello World!"
    }
