from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

from database import save_email_to_db

app = FastAPI(
    title="Rebelbean Test Roast",
    description="Get notification about test roast availability",
    version="0.0.1"
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
@app.get("/home")
@app.get("/rebelbean")
def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get("/signed_up")
@app.post("/signed_up")
def signed_up(request: Request, email: str = Form("john.snow@nightwatch.com")):
    save_email_to_db(email)
    return templates.TemplateResponse("signed_up.html", {"request": request, "email": email})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8080, debug=True)
