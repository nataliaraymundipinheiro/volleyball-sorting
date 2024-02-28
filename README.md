# Volleyball Sorting

## Project Overview


The Volleyball Sorting algorithm is designed to create balanced teams for
volleyball games by minimizing the difference in overall team grades. This
innovative approach takes into account each player's technical and physical
abilities, as well as their desire to play, to ensure fair and competitive
matches.

The algorithm processes a list of players provided in a CSV file, utilizing a
weighted sum of three categories: technical ability, physical ability, and the
desire to play volleyball. Our goal is to enhance the sports experience by
ensuring each game is as enjoyable and fair as possible.


## Installation

Before you can run the Volleyball Sorting algorithm, you'll need to have Python
3 installed on your system. If you don't have Python 3, you can download it from
 the official website at [https://www.python.org/downloads/](https://www.python.org/downloads/).

Once Python is set up, clone this repository to your local machine:

```
git clone https://github.com/nataliaraymundipinheiro/volleyball-sorting
```

### Install Required Libraries

This project requires NumPy for numerical computations. To install NumPy, run
the following command:

```
pip3 install numpy
```

Ensure that all dependencies are installed before proceeding to use the
Volleyball Sorting algorithm.


## How to Use

### Running with the Example File

To run the Volleyball Sorting algorithm with the provided example CSV file in
the `data` directory, simply execute:

```
python3 main.py
```

### Using Your Own Player File

To use your own file of players, ensure it's in CSV format according to the
examples in `data` and run:

```
python3 main.py --filename=path/to/your/file
```

### Customizing Number of Shuffles

The algorithm supports shuffling the roster to explore different team
combinations. To change the default number of shuffles (to 100, for example),
use:

```
python3 main.py --shuffles=100
```

## Contributing

We welcome contributions to the Volleyball Sorting project. Whether you're
looking to fix bugs, add new features, or improve documentation, please feel
free to make a pull request.