# douglas the self driving go-kart
My high school gives seniors the option to undergo a large project instead of taking classes for the last month of school. I had the idea to outfit a go-kart with self-driving functionality and roped some friends in to build it with me. We started with a bare-bones gas powered go-kart and added motors so we could programmatically  control the steering, accelerating, and breaking. Then, we outfitted the kart with a camera and software to view street lines and hooked everything up to a Raspberry Pi 3. In the end, we had somewhat promising results but lacked any time to polish the steering algorithm.

track_lines.py contains the main Raspberry Pi loop. The loop analyzes the incoming video feed and steers according to the difference between the angle of the detected lines and 90/270 degrees. This primitive steering algorithm simply assumes that we want to move parallel to the street lines to be successful. The breaking is done off of an OS interrupt, and the entire program would benefit off of some multi-threading so we can think faster than the Raspberry Pi takes video frames. 

The other relevant files are wrappers around the output motors. The APIs are meant to make each motor easy to test in an interactive session and also easy to hook into for the real execution.

I destroyed too many boards doing this project...
