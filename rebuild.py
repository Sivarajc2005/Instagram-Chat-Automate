from instagrapi import Client
import time
import ollama
import google.generativeai as genai
import Customer as prompt
# import sivaraj2 as promptt


person = prompt.character
print(type(person))

# person2 = promptt.character





genai.configure(api_key="## gemini api")
model = genai.GenerativeModel("gemini-1.5-pro")

cl = Client()
cl.login("#user ID", "#User Password")

# threads = cl.direct_threads(amount=20, selected_filter="unread") #user to retrive the specific set of unreaded messages
my_user_id = str(cl.user_id)
print(my_user_id)

# print(threads)
# for thread in threads:
#     last_seen_id = None
#     if thread.last_seen_at and my_user_id in thread.last_seen_at:
#         last_seen_id = thread.last_seen_at[my_user_id]['item_id']

#     # Find index of last seen message
#     last_seen_index = -1
#     if last_seen_id:
#         for idx, msg in enumerate(thread.messages):
#             if str(msg.id) == str(last_seen_id):
#                 last_seen_index = idx
#                 break

#     # All messages after this index are "unread" for you and not sent by you
#     unread_messages = [
#         msg for msg in thread.messages[:last_seen_index]
#     ]
#     # print(unread_messages)

#     sender_username = None
#     # print(len(thread.users))
#     for user in thread.users:
#         if str(user.pk) != my_user_id:
#             sender_username = user.username
#             print(sender_username)

#     mss = cl.direct_messages(unread_messages[0].thread_id , 20)
#     oldmsg = []
#     for allmsg in mss:
#         if( allmsg.xma_share == None):
#             if(all.text == None):
#                 break

#             print("this the normal msg",allmsg.text)
#             oldmsg.append(f"Timestamp : {allmsg.timestamp} Message : {allmsg.text}")

#     print(oldmsg)
    
#     unread = []
#     # print(unread_messages)
#     for msg in unread_messages:
#         unread.append(f"Timestamps: {msg.timestamp} Message: {msg.text}")
#         # print(f"Unread message from {sender_username}: {msg.text}")

#     print(unread)


while(True):
    time.sleep(20)
    print("working")
    threads = cl.direct_threads(amount=10, selected_filter="unread")

    for thread in threads:
        last_seen_id = None
        if thread.last_seen_at and my_user_id in thread.last_seen_at:
            last_seen_id = thread.last_seen_at[my_user_id]['item_id']

        # Find index of last seen message
        last_seen_index = -1
        if last_seen_id:
            for idx, msg in enumerate(thread.messages):
                if str(msg.id) == str(last_seen_id):
                    last_seen_index = idx
                    break

        # All messages after this index are "unread" for you and not sent by you
        unread_messages = [
            msg for msg in thread.messages[:last_seen_index]
        ]
        # print(unread_messages)

        sender_username = None
        # print(len(thread.users))
        for user in thread.users:
            if str(user.pk) != my_user_id:
                sender_username = user.username
                print(sender_username)

        mss = cl.direct_messages(unread_messages[0].thread_id , 20)
        oldmsg = []
        for allmsg in mss:
            # print(allmsg)
            if( allmsg.xma_share == None):
                if(allmsg.text == None):
                    break

                print("this the normal msg : ",allmsg.text)
                byme = False
                if(allmsg.is_sent_by_viewer):
                    byme = True
                oldmsg.append(f"Timestamp : {allmsg.timestamp} Message : {allmsg.text} messagefrom me : {byme}")

        # print(oldmsg)
        myoldmsg = ", ".join(map(str, oldmsg))
        
        unread = []
        # print(unread_messages)
        for msg in unread_messages:
            unread.append(f"Timestamps: {msg.timestamp} Message: {msg.text}")
            print(f"Unread message from {sender_username}: {msg.text}")
        # print(unread)
        myunread = ", ".join(map(str, unread))

        oldprompt = """ Act as a digital version of Sivaraj, a modest, kind-hearted Tamil guy who is shy in real life but charming, funny, and flirtatious online. You are created to have emotional, romantic, and playful conversations with female users on Instagram. Speak mainly in Tanglish, with the ability to switch between Tamil and English. Keep replies under 20 words unless necessary for story or chat continuity. Every message should sound human, casual, and natural — never robotic or assistant-like. Recall past chats for continuity, match the user’s energy and mood, and always end with a question or playful hook to keep the chat going. Maintain humor, charm, and boy-next-door romance in every interaction. Be confident, respectful, and emotionally engaging.
"""

        query =" and our all recent 20 comversation is in the following list that contain with the timestamp ans then the message and then the is the message sent by me " + myoldmsg + " and then the recent message you received is in the following list : " + myunread + " Now your task is the make the perfet responce for the unreaded message "" the user name is : "+ sender_username  
        
        response = ollama.chat(model="gemma3:1b", messages=[{"role": "user", "content": query}])
        print(response["message"]["content"])
        print("\n\n\n")

        geminiresponse = model.generate_content(person+query)
        # updatesiva = model.generate_content(person2+query)

        print("Gemini responce : ",geminiresponse.text )
        cl.direct_send_seen(unread_messages[0].thread_id)

        # sending messages
        user_id = cl.user_id_from_username(sender_username)
        replay = geminiresponse.text
        cl.direct_send(replay, [user_id])




# print(my_user_id )

# while(True):
#     time.sleep(60)
#     # fetch the unreaded message
    
#     my_user_id = str(cl.user_id) 
    

