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


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/hi")
# def greet(who):
#     return f"Hello? {who}?"


from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/hi")
def greet(who: str = Body(embed=True)):
    return f"Hello? {who}?"


# from fastapi import FastAPI, Header

# app = FastAPI()

# @app.get("/hi")
# def greet(who: str = Header()):
#     return f"Hello? {who}?"


# from fastapi import FastAPI, Header

# app = FastAPI()

# @app.get("/agent")
# def get_agent(user_agent: str = Header()):
#     return user_agent


# @app.get("/happy")
# def happy(status_code=200):
#     return ":)"


# from fastapi import Response

# @app.get("/header/{name}/{value}")
# def header(name: str, value: str, response: Response):
#     response.headers[name] = value
#     return "normal body"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)