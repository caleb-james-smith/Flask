# Flask

A demo repo for learning Flask.

## References

- Flask tutorial from Tutorials Point [here](https://www.tutorialspoint.com/flask/index.htm)
- Flask tutorial from Pallets Projects [here](https://flask.palletsprojects.com/en/2.2.x/)
- Flask tutorial from Digital Ocean [here](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
- Info on python virtual environments [here](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html)
- HTTP Status Messages [here](https://www.w3schools.com/tags/ref_httpmessages.asp)

## Setup

Install virtualenv:
```
pip install virtualenv
```

Create a python virtual environment:
```
virtualenv venv
```

To activate a virtual environment:
```
source venv/bin/activate
```

To deactivate a virtual environment:
```
deactivate
```

Install Flask in the virtual environment:

```
source venv/bin/activate
pip install Flask
```

Run hello.py:
```
python python/hello.py
```

## Monitoring page

Open two terminals (two terminal windows or tabs).
In both terminals, go to the project directory for this repository and activate the python virtual environment:
```
cd <path_to_project>
source venv/bin/activate
```
In one terminal, run the monitor application to start the server:
```
python python/monitor.py
```
Then, in the other terminal, run this script to write data to a json file.
This script can write data once or continually with a time delay.
```
python python/write_data.py
```

Now, in a browser, load the monitoring page at http://127.0.0.1:5000/monitor.
If everything works, you should see an example monitoring page!
Refresh the page and check if the data has changed.
The data should update (with a fixed time delay) if the `write_data.py` script is set to run continually. 

When you are done, you can stop both scripts with `Ctrl-c`.
The monitoring page will not update with new values if `python python/write_data.py` is not running.  
The monitoring page will not load if `python python/monitor.py` is not running.  


