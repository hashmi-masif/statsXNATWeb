
# statsXNAT Web

statsXNATWeb is a integration of statsXNAT with a website. This website gives the user an overview of the data present at XNAT servers in a graphical form. statsXNAT uses pyXNAT to connect to the XNAT servers using RESTful Web services provided by XNAT.


## Dependencies

 - [pyXNAT](https://pyxnat.github.io/pyxnat/index.html) 
 - [Flask](https://palletsprojects.com/p/flask/)
 - [Pytest](https://docs.pytest.org/en/latest/)
 - [Chart.js](https://www.chartjs.org/)

# Devlopment

## Getting Started 
- Installing the required dependencies type ```pip3 install -r requirements.txt``` 
- Starting the server type ``` python3 app.py``` 
- Testing ``` pytest tests/ ```

## File Structure  
![File Structure](https://github.com/Udolf15/statsXNATWeb/blob/master/images/fileStruct.jpg)