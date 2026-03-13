# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/hi")
# def greet():
#     return "Hello? World?"


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/hi/{who}")
# def greet(who):
#     return f"Hello? {who}?"


from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)