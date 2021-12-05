from multiprocessing import Process
import multiprocessing
import cv2


def stream(path, queue):
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
        while frame_counter < 510:
            # grab the current frame
            res, frame = vs.read()
            if res:
                # cv2.imshow("Frame", frame)
                # cv2.waitKey()
                i = 2
            # todo share frame with detector
            # if the frame could not be grabbed, then we have reached the end of the video
            if frame is None:
                print("End of Video")
                # todo task 3 - end all processes
                break
            else:
                queue.put(frame)
                print("stream frame #", frame_counter)
                frame_counter += 1


def f(name):
    print('hello', name)


def detect(stream_queue):
    frame_counter = 1
    while True:
        frame = stream_queue.get()
        # cv2.imshow("Frame", frame)
        # cv2.startWindowThread()
        # cv2.namedWindow("preview")
        cv2.imshow("preview", frame)
        # cv2.waitKey()
        print("detect frame #", frame_counter)
        frame_counter += 1


if __name__ == '__main__':
    video_path = 'C:/Users/ADAM/Downloads/People.mp4'

    stream_queue = multiprocessing.Queue()

    streamer = Process(target=stream, args=(video_path, stream_queue))
    streamer.start()

    detector = Process(target=detect, args=(stream_queue,))
    detector.start()

    presentor = Process(target=f, args=('presentor',))
    presentor.start()

    stream_queue.close()
    stream_queue.join_thread()
    streamer.join()
    detector.join()
    presentor.join()
