	              Spotify Discover Weekly Automation
--------------------------------------------------------------------------------
Description: 
	    Have you ever gave the Discover weekly playlist on spotify a listen? 
	    Have you ever listened to a song you really liked from that playlist 
	    but you forgot to save it for later?

	    This is the problem I also faced so I decided to fix my problem 
            using my Python knowledge.

	    I decided to use Spotify's very own Web API which can be found
	    here (https://developer.spotify.com/documentation/web-api/).

	    	                 Program functionality
            --------------------------------------------------------------------
            This program will go into Spoifiy's Discover Weekly playlist, pull 
            all the songs and will automatically create a new playlist with 
            those songs of that week. 
 
            Spotify's Discover Weekly playlist changes every week so this 
            program will run every Monday and it will create a new playlist with 
            the songs of that week and will have the date the playlist was 
            created as the title.

    	                    How to make it run every Monday
            --------------------------------------------------------------------
            1. Go to your Task Scheduler
            2. Create a Task
            3. Name the task
            4. Go to Triggers
            5. Press New
            6. Press weekly then change the date to every Monday
            7. Go to Actions
            8. Press New
            9. Next to Action change it to "Start a program"
           10. Now under Program/script we need to find the directory of python
                	 - Go to powershell
                         - Enter: import sys
                                      sys.executable
                         - That will print out the directory so copy it
           11. Paste the directory under "Program/script"
           12. In "Add arguments" type "main.py"
           13. In "Start in" You want to type in the directory where the main.py 
                file is stored
           14. Then press OK and you're all set it will run every week
          
            
            
	     		

		