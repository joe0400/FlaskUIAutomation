import pyaudio
import librosa
import numpy
import threading

class AudioTranscevier:

    def __init__(self, timestep):
        self.timestep = timestep
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def callback_processor(self, in_data, frame_count, time_info, flag):
        if(self.callback == None): return
        self.callback(in_data, frame_count, time_info, flag)

    def setup_transceiver(self):
        self.pyaudio_value = pyaudio.PyAudio()
        self.stream = self.pyaudio_value.open(
            format=pyaudio.paFloat32,
            channels=2,
            rate=44100,
            input=True,
            output=False,
            stream_callback=self.callback_processor,
            frames_per_buffer=1024*2
        )

    # this needs to be daemonic in nature, for it to make sense

    def mainloop(self):

        def innerfunc():
            rolling_frames = []
            while(True):
                frame = self.stream.read(1)
                rolling_frames.append(frame)
                if(len(rolling_frames) > 10):
                    rolling_frames = rolling_frames[:-1:10]

        threading.Thread(
            target=innerfunc,
            name="AudioProcessorThread",
            daemon=True
        )