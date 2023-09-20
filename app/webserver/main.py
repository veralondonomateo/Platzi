#Con fastapi podemos desplegar una página web a través de python
# El archivo debe llamarse main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3,4,5]

@app.get('/contact', response_class = HTMLResponse)
def get_list():
    return """


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us - Doctor Clinic</title>
    <link rel="stylesheet" href="styles.css"> <!-- Make sure to link your CSS file here -->
</head>
<body>
    <header>
        <h1>Doctor Clinic</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="services.html">Services</a></li>
                <li><a href="contact.html">Contact</a></li>
                <li><a href="about.html">About Us</a></li>
            </ul>
            <img src = "https://images.unsplash.com/photo-1629909613654-28e377c37b09?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2xpbmljfGVufDB8fDB8fHww&w=1000&q=80">
        </nav>
    </header>
    <main>
        <section id="about">
            <h2>About Us</h2>
            <p>Welcome to Doctor Clinic, your trusted healthcare provider. Our dedicated team of medical professionals is committed to providing top-notch healthcare services to our patients. With years of experience and a passion for healthcare, we strive to ensure your well-being and peace of mind.</p>
            <p>At Doctor Clinic, we offer a wide range of medical services, including general check-ups, specialized treatments, and preventive care. Your health is our priority, and we are here to support you on your journey to wellness.</p>
        </section>
        <section>
            <h1>
                Here are some images about our cosultary
             </h1>
             <h2>
                Welcome to our consultory, We are here for to be a service
              </h2>
              <section>
                    <img src = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fdepositphotos.com%2Fphotos%2Fclinic.html&psig=AOvVaw26cSPNckfkOQ1j8NIdSAt-&ust=1694618021617000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKCo9rSupYEDFQAAAAAdAAAAABAJ">
                    <img src = "https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fclinic&psig=AOvVaw26cSPNckfkOQ1j8NIdSAt-&ust=1694618021617000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKCo9rSupYEDFQAAAAAdAAAAABAO">
              </section>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Doctor Clinic</p>

    </footer>
</body>

"""

app.get('/info', response_class = HTMLResponse)
def get_list():
    return """
    <h1>
        This is a page of info
    </h1>
    <h2>
        You find a info into this page for a doctor services
    </h2>
    """


