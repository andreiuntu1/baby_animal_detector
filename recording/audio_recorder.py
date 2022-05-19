import sounddevice as sd
from scipy.io.wavfile import write
import os, sys
import shutil
import logging
from baby_animal_detection.prediction.prediction import _prediction
from baby_animal_detection.send_notification import send_notification

def _record():
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording
    wav = "record.wav"
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write(wav, fs, myrecording)  # Save as WAV file
    value = os.getcwd()+"\\"+wav
    return shutil.copy(value, os.path.dirname(os.path.abspath(__file__)))

def main(text):
    # Print logger
    # root = logging.getLogger()
    # root.setLevel(logging.DEBUG)
    # handler = logging.StreamHandler(sys.stdout)
    # handler.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # handler.setFormatter(formatter)
    # root.addHandler(handler)

    record_file = _record()
    #recognition = _call_recognition((record_file))
    #print(recognition)
    prediction = _prediction(record_file)
    if (prediction is None):
        return 'No one is in the car!'
    elif('Cat' in prediction):
        if('a little too cold' in text or 'getting warm' in text):
            send_notification.main('Notification!', text + prediction + "\nDon\'t forget that your CAT is in the car!")
        if('really cold' in text or 'pretty hot' in text):
            send_notification.main('Warning!',text + prediction + "\nYou should hurry up, your CAT is in the car!")
        if ('freeazing' in text or 'really hot' in text):
            send_notification.main('ALERT!!!!', text + prediction + "\nGo to car now!")
        if ( "Check car" in text):
            send_notification.main('Notification', text + prediction + "\nThe cat meows!")
        return 'Send notification!\n' + prediction
    elif('Dog' in prediction):
        if('a little too cold' in text or 'getting warm' in text):
            send_notification.main('Notification!', text + prediction + "\nDon\'t forget that your DOG is in the car!")
        if ('really cold' in text or 'pretty hot' in text):
            send_notification.main('Warning!', text + prediction + "\nYou should hurry up, your DOG is in the car!")
        if ('freeazing' in text or 'really hot' in text):
            send_notification.main('ALERT!!!!', text + prediction + "\nGo to car now!")
        if ( "Check car" in text):
            send_notification.main('Notification', text+ "\n" + prediction + "\n")
        return 'Send notification!\n' + prediction
    elif('Baby' in prediction):
        if('a little too cold' in text or 'getting warm' in text):
            send_notification.main('Notification!', text + prediction + "\nDon\'t forget that your BABY is in the car!")
        if ('really cold' in text or 'pretty hot' in text):
            send_notification.main('Warning!', text + prediction + "\nYou should hurry up, your BABY is in the car!")
        if ('freeazing' in text or 'really hot' in text):
            send_notification.main('ALERT!!!!', text + prediction + "\nGo to car now!")
        if ( "Check car" in text):
            send_notification.main('Notification', text + prediction + "\nBaby is crying!")
        return 'Send notification!\n' + prediction
    elif ("Check car" in text and "" in prediction):
        send_notification.main('Notification', text + prediction + "\nNo sound in the car!")
    else:
        return 'No one is in the car!'


if __name__ == '__main__':
    main()
