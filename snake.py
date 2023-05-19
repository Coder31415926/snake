
import time
import random
import pygame


pygame.init()



def show_sc(color, font, size,score,window):

	
	font = pygame.font.SysFont(font, size)
	

	surface = font.render(f'Score : {score} Level: {score // 50}', True, color)
	
	rect = surface.get_rect()
	
	# displaying text
	window.blit(surface, rect)

def game_over(color, font, size,score,window):

	
	font = pygame.font.SysFont(font, size)
	

	surface = font.render(f'GAME OVER\nScore : {score}\nPress any button to exit', True, color)
	
	rect = surface.get_rect()
	
	# displaying text
	window.blit(surface, rect)


def main():
    #Define a bunch of vars used
    score_font = pygame.font.SysFont("times new roman", 100)
    playing = True

    window_x = 1000
    window_y = 1000
    frame_rate = pygame.time.Clock()

    score = 0
    snake_pos = [500,500]
    snake_segs = [[500,500],[480,500],[460,500]]

    window = pygame.display.set_mode((window_x,window_y))

    snake_speed_factor = 1

    fruit_pos = [random.randrange(10, (window_x) + 10),random.randrange(10, (window_y) + 10)]
   
    direction = "r"
    next_dir = ""

    while playing:

        for event in pygame.event.get():
            #Register the key presses and save their direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    next_dir = "u"
                if event.key == pygame.K_DOWN:
                    next_dir = "d"
                if event.key == pygame.K_LEFT:
                    next_dir = "l"
                if event.key == pygame.K_RIGHT:
                    next_dir = "r"

        #Prevent turning directly into yourself 
        #This technically makes the game easier but it is kinda annoying
        #To fat finger the keyboard and die
        if next_dir == "u" and direction != "d":
            direction = "u"
        if next_dir == "d" and direction != "u":
            direction = "d"
        if next_dir == "l" and direction != "r":
            direction = "l"
        if next_dir == "r" and direction != "l":
            direction = "r"

        #Update the location of the snake

        if direction == "u":
            snake_pos[1] -= 10 #* snake_speed_factor
        if direction == "d":
            snake_pos[1] += 10 #* snake_speed_factor
        if direction == "l":
            snake_pos[0] -= 10 #* snake_speed_factor
        if direction == "r":
            snake_pos[0] += 10 #* snake_speed_factor

        if snake_pos[0] > window_x:
            snake_pos[0] = 0
        if snake_pos[1] > window_y:
            snake_pos[1] = 0
        if snake_pos[0] < 0:
            snake_pos[0] = window_x
        if snake_pos[1] < 0:
            snake_pos[1] = window_y
            

        #To move the snake add the current position (post direction update)
        #As a new body part and remove the last body part
        #If eating a fruit in the same tick dont remove the part
        #Increasing the length of the snake
        snake_segs.insert(0, list(snake_pos))
        if abs(snake_pos[0]-fruit_pos[0]) < 10 and abs(snake_pos[1]-fruit_pos[1]) < 10 :
            score += 10
            snake_speed_factor += 0.2
            fruit_pos = [random.randrange(10, (window_x)),random.randrange(10, window_y)]
        else:
            snake_segs.pop()
        

        #Drawing snake and fruit
        window.fill(pygame.Color(0,0,0))
        for seg in snake_segs:
            print(seg[0],seg[1])
            pygame.draw.rect(window, pygame.Color(0,0,255), pygame.Rect(seg[0],seg[1],10,10))
        
        pygame.draw.rect(window,pygame.Color(255,0,0), pygame.Rect(fruit_pos[0],fruit_pos[1],10,10))
        
        frame_rate.tick(int(snake_speed_factor)*10)
        

        #Show score
        show_sc(pygame.Color(255,255,255), 'times new roman', 20,score,window)  

        pygame.display.update()
        #Collision checks
        for seg in snake_segs[1:]:
            if snake_pos == seg:
                playing = False
    
    #you lost, unlucky
    exit = True
    while exit:
        window.fill(pygame.Color(0,0,0))
        game_over(pygame.Color(255,255,255), 'times new roman', 20,score,window)
        
        pygame.display.update()

        #Prevents instantly exiting by mistake
        time.sleep(1)
        for event in pygame.event.get():
            #Register the key presses and save their direction
            if event.type == pygame.KEYDOWN:
                exit = False



if __name__=="__main__":
    main()