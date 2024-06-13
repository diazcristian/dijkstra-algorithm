# Dijkstra-algorithm

This project implements Dijkstra's algorithm to find the shortest path between two municipalities represented by an adjacency matrix.

## Description

The program receives as parameters the number of the origin and destination city, as well as the file containing the adjacency matrix. The graph is represented by a bidimensional matrix where each cell `graph[i][j]` represents the distance from municipality `i` to municipality `j`.

## Usage

To run the program:

```sh
python3 dijkstra.py <start> <goal> <filename>
