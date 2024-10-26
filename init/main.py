from fastapi import FastAPI, Body, Header, Response

app = FastAPI()

@app.get("/")
def init():
    return "Hello World!"

# parameter test
# http -b localhost:8000/hi/damgom
@app.get("/hi/{who}")
def param_test(who):
    return f"Hello {who}"

# http -b localhost:8000/h who==damgom
# http://localhost:8000/h?who=damgom
@app.get("/h")
def hi(who):
    return f"Hello {who}"

@app.get("/hello")
def greet(who: str = Header()):
    return f"Hello {who}?"

# post test
# import requests r = requests.post("http://localhost:8000/hi", json={"who: damgom"})
@app.post("/hi")
def post_test(who: str = Body(...)):
    return f"Hello {who}"

# status code test
# http localhost:8000/happy
@app.get("/happy")
def status_code_test(status_code=200):
    return ":)"

# response header test
# http localhost:8000/header/marco/polo
@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)