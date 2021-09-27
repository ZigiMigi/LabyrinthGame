# LabyrinthGame
## About
This game will test your intuition in a given maze. Server creates a maze with a random size (etc. 100x100, 30x30, ...), and gives it to all clients/players. 
Clients/players get the maze and solve it as quickly as possible and return their time to the server, which shows the scoreboard.
This is my first ever big project that I am working on alone. Project started in July 2021.

## Features
- Server site generates a random maze that is created with the Random Prim Algorithm. (*Maze's always have solutions)

- Maze 40x40
  ![image](https://user-images.githubusercontent.com/82703447/134900590-375f23a6-186c-4b57-ba96-d529cb9c0ccf.png)
  
- Maze 100x100  
  ![image](https://user-images.githubusercontent.com/82703447/134900813-08222348-e5bc-4d1c-aee0-93c2bfc9489d.png)
  
- My project also includes a MazeSolver (if a player gives up on a maze or just wants to see how a solution looks he may use a function that will show draw him a solution). The function uses the BFS method to find the end.
  ![image](https://user-images.githubusercontent.com/82703447/134901514-3293a0ad-7a12-40e7-8372-9aaefdf170fd.png)
  
- Demonstration of the Maze Solver:



https://user-images.githubusercontent.com/82703447/134904953-5d2967ab-03d2-41d9-914b-0feafb927ef0.mp4



## TBD
- Server's site that shows the scoreboard
- Server sending mazes over the network (currently server writes the maze in a .txt file and clients read it from that file localy)

