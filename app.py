from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from database import save_email_to_db
from emailing import send_email

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


@app.post("/signed_up", response_class=HTMLResponse)
def signed_up(request: Request, email: str = Form("john@nightwatch.com")):
    save_email = save_email_to_db(email)
    if save_email:
        send_email("You've signed up for the Rebelbean Test Roast alert!", email)
    return templates.TemplateResponse("signed_up.html", {"request": request, "email": email})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8080, debug=True)
