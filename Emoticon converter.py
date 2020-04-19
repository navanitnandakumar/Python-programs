emoticon_conv = {                  
    #dictionary
    ":)":"😊",
    ":(":"😢",
    ":D":"😃",
    ":|":"😐",
    ":o":"😮",
    ";)":"😉"
}

print("-------- 🔹 Emoticon Converter 🔹 --------")
#user input
emote = input("Enter emoticon (in modern format) : ")    
#to store the emoji
output_emoji = ""    
#using dictionary to convert emote to emoji
output_emoji += emoticon_conv.get(emote) + " "   
#to print emoji
print(output_emoji)                                           
