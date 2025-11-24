with open("poems.txt","r") as f:
    text=f.read()
    lower_text=text.lower()
    
    if "twinkle" in lower_text:
        print("present")
    else:
        print("not found")