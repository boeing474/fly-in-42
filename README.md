*This project has been created as part of the 42 curriculum by pboeing-.*

# Fly-in

## Description
Fly-in is an algorithmic simulation project designed to route a fleet of autonomous drones through a complex, dynamic network of connected zones. The primary objective is to move all drones from a central starting hub to a target destination in the fewest possible simulation turns. The project strictly enforces capacity limits, movement constraints, and zone priority rules, fully implemented in object-oriented Python.

## Instructions
To set up and run the simulation, use the provided Makefile:

1. **Install dependencies**:
    make install

2. **Run the simulation** (uses the default easy map):
    make run

3. **Run a specific map**:
    python3 main.py maps/hard/01_maze_nightmare.txt

4. **Run Linting & Type Checking** (Flake8 & Mypy):
    make lint

## Algorithm Strategy
The core pathfinding relies on a graph traversal algorithm adapted from Dijkstra's principles, optimized for maximum throughput. Because multiple drones move simultaneously, the algorithm calculates overlapping and disjoint paths. It manages "strategic waiting" when a connection or zone reaches its `max_drones` or `max_link_capacity` limits. It meticulously schedules turn-by-turn movements to prevent deadlocks and collisions while prioritizing paths that contain `priority` zones and calculating the delayed arrival for `restricted` zones.

## Visual Representation
The simulation provides a colored terminal output to track drone movements and zone states turn-by-turn. This visual representation enhances the user experience by making it easy to track parallel drone movements and quickly identify bottlenecks or capacity limitations within the graph without relying on external graphical dependencies.

## Example
**Input (Map Snippet):**
    nb_drones: 2
    start_hub: hub 0 0 [color=green]
    end_hub: goal 10 10 [color=yellow]
    hub: roof1 3 4 [zone=normal color=blue]
    connection: hub-roof1
    connection: roof1-goal

**Expected Output:**
    --- Simulation Output ---
    D1-roof1
    D1-goal D2-roof1
    D2-goal

## Resources
* **Graph Theory & Pathfinding**: General concepts based on Dijkstra's Algorithm and Network Flow configurations.
* **AI Usage**: Artificial Intelligence was utilized strictly as a learning assistant to help format this README according to the subject's standards, to resolve flake8 spacing violations (PEP 8), and to generate type hints for mypy strict compliance. The core mathematical logic, object-oriented architecture, and algorithmic implementation were manually studied and structured.