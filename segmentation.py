import os
from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
import scipy.io.wavfile as wavfile
import wave


def remove_silence(filename, out_dir, smoothing=1.0, weight=0.3, plot=True):
    print(filename)
    partic_id = 'P' + filename.split(r'/')[-1].split('_')[0][6:]
    print(partic_id)
    if is_segmentable(partic_id):
        participant_dir = os.path.join(out_dir,partic_id)
        print(participant_dir)
        if not os.path.exists(participant_dir):
            os.makedirs(participant_dir)

        os.chdir(participant_dir)

        [Fs, x] = aIO.read_audio_file(filename)
        segments = aS.silence_removal(x, Fs, 0.020, 0.020,
                                     smooth_window=smoothing,
                                     weight=weight,
                                     plot=plot)

        for s in segments:
            seg_name = "{:s}_{:.2f}-{:.2f}.wav".format(partic_id, s[0], s[1])
            wavfile.write(seg_name, Fs, x[int(Fs * s[0]):int(Fs * s[1])])
        concatenate_segments(participant_dir, partic_id)


def is_segmentable(partic_id):
    troubled = set(['P300', 'P305', 'P306', 'P308', 'P315', 'P316', 'P343',
                    'P354', 'P362', 'P375', 'P378', 'P381', 'P382', 'P385',
                    'P387', 'P388', 'P390', 'P392', 'P393', 'P395', 'P408',
                    'P413', 'P421', 'P438', 'P473', 'P476', 'P479', 'P490',
                    'P492'])
    return partic_id not in troubled


def concatenate_segments(participant_dir, partic_id, remove_segment=False):

    infiles = os.listdir(participant_dir) 
    outfile = '{}_no_silence.wav'.format(partic_id)

    data = []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
        if remove_segment:
            os.remove(infile)

    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for idx in range(len(data)):
        output.writeframes(data[idx][1])
    output.close()


if __name__ == '__main__':
    dir_name = r'C:/Dinesh/SEM-VI/RBL/Mental_Health_Portal/data/raw/audio'
    out_dir = r'C:/Dinesh/SEM-VI/RBL/Mental_Health_Portal/data/processed'
    for file in os.listdir(dir_name):
        print("Hello")
        print(file)
        if file.endswith('.wav'):
            print("Hello1")
            filename = os.path.join(dir_name,file)
            remove_silence(filename, out_dir)