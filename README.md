# Volleyball Sorting

The volleyball sorting algorithm separates two teams of players based on the
team score. This score is given by the sum of each player's score. The idea is
to minimize the difference in score between the two teams.

The score is defined by weighted sum of three categories: technical ability, 
physical ability, and the desire to play volleyball (yes, unfortunately, this is
a category that sometimes has to be included).

The list of players will be passed as a CSV file. You can use the CSV files in
`data` for the formatting.

## How to Use

Run

```
python3 main.py
```

to run with the example file. To run with your own file of players, run

```
python3 main.py --filename=path/to/file
```

It must be a CSV file. To change the number of shuffles (to 100, for example)
you want to perform to the roster, run

```
python3 main.py --shuffles=100
```

