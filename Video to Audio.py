##requirements

#pip install moviepy
#pip install google-cloud-speech
#pip install SpeechRecognition pydub
#pip install gtts




# #Video To Audio

from moviepy.editor import VideoFileClip

# Load the video file
video = VideoFileClip("C:/video to audio/What is TensorFlow _ TensorFlow Explained in 3-Minutes _ Introduction to TensorFlow _ Intellipaat.mp4")

# Extract audio
audio = video.audio

# Save audio to a file
audio.write_audiofile("C:/video to audio/output_audio.wav")







# # #Audio To Text

# import speech_recognition as sr

# # Convert audio file to compatible format
# audio_file = "C:/video to audio/output_audio.wav"

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
# audio_file = "C:/video to audio/output_audio.wav"

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





#converthing english text into french text, then save that french text in audio

# import speech_recognition as sr
# from googletrans import Translator
# from gtts import gTTS

# # Path to your audio file
# audio_file = "C:/video to audio/output_audio.wav"

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
#     tts.save("C:/video to audio/french_audio.mp3")

#     print("French audio has been saved as 'french_audio.mp3'.")

# except sr.UnknownValueError:
#     print("Google Web Speech API could not understand the audio.")
# except sr.RequestError as e:
#     print(f"Could not request results from Google Web Speech API; {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")


















#pip install for TTS is not working



# from TTS.api import TTS

# # Initialize the TTS model with a valid model name
# tts = TTS(model_name='tts_models/multilingual/multi-dataset/your_tts_model_name')

# # Print available speakers for the model
# print("Available speakers:", tts.speakers)


# import torch
# from TTS.api import TTS
# import os

# # Set the device to 'cpu' since you are not using a GPU
# device = "cpu"

# def generate_audio(text="A journey of a thousand miles begins with a single step"):
#     # Initialize the TTS model
#     tts = TTS(model_name='tts_models/multilingual/multi-dataset/your_tts_model_name', progress_bar=True)

#     # Generate audio file in Arabic
#     output_file_path = "C:/video to audio/output.wav"
#     tts.tts_to_file(
#         text=text,
#         file_path=output_file_path,
#         speaker="your_speaker_name",  # Replace with a valid speaker name for your model
#         language="ar"
#     )

#     return output_file_path

# # Call the function and print the output file path
# output_path = generate_audio()
# print(f"Audio generated and saved at: {output_path}")












    
    
    
