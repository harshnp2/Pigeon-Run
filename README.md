# Pigeon-Run
A game where you can learn American Sign Language and have fun while doing it.

## Inspiration
After the theme was announced I knew I wanted to create a project that would make the gaming industry more of an inclusive community. That was when the idea of creating game centered around ASL struck me. This game concept has the potential to make a real difference in the lives of people who are deaf or hard of hearing. By creating a fun and engaging way for players to learn ASL, you are empowering them to communicate more effectively and breaking down the barriers that often exist between the hearing and deaf communities

## What it does
Pigeon run is a game similar to Subway Surfers in the way that involves moving to dodge obstacles. You are a airplane and your goal is to dodge the pigeons in order to get points. If you hit the pigeon you lose However, unlike Subway Surfers to move your character up or down you have to sign a certain letter from ASL in order to move up or down. The game is able to detect which letter you are signing by using your computer's camera. As the game continues the number of pigeons increases from 1 to 2, and the speed that pigeon's are moving also increases decreasing the time you have to sign a specific letter. 

## How we built it
The game aspect of the project was built using Pygame and to detect the ASL letter that player is trying to do, that aspect was built using OpenCV and Roboflow.

## Challenges we ran into
Challenges that I ran into were I was having trouble making both the game aspect and the ASL recognition aspect to work together. Since I couldn't run another window alongside the pygame window, even if I used threads, that setup many obstacles. As a result I had to change parts of the layout of my game in order for both the game aspect and the ASL recognition aspect to work together. 

## Accomplishments that we're proud of
Accomplishments that I'm proud of are being able to make a functioning game using Pygame as I haven't worked with it before this hackathon. Furthermore, being able to make the game aspect and ASL recognition of my project to work together is something that I'm very proud of.

## What we learned
I learned how to use Pygame and to incorporate it with computer vision. 

## What's next for Pigeon Run
To make Pigeon Run even better, instead of just recognizing letters I can train and test a larger dataset with images for words as well so that players can practice more than just the ASL alphabet.
