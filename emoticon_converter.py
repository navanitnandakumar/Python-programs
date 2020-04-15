emoticon_conv = {                   #dictionary
    ":)":"😊",
    ":(":"😢",
    ":D":"😃",
    ":|":"😐",
    ":o":"😮",
    ";)":"😉"
}

print("-------- 🔹 Emoticon Converter 🔹 --------")               
emote = input("Enter emoticon (in modern format) : ")          #user input
output_emoji = ""                                              #this is the variable used to store the emoji
output_emoji += emoticon_conv.get(emote) + " "                 #using dictionary to convert emote to emoji
print(output_emoji)                                            #to print emoji