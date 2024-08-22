<a id="readme-top"></a>

<h1 align="center">Tech News</h3>

<!-- ABOUT THE PROJECT -->
## About The Project
This is the Back-end of a news website, which includes a web crawler that can crawl news from `zoomit.ir` website.
- The project is accessible through the links below:
   - [Deployed website (API)](https://fartechnews.darkube.app/news)
   - [Celery Flower](https://fartechnews-monitor.darkube.app/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

* ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

* ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

* ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

* ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

* ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

* ![Scrapy Badge](https://img.shields.io/badge/Scrapy-60A839?logo=scrapy&logoColor=fff&style=for-the-badge)

* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

* ![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)

* ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
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

### Running with docker compose

1. In root directory of the project, run:

   ```sh
   docker compose up
   ```
   **Note**: You need to provide a file named `app.env` (using `--env-file`) that contains the environment variables for the project. \
   \
   **About Dockerfiles:**
      - Two dockerfiles are implemented :
         - **Dockerfile.base**: Which is the base file that only installs dependencies. Backend, celery-beat and celery-flower containers will be run upon the image built from this file.
         - **Dockerfile.worker**: This file also installs Google Chrome and needed packages in order to be able to run selenium in celery workers. Celery-worker container will be run upon the image built from this file.
         
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Crawler schedule
   At startup, 500 news will be crawled from `zoomit.ir`. After that, celery beat is scheduled to push crawl tasks to message queue daily at midnight. which means everyday at midnight, 60 news items will be crawled from `zoomit.ir`.

<!-- LICENSE -->
## License

- Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
