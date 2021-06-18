Using pillow to draw maze and create a gif: https://pypi.org/project/Pillow/

# BFS:
How to run:
In the same directory, run the following command: 
	`python .\Bfs-A-Star-Search.py x_start_coord y_start_coord x_treasure_coord y_treasure_coord`
	Ex: ` python .\Bfs-A-Star-Search.py 13 2 5 23`
	
Sample gif output:

![bfs-maze](https://user-images.githubusercontent.com/33491921/122524925-b3266e00-cfe6-11eb-929b-d11d31c0a154.gif)

# DFS:
How to run:
In the same directory, run the following command: 
	`python .\DfsMaze.py x_start_coord y_start_coord x_treasure_coord y_treasure_coord`
	Ex: ` python .\DfsMaze.py 13 2 5 23`
	
Sample gif output:

![dfs-maze](https://user-images.githubusercontent.com/33491921/122524662-680c5b00-cfe6-11eb-86ba-cfbf9ee49b46.gif)


# A* Search:
How to run:
In the same directory, run the following command (note that there is an 'a' at the end to enable A* Search): 
	`python .\Bfs-A-Star-Search.py x_start_coord y_start_coord x_treasure_coord y_treasure_coord a`
	Ex: ` python .\Bfs-A-Star-Search.py 13 2 5 23 a`
	
Sample gif output:

![a_star_search](https://user-images.githubusercontent.com/33491921/122524999-c5a0a780-cfe6-11eb-86b4-cba2e865a810.gif)

They will all output separate gif file and print statements for more stats.
