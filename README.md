Contributors:
- [Vanshpreet Singh Kohli](https://github.com/VKohli17)
- [Shashwat Singh](https://github.com/shashwat1002)

\* *Created by the aforementioned authors for a course project for Language and Society, IIITH, Fall 2021* \*

The final project report is attached as `report.pdf` in the repository.

It is recommended that before running any of the code files in the project, a python virtual environment is created.

Assuming you have python installed, 

run `python3 -m venv env` to create a virtual environment in the current directory. 

and the run `source env/bin/activate` to activate the virtual environment 

To install all the dependencies, in the home directory run the following on the command line (ideally with a virtual environment created):

```
pip install -r requirements.txt
```

the virtual environment will be around 140 MB after installation of all dependencies 

## Files and directories

### `fetch_data.py`

This file uses tweepy to fetch relevant data

For the code in this file to work properly, there must a exist a file in the home directory with the name of `api_keys.txt`.

The `api_keys.txt` must have the following information in the following order 

- consumer key
- consumer key secret
- access key 
- access key secret
- dev environment (which has to be set up for full API access)

Note: the `api_keys.txt` we used hasn't been uploaded in the repository (and is not in the submission) for safety reasons. Therefore the `fetch_data.py` won't run as-is

`fetch_data.py` prompts to ask which years you want the data for, and runs the query for `bhakt` for those years. 

A file corresponding to each year will be generated in the `data/` directory. 

### `data/`

as mentioned above, all the data fetched directly from twitter is generated and stored in this directory

### `annotated/`

All the data files we manually annotated are stored here.

### `analysis.py`

The graph used for analysis is generated in this file. 

It takes relevant files from the `annotated/` to generate the graph 

### `output.png`

This is the graph that was used in the report

