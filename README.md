<a id="readme-top"></a>

<h1 align="center">Tech News</h3>

<!-- ABOUT THE PROJECT -->
## About The Project
This is the Back-end of a news website, which includes a web crawler that can crawl news from `zoomit.ir` website.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

* ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

* ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

* ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

* ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

* ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Prerequisites
 
 - Python

 - PostgreSQL

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/farzanmosayyebi/TechNews
   ```
2. Navigate to `src` directory

   ```sh
   cd src
   ```
3. Install the requirements

   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations
   
   **Note**: First, You will need to create the PostgreSQL database and set the environment variables in a file named `.env` with the following format in `src` directory:

   
   
   `TechNews/src/.env`:
   ```
   SECRET_KEY=your-secret-key
   DB_NAME=your-db-name
   DB_USER=your-db-user
   DB_PASSWORD=your-db-password
   DB_HOST=your-db-host
   DB_PORT=your-db-port
   ```

   Then run 

   ```sh
   python manage.py migrate
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

- To start the project, in `src` directory run

   ```sh
   python manage.py runserver
   ```

    - Url to see the Swagger UI

   ```
   127.0.0.1:8000/swagger/
   ```

### Running the tests
- In `src` directory run

    * Windows
    ```sh
    python manage.py test ..\tests
    ```

    * Linux/MacOS
    ```sh
    python manage.py test ../tests
    ```
 
### Running the crawler
- In `src` directory, run

   ```sh
   python manage.py crawl --limit <number-of-items-to-scrape>
   ```

    - This is a custom django `Command` which crawls the specified number of items from `zoomit.ir` website. The default number is 500.

    #### Example
    - To crawl 50 items

    ```sh
    python manage.py crawl --limit 50
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

- Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
