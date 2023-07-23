from talon import app

app.notify(body="Hello world")
app.notify(title="Hello world",
           subtitle="Welcome to Talon",
           body="Enjoy your stay.",
           sound=True)