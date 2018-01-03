from transitions.extensions import GraphMachine

import time
import vlc

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'

    def is_going_to_play(self, update):
        text = update.message.text
        return text.lower() == 'play outside'
    
    def is_going_to_stay(self, update):
        text = update.message.text
        return text.lower() == 'stay at home'
    
    def is_going_to_donothing(self, update):
        text = update.message.text
        return text.lower() == 'just do nothing'
    
    def is_going_to_far(self, update):
        text = update.message.text
        return text.lower() == 'go far away'
    
    def is_going_to_near(self, update):
        text = update.message.text
        return text.lower() == 'go to near place'
    
    def is_going_to_abroad(self, update):
        text = update.message.text
        return text.lower() == 'go abroad'
    
    def is_going_to_aroundisland(self, update):
        text = update.message.text
        return text.lower() == 'drive around island'
    
    def is_going_to_walk(self, update):
        text = update.message.text
        return text.lower() == 'take a walk'
    
    def is_going_to_departmentstore(self, update):
        text = update.message.text
        return text.lower() == 'go to department store'
    
    def is_going_to_park(self, update):
        text = update.message.text
        return text.lower() == 'go to park'
    
    def is_going_to_drive(self, update):
        text = update.message.text
        return text.lower() == 'i want to drive my car'
    
    def is_going_to_Kaohsiung(self, update):
        text = update.message.text
        return text.lower() == 'go to kaohsiung'
    
    def is_going_to_mountainclimbing(self, update):
        text = update.message.text
        return text.lower() == 'go mountain climbing'
    
    def is_going_to_game(self, update):
        text = update.message.text
        return text.lower() == 'play game'
    
    def is_going_to_sleep(self, update):
        text = update.message.text
        return text.lower() == 'i just want to sleep'
    
    def on_enter_state1(self, update):
        update.message.reply_text("Hello~")
        update.message.reply_photo("https://gadgetflowcdn.com/wp-content/uploads/2015/07/BUDDY-06.jpg")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("I'm entering state2")
        update.message.reply_photo(open("img/show-fsm.png","rb"));
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
    
    def on_enter_play(self, update):
        update.message.reply_text("Have a good time")
        update.message.reply_photo(open("img/play.jpg","rb"));

    def on_enter_stay(self, update):
        update.message.reply_text("let's be coach potato,play game or sleep?")
        update.message.reply_photo(open("img/stay.jpg","rb"));

    def on_enter_donothing(self, update):
        update.message.reply_text("I'm lazy")
        instance=vlc.Instance()
        player=instance.media_player_new()
        media=instance.media_new_path('img/lazy.avi')
        player.set_media(media)
        player.play()

        self.go_back(update)
    
    def on_exit_donothing(self, update):
        print("do everything hard")

    def on_enter_far(self, update):
        update.message.reply_text("go abroad or drive around island?")

    def on_enter_near(self, update):
        update.message.reply_text("walk or drive,which one do you like")

    def on_enter_abroad(self, update):
        update.message.reply_text("Let's book a ticket first")
        
        instance=vlc.Instance()
        player=instance.media_player_new()
        media=instance.media_new('sound/OnBoard.mp3')
        player.set_media(media)
        player.play()
        
        update.message.reply_photo(open("img/plane.jpg","rb"));
        self.go_back(update)

    def on_exit_abroad(self, update):
        print("bye~let's go home")
    
    def on_enter_aroundisland(self, update):
        update.message.reply_text("Let's go as soon as possible")
        update.message.reply_photo(open("img/around.jpg","rb"))
        self.go_back(update)
    
    def on_exit_aroungisland(self, update):
        print("Let's go home")

    def on_enter_walk(self, update):
        update.message.reply_text("Let's take a walk")

    def on_enter_departmentstore(self, update):
        update.message.reply_text("I'm entering department store")
        update.message.reply_photo(open("img/department.jpg","rb"));
        self.go_back(update)

    def on_exit_departmentstore(self, update):
        print('Finish shopping')
    
    def on_enter_park(self, update):
        update.message.reply_text("Let's play on the swing")
        update.message.reply_photo(open("img/swing.jpg","rb"));
        self.go_back(update)

    def on_exit_park(self, update):
        print('Leaving park')

    def on_enter_drive(self, update):
        update.message.reply_text("Here's your key,where do you want to go?")

    def on_enter_Kaohsiung(self, update):
        update.message.reply_text("Welcome to Kaohsiung")
        update.message.reply_photo("https://api.services.trvl.com/backgrounds/images/kaohsiung_1.jpg")
        self.go_back(update)

    def on_exit_Kaohsiung(self, update):
        print('Leaving Kaohsiung')
    
    def on_enter_mountainclimbing(self, update):
        update.message.reply_text("Let's start mountain climbing")
        update.message.reply_photo(open("img/mountain.jpg","rb"));
        self.go_back(update)

    def on_exit_mountainclimbing(self, update):
        print('Finish mountain climbing')
    
    def on_enter_game(self, update):
        update.message.reply_text("I'm playing game")
        
        instance=vlc.Instance()
        player=instance.media_player_new()
        media=instance.media_new('sound/LINE.mp3')
        player.set_media(media)
        player.play()

        second=10;   #sleep 10 seconds
        while second>=0:
            update.message.reply_text(second)
            time.sleep(1)
            second-=1;

        self.go_back(update)

    def on_exit_game(self, update):
        print('Leaving game')

    def on_enter_sleep(self, update):
        update.message.reply_text("I'm sleeping now")

        second=5;   #sleep 5 seconds
        while second>=0:
            update.message.reply_text(second)
            time.sleep(1)
            second-=1;
        
        instance=vlc.Instance()
        player=instance.media_player_new()
        media=instance.media_new('sound/WakeUp.mp3')
        player.set_media(media)
        player.play()
                    
        update.message.reply_text("I wake up")
        self.go_back(update)

    def on_exit_sleep(self, update):
        print('Wake up')

