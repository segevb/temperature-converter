from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def my_form(): ## This function prints homescreen's web app
    celsius = request.args.get("tempInCelsius", "")
    if celsius:
        try:
            fahrenheit = str(float(celsius) * 9.0/5 + 32)
        except:
            fahrenheit = "That's not a number!"
    else:
        fahrenheit = ""
    return ('''
            <!DOCTYPE html>
            <html>
            <body>
            <form action="" method="get">
            <h1>Segev's Temperature Converter Web App</h1>
            <h4>(Please enter a value in Celsius, and it will be converted to Fahrenheit)</h4>
                <input type="text" name="tempInCelsius" value=''' + celsius + '''>
                <input type="submit" value="Convert">
                <p></p>
            </form>
            </body>
            </html>'''
            + fahrenheit
            )


if __name__ == '__main__':
    app.run()
