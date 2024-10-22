##requirements

# pip install moviepy
# pip install google-cloud-speech
# pip install SpeechRecognition pydub
# pip install gtts




# #Video To Audio

# from moviepy.editor import VideoFileClip

# # Load the video file
# video = VideoFileClip("C:/video to audio and Language transulation/What is TensorFlow _ TensorFlow Explained in 3-Minutes _ Introduction to TensorFlow _ Intellipaat.mp4")

# # Extract audio
# audio = video.audio

# # Save audio to a file
# audio.write_audiofile("C:/video to audio and Language transulation/output_audio.wav")




# #Video To Audio

# from moviepy.editor import VideoFileClip
# import os

# # Define paths
# video_path = r"C:/video to audio and Language transulation/What is TensorFlow _ TensorFlow Explained in 3-Minutes _ Introduction to TensorFlow _ Intellipaat.mp4"
# audio_output_path = r"C:/video to audio and Language transulation/output_audio.wav"

# # Ensure the output directory exists
# output_directory = os.path.dirname(audio_output_path)
# if not os.path.exists(output_directory):
#     os.makedirs(output_directory)

# # Load the video file
# video = VideoFileClip(video_path)

# # Extract audio
# audio = video.audio

# # Save audio to a file
# audio.write_audiofile(audio_output_path)





# # #Audio To Text

# import speech_recognition as sr

# # Convert audio file to compatible format
# audio_file = "C:/video to audio and Language transulation/output_audio.wav"

# # Initialize recognizer
# recognizer = sr.Recognizer()

# # Load audio file using SpeechRecognition
# with sr.AudioFile(audio_file) as source:
#     audio_data = recognizer.record(source)  # Read the entire audio file

# # Recognize (convert from speech to text)
# try:
#     # Using Google Web Speech API for speech-to-text
#     text = recognizer.recognize_google(audio_data)
#     print("Transcription: ", text)

# except sr.UnknownValueError:
#     print("Google Web Speech API could not understand the audio.")
# except sr.RequestError as e:
#     print(f"Could not request results from Google Web Speech API; {e}")




#English text to french text 

# import speech_recognition as sr
# from googletrans import Translator

# # Path to your audio file
# audio_file = "C:/video to audio and Language transulation/output_audio.wav"

# # Initialize recognizer and translator
# recognizer = sr.Recognizer()
# translator = Translator()

# # Load audio file using SpeechRecognition
# with sr.AudioFile(audio_file) as source:
#     audio_data = recognizer.record(source)  # Read the entire audio file

# # Recognize (convert from speech to text)
# try:
#     # Using Google Web Speech API for speech-to-text
#     english_text = recognizer.recognize_google(audio_data)
#     print("Transcription: ", english_text)

#     # Translate text from English to French
#     translated_text = translator.translate(english_text, src='en', dest='fr').text
#     print("Translated Text in French: ", translated_text)

# except sr.UnknownValueError:
#     print("Google Web Speech API could not understand the audio.")
# except sr.RequestError as e:
#     print(f"Could not request results from Google Web Speech API; {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")





# #converthing english text into french text, then save that french text in audio

# import speech_recognition as sr
# from googletrans import Translator
# from gtts import gTTS

# # Path to your audio file
# audio_file = "C:/video to audio and Language transulation/output_audio.wav"

# # Initialize recognizer and translator
# recognizer = sr.Recognizer()
# translator = Translator()

# # Load audio file using SpeechRecognition
# with sr.AudioFile(audio_file) as source:
#     audio_data = recognizer.record(source)  # Read the entire audio file

# # Recognize (convert from speech to text)
# try:
#     # Using Google Web Speech API for speech-to-text
#     english_text = recognizer.recognize_google(audio_data)
#     print("Transcription: ", english_text)

#     # Translate text from English to French
#     translated_text = translator.translate(english_text, src='en', dest='fr').text
#     print("Translated Text in French: ", translated_text)

#     # Convert the translated French text to speech using gTTS
#     tts = gTTS(text=translated_text, lang='fr')
#     tts.save("C:/video to audio and Language transulation/french_audio.mp3")

#     print("French audio has been saved as 'french_audio.mp3'.")

# except sr.UnknownValueError:
#     print("Google Web Speech API could not understand the audio.")
# except sr.RequestError as e:
#     print(f"Could not request results from Google Web Speech API; {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")











##################


# #used to convert mp3 audio file to wav audio file

# import librosa
# import soundfile as sf

# # Load MP3 file
# audio_file = "C:/video to audio and Language transulation/french_audio.mp3"
# wav_file = "C:/video to audio and Language transulation/french_audio.wav"

# # Load MP3 file into librosa
# data, sample_rate = librosa.load(audio_file, sr=None)

# # Save as WAV file using soundfile
# sf.write(wav_file, data, sample_rate)

# print("Conversion complete. WAV file saved.")




# #Video To Audio

# from moviepy.editor import VideoFileClip

# # Load the video file
# video = VideoFileClip("C:/video to audio and Language transulation/What is TensorFlow _ TensorFlow Explained in 3-Minutes _ Introduction to TensorFlow _ Intellipaat.mp4")

# # Extract audio
# audio = video.audio

# # Save audio to a file
# audio.write_audiofile("C:/video to audio and Language transulation/output_audio.wav")




# #Video To Audio

from moviepy.editor import VideoFileClip
import os

# Define paths
video_path = r"C:/video to audio and Language transulation/What is TensorFlow _ TensorFlow Explained in 3-Minutes _ Introduction to TensorFlow _ Intellipaat.mp4"
audio_output_path = r"C:/video to audio and Language transulation/output_audio.wav"

# Ensure the output directory exists
output_directory = os.path.dirname(audio_output_path)
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Load the video file
video = VideoFileClip(video_path)

# Extract audio
audio = video.audio

# Save audio to a file
audio.write_audiofile(audio_output_path)



#audio to text 
# #this code is used to convert any language audio to any language text 

# import speech_recognition as sr
# from googletrans import Translator

# # Path to your audio file
# audio_file = "C:/video to audio and Language transulation/french_audio.wav"

# # Initialize recognizer and translator
# recognizer = sr.Recognizer()
# translator = Translator()

# # Load audio file using SpeechRecognition
# with sr.AudioFile(audio_file) as source:
#     audio_data = recognizer.record(source)  # Read the entire audio file

# # Recognize (convert from speech to text)
# try:
#     # Using Google Web Speech API for speech-to-text in French
#     french_text = recognizer.recognize_google(audio_data, language='fr-FR')  # Specify French language
#     print("Transcription in French: ", french_text)

#     # Translate text from French to English
#     translated_text = translator.translate(french_text, src='fr', dest='en').text  # Corrected src and dest
#     print("Translated Text in English: ", translated_text)

# except sr.UnknownValueError:
#     print("Google Web Speech API could not understand the audio.")
# except sr.RequestError as e:
#     print(f"Could not request results from Google Web Speech API; {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")





# #converthing english text into french text, then save that french text in audio


import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

# Path to your audio file
audio_file = "C:/video to audio and Language transulation/french_audio.wav"

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

# Load audio file using SpeechRecognition
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)  # Read the entire audio file

# Recognize (convert from speech to text)
try:
    # Using Google Web Speech API for speech-to-text
    english_text = recognizer.recognize_google(audio_data,language='fr-FR')
    print("Transcription: ", english_text)

    # Translate text from English to French
    translated_text = translator.translate(english_text, src='fr', dest='en').text
    print("Translated Text in english: ", translated_text)

    # Convert the translated French text to speech using gTTS
    tts = gTTS(text=translated_text, lang='en')
    tts.save("C:/video to audio and Language transulation/english_audio.mp3")

    print("english audio has been saved as 'english_audio.mp3'.")

except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")
except Exception as e:
    print(f"An error occurred: {e}")














    
    
    
