# **US Bikeshare Data Analysis**

This project started as an assesment for for the **Udacity Data Analysis Professional Track**.

Data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States.
Randomly selected data for the first six months of 2017 are provided for three major cities in the US:

- Chicago
- New York City
- Washington, DC

The goal is to build an interactive application where the user can choose the input data between three different cities: Chicago, New York City and Washington.

The user can then choose whether to filter the data by month or weekday, both or no filtering at all.
Then the Following Statistics are being evaluated:

1. The most frequent time of travel:
   - The most common month.
   - The most common day of the week.
   - The most common hour.
2. The most popular station and trip:
   - The most common start station.
   - Teh most common end station.
   - The most common combination of start and end stations.
3. The trip duration:
   - The total time traveled.
   - The mean travel time.
4. The User Data:
   - The user type(Subscriber, Customer, etc.).
   - The user gender information (Male or Female).
   - The user age information (eldest, youngest and the most common age).

To run the main program:

```Bash
python bikeshare.py
```

an additional jupyter notebook `bikeshare.ipynb` was used for testing and exploration of data.

## Challenges

In some cities some columns are totally missing like the Gender and Birth Year columns in the data for Washington. Also, the data contained a lot of missing data. So, the code is full of try/except blocks to handle such errors or missing data without crashing hte program.

The first challenge was converting the Start Time column from string to datetime object from which we could extract the month, weekday and hour.this was easily achieved with pandas function `pd.to_datetime(df['Start Time'])`.

To find the most common route the Start Station and End Station columns where combined into one column to be able to analyze the data much easier as follows:  

```Python
df['routes'] = 'from "' + df['Start Station'] + \ '" to "' + df['End Station'] + '"'
```

Formating the datetime objects to display it to the user was done using `time.gmtime` and `time.strftime` functions.

## Languages used

- [Python](https://www.python.org) (3.8 or above recommended)

## Requirements

- [NumPy](https://numpy.org/) (1.18 or above recommended)
- [Panadas](https://pandas.pydata.org/) (1.4 or above recommended)

if you don't have the requirements you can install them using [pip](https://pypi.org/project/pip/):

```Bash
pip install -r requirements.txt
```

if you are using conda use the command below instead:

```Bash
conda env create -f environment.yaml
```

## Recommended Tools

- [VScode](https://code.visualstudio.com/)
- [Jupyter Notebooks](https://jupyter.org/)
- [Anaconda](https://www.anaconda.com/)

## References

- [Pandas Datetime: Extract year, month, day, hour, minute, second and weekday from unidentified flying object (UFO) reporting date](https://www.w3resource.com/python-exercises/pandas/datetime/pandas-datetime-exercise-8.php)
- [Weekday name from a pandas dataframe Date object](https://stackoverflow.com/questions/60339049/weekday-name-from-a-pandas-dataframe-date-object)
- [Python | Working with date and time using Pandas](https://www.geeksforgeeks.org/python-working-with-date-and-time-using-pandas/)
