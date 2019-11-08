#!/usr/bin/env checkio --domain=py run open-labyrinth
def checkio(maze,y=1,x=1,hard_path=' '):
    soft_path=hard_path

	if x==10 and y==10:
		return soft_path.lstrip()

	maze[y][x]=1
	if maze[y][x+1]==0:
		soft_path=checkio(maze,y,x+1,hard_path+'E')
		if soft_path!='Dead':
			return soft_path
	if maze[y+1][x]==0:
		soft_path=checkio(maze,y+1,x,hard_path+'S')
		if soft_path!='Dead':
			return soft_path
	if maze[y][x-1]==0:
		soft_path=checkio(maze,y,x-1,hard_path+'W')
		if soft_path!='Dead':
			return soft_path
	if maze[y-1][x]==0:
		soft_path=checkio(maze,y-1,x,hard_path+'N')
		if soft_path!='Dead':
			return soft_path
	return 'Dead'
