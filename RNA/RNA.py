def transcribe(seq):
    transcript = seq.replace("T","U",seq.count("T"))
    with open("RNA Answer.txt","w") as f:
        f.write(transcript)


