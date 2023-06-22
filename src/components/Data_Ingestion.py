import cv2
import sys
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
import os

@dataclass
class DataIngestionConfig:
    storage_path: str = os.path.join('Data/')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initialize_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            # Path of video
            video_path = os.path.join(os.getcwd(), 'Video_data', 'Sample.mp4')
            video = cv2.VideoCapture(video_path)

            # Making directory to store the frames
            os.makedirs(self.ingestion_config.storage_path, exist_ok=True)
            logging.info("Created a data directory to store frames")

            frame_number = 0
            while True:
                # Read the next frame
                ret, frame = video.read()

                # Check if the frame was read successfully
                if not ret:
                    break

                # Save the frame as an image
                if frame_number % 20 == 0:  # Save every 50th frame
                    frame_path = os.path.join(self.ingestion_config.storage_path, 'frame{}.jpg'.format(frame_number))
                    cv2.imwrite(frame_path, frame)

                # Increment the frame number
                frame_number += 1

            video.release()
            cv2.destroyAllWindows()
            logging.info("Completed reading video")

            return self.ingestion_config.storage_path

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    frame = obj.initialize_data_ingestion()
