from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

# Create the main FastAPI app
app = FastAPI(title="Nomadiq Server", description="This is a simple FastAPI server", version="1.0")

# Mount static files
app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")

# Create a router to define your API routes
router = APIRouter()

# Define route functions using the router
@router.get("/", response_class=HTMLResponse)
async def root():
    """
    The root endpoint, which just returns simple HTML with Firebase authentication
    ---
    responses:
      '200':
        description: OK. 
    """
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nomadiq</title>
    <!-- Material Design Theming -->
    <script src="https://www.gstatic.com/firebasejs/ui/6.0.2/firebase-ui-auth__en.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <link type="text/css" rel="stylesheet" href="https://www.gstatic.com/firebasejs/ui/6.0.2/firebase-ui-auth.css" />
  
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link href="https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp" rel="stylesheet">
    <link rel="stylesheet" href="/css/nomadiq-styles.css">
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    
    <!-- Firebase App (the core Firebase SDK) -->
    <script src="https://www.gstatic.com/firebasejs/7.18/firebase-app.js"></script>
    <!-- Add Firebase Auth service-->
    <script src="https://www.gstatic.com/firebasejs/7.18/firebase-auth.js"></script>
    <!-- Firebase Implementation -->
    <script type="text/javascript" src="/js/login-page.js"></script>
    
</head>
<body>
    <!-- Nav Bar-->
    <nav class="navbar sticky">
      <div>
        &nbsp;
        <a class="logo-nav" href="/">nomadiq</a>
        &nbsp;
        <button class="btn btn-lg btn-outline-success" type="button" disabled data-bs-toggle="button" autocomplete="off"><a href="explore.html" class="disabled" tabindex="-1"role="button" aria-disabled="true" data-bs-toggle="button">Explore</a></button>
        &nbsp;
        <button class="btn btn-lg btn-outline-success" type="button"><a href="./about">About Us</a></button>
      </div>  
    </nav>
    <!-- </nav> -->
    <div class="container">
      <div class="row gx-5">
        <!-- left content col -->
        <div class="container-left text-center col">
          <h4 class="login">SIGN IN</h4>
          <p>Sign in to your account for full search capabilities</p>
          <!-- FirebaseUI Widget -->
          <div class="firebaseui-auth-container" id="firebaseui-auth-container"></div>
          <div class="firebaseui-auth-container" id="loader">Loading...</div>
        </div>
        <!-- right content col -->
        <div class="container-right text-center col">
          <h2 class="logo-large">nomadiq</h2>
          <!-- Google Material Icons -->
          <i class="material-icons-round">work</i>
          <i class="material-icons-round">wb_sunny</i>
          <i class="material-icons-round">flight</i>
          <i class="material-icons-round">laptop_mac</i>
        </div>
      </div>
    </div>
    <!-- Bootstrap Script -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
</body>
</html>
    """


# /search route
@router.get("/search", response_class=HTMLResponse)
async def search():
    """
    The search endpoint, which returns  simple HTML with Firebase JS because the actual search is happening in an iframe using Elastic and Streamline.
    ---
    responses:
      200:
        description: Returns
    """
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nomadiq</title>
    <!-- Material Design Theming -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
      
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link href="https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp" rel="stylesheet">
    <link rel="stylesheet" href="/css/nomadiq-styles.css">
    
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    
    <!-- Firebase App (the core Firebase SDK) -->
    <script src="https://www.gstatic.com/firebasejs/7.18/firebase-app.js"></script>
    <!-- Add Firebase Auth service-->
    <script src="https://www.gstatic.com/firebasejs/7.18/firebase-auth.js"></script>
    <!-- Firebase Implementation -->
    <script type="text/javascript" src="/js/search-page.js"></script>
    
</head>
<body>
    <!-- Nav Bar-->
    <nav class="navbar sticky">
      <div>
        &nbsp;
        <a class="logo-nav" href="/">nomadiq</a>
        &nbsp;
        <button class="btn btn-lg btn-outline-success" type="button" disabled data-bs-toggle="button" autocomplete="off"><a href="explore.html" class="disabled" tabindex="-1"role="button" aria-disabled="true" data-bs-toggle="button">Explore</a></button>
        &nbsp;
        <button class="btn btn-lg btn-outline-success" type="button"><a href="./about">About Us</a></button>
      </div>
      <div>
        <button class="btn btn-lg btn-outline-success" type="button" id="signInButton" onclick="toggle()">Sign Out</button>
        &nbsp; &nbsp;
      </div>
    </nav>
    <!-- </nav> -->
    <div class="container">
      <div class="container-search">
        <!-- Elastic GPT IFRAME -->
        <iframe style="border:none;" title="ElasticGPT" src="http://172.23.145.28:8501" class="iframe" scrolling="auto"></iframe>
      </div> 
    </div>
    <!-- Bootstrap Script -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
</body>
</html>
    """
    
# /about route
@router.get("/about", response_class=HTMLResponse)
async def about():
    """
    The about endpoint, which returns  simple HTML.
    ---
    responses:
      200:
        description: Returns
    """
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nomadiq</title>
    <!-- Material Design Theming -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
      
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <link href="https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp" rel="stylesheet">
    <link rel="stylesheet" href="/css/nomadiq-styles.css">
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    
    <!-- Firebase App (the core Firebase SDK) -->
    <script src="https://www.gstatic.com/firebasejs/7.18/firebase-app.js"></script>
    <!-- Add Firebase Auth service-->
    <script src="https://www.gstatic.com/firebasejs/7.18/firebase-auth.js"></script>
    <!-- Firebase Implementation -->
    <script type="text/javascript" src="/js/ext-page.js"></script>
    
</head>
<body>
    <!-- Nav Bar-->
    <nav class="navbar sticky">
      <div>
        &nbsp;
        <a class="logo-nav" href="/">nomadiq</a>
        &nbsp;
        <button class="btn btn-lg btn-outline-success" type="button" disabled data-bs-toggle="button" autocomplete="off"><a href="explore.html" class="disabled" tabindex="-1"role="button" aria-disabled="true" data-bs-toggle="button">Explore</a></button>
        &nbsp;
        <button class="btn btn-lg btn-outline-success" type="button"><a href="./about">About Us</a></button>
      </div>
      <div>
        <button class="btn btn-lg btn-outline-success" type="button" id="signButton" onclick="toggle()">Sign In</button>
        &nbsp; &nbsp;
      </div>
    </nav>
    <!-- </nav> -->
    <div class="container">
      <div class="container-search">
        
        <!-- Content -->
        
        <div class="container-text">
        
        <h4>About Nomadiq:<br>Your Gateway to Nomadic Living and International Adventure</h4>

        <p>Welcome to our online service, where we are committed to serving the global community of expats and nomadic travelers with comprehensive, up-to-date, and invaluable information to support your international journey. We are passionate about empowering you to embrace the spirit of adventure, discover new cultures, and create unforgettable memories across borders.</p>

        <h4>Our Mission</h4>

        <p>Our mission is to be your ultimate resource for international travel information, catering specifically to the needs of expatriates and nomadic souls. We understand that moving to a new country or continuously exploring different destinations can be both exciting and challenging. That's why we strive to provide accurate, reliable, and localized insights to help you make informed decisions during every step of your journey.</p>

        <h4>The Nomadic Traveler's Toolkit</h4>

        <p>At our core, we believe that knowledge is the key to unlocking the full potential of your adventures abroad. Our platform equips you with a comprehensive toolkit that covers essential aspects of your nomadic lifestyle, including:</p>

        <ol>
          <li> Cost of Living Comparisons: We understand that financial planning is vital for a successful and stress-free experience abroad. Our platform allows you to compare the cost of living between various cities and countries, helping you budget effectively and make choices that align with your lifestyle and preferences.

          <li> Medical Treatment Guidance: Your health is our priority. We provide essential information about medical facilities, health insurance options, and vaccination requirements in different countries, ensuring that you can access quality healthcare wherever your journey takes you.

          <li> Internet Service Availability: In the digital age, staying connected is crucial for remote workers, digital nomads, and expatriates. Our service provides insights into internet service availability and reliability in different locations, enabling you to choose destinations that cater to your online needs.

          <li> Local Culture and Etiquette: Understanding the customs and traditions of the countries you visit fosters respect and enriches your experiences. We offer cultural guides and etiquette tips to help you navigate unfamiliar territory with confidence and ease.

          <li> Legal and Visa Support: Visa regulations and legal requirements can be complex and vary greatly from one country to another. Our platform simplifies these complexities, providing you with clear information on visa processes and legal obligations, facilitating a smoother transition.
        </ol>
        
        <h4>Our Commitment to Quality</h4>

        <p>We take pride in delivering accurate and up-to-date information. Our team of dedicated researchers and travel experts scours reputable sources, collaborates with local experts, and keeps a vigilant eye on global trends to ensure the information we provide is reliable and relevant.</p>

        <h4>Community-Driven Engagement</h4>

        <p>We value the sense of community that emerges among travelers and expats. Our platform fosters a welcoming environment where users can share their experiences, exchange tips, and engage with like-minded individuals. Our community forums provide a platform for open discussions and the exchange of valuable insights that enhance your travel journey.</p>

        <h4>Privacy and Security</h4>

        <p>We understand the importance of your privacy and security while using our platform. We are committed to maintaining a secure environment and protecting your personal information. Our privacy policy ensures that your data remains confidential and is used only to enhance your user experience.</p>

        <h4>Let's Embark on this Journey Together</h4>

        <p>Whether you are a seasoned expat or a first-time nomad, we are here to accompany you on your global expedition. Our platform is designed to be your trusted companion, supporting you in making well-informed decisions and embracing the wonders of international living.</p>

        <p>Thank you for being part of our community. Let's explore the world together, one adventure at a time!</p>
        
        </div>
      </div> 
    </div>
    <!-- Bootstrap Script -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
</body>
</html>
    """

# Add the router 
app.include_router(router)

# Generate the Swagger UI HTML
def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API Docs")

@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_endpoint():
    return get_openapi(
        title="API Docs", version="1.0", routes=app.routes
    )

app.swagger_ui_html = custom_swagger_ui_html

# Add an endpoint to serve the OpenAPI schema
@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return app.openapi()

# Serve Swagger UI from "/docs"
@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API Docs")
