
# Spam Detector using simple keyword match
def is_spam(message):
    keywords = ["free", "won", "click", "offer", "prize"]
    return any(word in message.lower() for word in keywords)

message = input("Enter a message: ")
print("Spam" if is_spam(message) else "Safe")
