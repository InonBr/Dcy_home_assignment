# Dcy Home Assignment Flask

## Run App Locally
1. In order to run the app locally, enter the base directory and activate create a virtual environment by using this command: `python3 -m venv venv`.
2. Now, activate the virtual environment using `. venv/bin/activate`.
3. You need to install all the requirements from the file `requirements.txt`, using this command:  `pip3 install -r ./requirements.txt`.
4. In the email I've sent you, you can find a `.env` file, please place it in the root directory of the app.
5. In order to connect **MySQL database** using **docker-compose**, please run `docker-compose up --build -d`.
6. You need to run the migrations in order to use the models that I've created, please run:
   1. `flask db init`
   2. `flask db migrate`
   3. `flask db upgrade`
7. You can run the server locally on port **5000**, using `python3 app.py`.
8. In the email I've sent you, you can find a file called `flask.postman_collection.json`, please import it into **Postman** in order to test the app. 
   1. You will first have to use the `signup` route in order to have a **JWT token**.
   2. For protected routes, please make sure to provide the **JWT token** as an `Authorization` header. 

