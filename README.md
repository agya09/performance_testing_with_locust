# Performance testing using Locust

Performance testing shows how quickly a site loads in a web browser and the quality of the website's interaction, reliability, and usability.


# Installation 

1. Clone the repository 
```
git clone git@github.com:agya09/performance_testing_with_locust.git
```
2. Move to the projects' root directory:
```
cd PerformanceTesting
```
3. Create and activate virtual environment. <br>
For Linux/MacOS

```
python3 -m venv venv
source venv/bin/activate
```

For Windows
```
python -m venv venv
venv\Scripts\activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

# Test execution

Firstly, generate a csv file including all the urls present in the provided page's url. Run the command below:

```
python get_links.py
```

This command will scrape the web page and save all urls present in href tag to <b> Data/urls.csv </b> file.

Now, run the command below in your terminal to perform performance test:
```
locust -f locustfile.py 
```
As an output, you will see a locust server starting at  http://0.0.0.0:8089. Open it in your browser and send request as per your requirement.

