# what do you want to do bot

## prerequirement
 - python3
 - telegram
 - network
 - ngrok (如果使用本機作為伺服器)

## setup
    pip3 install requirement.txt
    pip3 install python-vlc

## execute
    ./ngrok http 5000
    python3 app.py

## purpose
常常放假的時候都不知道要做什麼，因此我做了這個聊天機器人，當你放假不知道要做什麼的時候，可以替你出主意

## fsm finite state machine
https://imgur.com/SPA5nMb

## usage
主要有三個項目:
1. **出去玩**
可以選擇要在近的地方玩或跑遠一點的地方
2. **在家**
可以選擇玩遊戲或睡覺，會有一個計時器倒數，*bot會回傳倒數時間*，時間到了bot會播音樂提醒
3. **什麼都不要做 耍廢**
像一個樹懶一樣，就待在那裏不要動，會播一個樹懶的影片


## state
1.state: user

	- input: ```"go to state1"```
		- response: ```"Hello~"``` 	
        *show image
        *go to state state1	
	
	- input: ```"go to state2"```
		- response: ```"I'm entering state2"``` 	
        *show fsm image*
        *go to state state1*		
	
	- input: ```"play outside"```
		- response: ```"Have a good time"```	
		*show image*
        *go to state play*		
	
	- input: ```"stay at home"```
		- response: ```"let's be a coach potato,play game or sleep?"```	
		*show image*
		*go to state stay*		
		
	- input: ```"just do nothing"```
		- response: ```"I'm lazy"```	
		*go to state donothing*
        *play a video*
		
2.state: play

	- input: ```"go far away"```
		- response: ```"go abroad or drive around island?"```
		*go to state far*		
		
	- input: ```"go to near place"```
		- response: ```"walk or drive,which one do you like"```	
		*go to state near*
		
3.state: far

	- input: ```"go abroad"```
		- response: ```"Let's book a ticket first"```
		*撥放廣播並傳圖片*
		*go to state abroad*		
		
	- input: ```"drive around island"```
		- response: ```"Let's go as soon as possible"```	
		*bot 回傳圖片*
        *go to state aroundisland*
	
4.state: near

	- input: ```"take a walk"```
		- response: ```"Let's take a walk"```
		*go to state walk*		
		
	- input: ```"i want to drive my car"```
		- response: ```"Here's your key,where do you want to go?"```		
		*go to state drive*
		
5.state: walk

	- input: ```"go to department store"```
		- response: ```"I'm entering department store"```
		*回傳圖片*
		*go to state departmentstore*	
		
	- input: ```"go to park"```
		- response: ```"Let's play on the swing"```		
		*回傳圖片*
		*go to state park*
		
6.state: drive

	- input: ```"go to kaohsiung"```
		- response: ```"Welcome to Kaohsiung"```
		*回傳圖片*
		*go to state kaohsiung*		
		
	- input: ```"go mountain climbing"```
		- response: ```"Let's start mountain climbing"```	
		*回傳圖片*		
		*go to state mountainclimbing*
	
7.state: stay

	- input: ```"play game"```
		- response: ```"I'm playing game"```
		*go to state game*
		*播旅遊大亨音樂，並讓server sleep十秒*	
		
	- input: ```"i just want to sleep"```
		- response: ```"I'm sleeping now"```
		*go to state sleep*		
		*讓server sleep五秒，時間到了以後播放起床歌*
		
	
8.back to user state
    **state1,state2,abroad,aroundisland,departmentstore,park,kaohsiung,mountainclimbing,play,sleep,donothing會自動回到user state**	
		
		
