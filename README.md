# FlightsManager 💡
 
## run project in virtual environment 🚀

- Create virtual env:

```bash
        python -m virtualenv <folder_name>
```

- Create virtual environment version depend:

```bash
        virtualenv <folder_name> --python=python3.9
```

- activate

```bash
  .\<folder_name>\Scripts\activate.bat
```

- ctrl + shift + p: Python: Select interpreter
  should include Python interpreter related to your environment
- refresh terminal
- install requirements:
  There exist two requirements files one for production and one for development.

```bash
        pip install -r requirements.txt
```

- deactivate:

```bash
        deactivate
```

# requirements:
- No more than 20 success can exist in the airport during the day. 
- Success for a flight is if no more than 20 success happens in a day and the difference between the
arrival and departure is greater or equal than 180 minutes
- If there is no success put ‘fail’ in the success column either wise ‘success’
- Flights should be sorted by arrival time.

1) Pls write down
Python (JAVA OR C# also can be acceptable) code that produce the success column

2)Write 2 rest API
GET - to get info about a flight
POST - update the csv file with flights as an input

# Answer:
main.py file include two endpoints with requested API
flight_manager -> update_flight_info() include Python code that produce success column launched by flight_manager.py 
