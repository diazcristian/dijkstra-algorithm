# Dijkstra-algorithm

This project implements Dijkstra's algorithm to find the shortest path between two municipalities represented by an adjacency matrix.

## Description

The program receives as parameters the number of the origin and destination city, as well as the file containing the adjacency matrix. The graph is represented by a bidimensional matrix where each cell `graph[i][j]` represents the distance from municipality `i` to municipality `j`.

## Requirements

- Python 3.x
- Pandas

## Installation

1. Clone this repository to your local machine:

    ```sh
    git clone https://github.com/yourusername/dijkstra-project.git
    cd dijkstra-project
    ```

2. Install the required dependencies:

    ```sh
    pip install pandas
    ```

## Usage

To run the program, use the following command in the terminal:

```sh
python3 dijkstra.py <start> <goal> <filename>
