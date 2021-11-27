from multiprocessing import Process
import cv2


def stream(path):
    # if the path argument is None, then path is invalid
    if path is None:
        print("Invalid video file path")
        return
    else:
        vs = cv2.VideoCapture(path)
        if vs is None:
            print("An error occurred when reading video from:", path)
            return
        frame_counter = 1
        while True:
            # grab the current frame
            res, frame = vs.read()
            if res:
                # debug cv2.imshow("Frame", frame)
                i = 2
                # todo share frame with detector
            # if the frame could not be grabbed, then we have reached the end of the video
            if frame is None:
                print("End of Video")
                # todo task 3 - end all processes
                break
            else:
                print("frame #", frame_counter)
                frame_counter += 1


def f(name):
    print('hello', name)


def detect():
    print('todo')


if __name__ == '__main__':
    video_path = 'C:/Users/ADAM/Downloads/People.mp4'

    streamer = Process(target=stream, args=(video_path,))
    streamer.start()

    detector = Process(target=f, args=('detector',))
    detector.start()

    presentor = Process(target=f, args=('presentor',))
    presentor.start()

    streamer.join()
    detector.join()
    presentor.join()
