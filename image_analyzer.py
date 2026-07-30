"""

image_analyzer.py



Main module for the Image Analyzer Project.

"""

import os

import cv2

import time

import logging



from config import (

    OUTPUT_FOLDER,

    REPORT_FILE,

    RESIZE_WIDTH,

    RESIZE_HEIGHT

)



from file_handler import (

    get_image_files,

    get_file_size

)



from utils import (

    get_filename,

    get_extension,

    format_resolution,

    print_line,

    get_orientation,

    get_image_type,

    calculate_aspect_ratio,

    print_dataset_info

)





class ImageAnalyzer:

    """

    Image Analyzer Class

    """



    def __init__(self):



        self.total_images = 0

        self.success_count = 0

        self.failed_count = 0



        self.report_data = []



        self.start_time = 0



    # ----------------------------------------------------



    def analyze_images(self):

        """

        Reads all images and starts processing.

        """



        self.start_time = time.time()



        image_files = get_image_files()



        if not image_files:



            print("\nNo Images Found Inside input_images Folder.")



            logging.warning("No Images Found.")



            return



        self.total_images = len(image_files)



        print_dataset_info(self.total_images)



        for index, image_path in enumerate(image_files, start=1):



            print()

            print_line()



            print(

                f"Processing Image {index} of {self.total_images}"

            )



            print_line()



            try:



                self.process_image(image_path)



                print("\n✓ Successfully Processed")



            except Exception as error:



                self.failed_count += 1



                logging.error(error)



                print(f"\n✗ Failed : {error}")



        self.generate_report()



        self.display_summary()



    # ----------------------------------------------------



    def process_image(self, image_path):

        """

        Processes one image.

        """



        image = cv2.imread(image_path)



        if image is None:



            raise ValueError(

                "Corrupted or Unsupported Image."

            )



        height, width, channels = image.shape



        filename = get_filename(image_path)



        extension = get_extension(image_path)



        resolution = format_resolution(

            width,

            height

        )



        orientation = get_orientation(

            width,

            height

        )



        aspect_ratio = calculate_aspect_ratio(

            width,

            height

        )



        image_type = get_image_type(

            channels

        )



        file_size = get_file_size(

            image_path

        )



        self.display_image_information(

            filename,

            extension,

            resolution,

            orientation,

            aspect_ratio,

            channels,

            image_type,

            file_size

        )



        gray_image = self.convert_grayscale(

            image

        )



        resized_image = self.resize_image(

            gray_image

        )



        self.save_image(

            gray_image,

            resized_image,

            filename

        )



        self.report_data.append({



            "name": filename,



            "extension": extension,



            "resolution": resolution,



            "orientation": orientation,



            "aspect_ratio": aspect_ratio,



            "channels": channels,



            "type": image_type,



            "size": file_size



        })



        self.success_count += 1



        logging.info(

            f"{filename} Processed Successfully."

        )



    # ----------------------------------------------------



    def display_image_information(

        self,

        filename,

        extension,

        resolution,

        orientation,

        aspect_ratio,

        channels,

        image_type,

        file_size

    ):

        """

        Displays Image Information.

        """



        print(f"Image Name      : {filename}")



        print(f"Extension       : {extension}")



        print(f"Resolution      : {resolution}")



        print(f"Orientation     : {orientation}")



        print(f"Aspect Ratio    : {aspect_ratio}")



        print(f"Channels        : {channels}")



        print(f"Image Type      : {image_type}")



        print(f"File Size       : {file_size} MB")



    # ----------------------------------------------------



    def convert_grayscale(

        self,

        image

    ):

        """

        Converts image to grayscale.

        """



        return cv2.cvtColor(

            image,

            cv2.COLOR_BGR2GRAY

        )



    # ----------------------------------------------------



    def resize_image(

        self,

        image

    ):

        """

        Resizes image.

        """



        return cv2.resize(



            image,



            (

                RESIZE_WIDTH,

                RESIZE_HEIGHT

            )



        )

    # ----------------------------------------------------



    def save_image(

        self,

        gray_image,

        resized_image,

        filename

    ):

        """

        Saves processed images.

        """



        name = os.path.splitext(filename)[0]



        gray_path = os.path.join(

            OUTPUT_FOLDER,

            f"{name}_gray.jpg"

        )



        resized_path = os.path.join(

            OUTPUT_FOLDER,

            f"{name}_resized.jpg"

        )



        cv2.imwrite(

            gray_path,

            gray_image

        )



        cv2.imwrite(

            resized_path,

            resized_image

        )



        logging.info(

            f"{filename} Saved Successfully."

        )



    # ----------------------------------------------------



    def generate_report(self):

        """

        Generates analysis report.

        """



        try:



            with open(

                REPORT_FILE,

                "w",

                encoding="utf-8"

            ) as report:



                report.write("=" * 80 + "\n")

                report.write("IMAGE ANALYSIS REPORT\n")

                report.write("=" * 80 + "\n\n")



                for index, data in enumerate(

                    self.report_data,

                    start=1

                ):



                    report.write(

                        f"Image {index}\n"

                    )



                    report.write(

                        "-" * 40 + "\n"

                    )



                    report.write(

                        f"Image Name      : {data['name']}\n"

                    )



                    report.write(

                        f"Extension       : {data['extension']}\n"

                    )



                    report.write(

                        f"Resolution      : {data['resolution']}\n"

                    )



                    report.write(

                        f"Orientation     : {data['orientation']}\n"

                    )



                    report.write(

                        f"Aspect Ratio    : {data['aspect_ratio']}\n"

                    )



                    report.write(

                        f"Channels        : {data['channels']}\n"

                    )



                    report.write(

                        f"Image Type      : {data['type']}\n"

                    )



                    report.write(

                        f"File Size       : {data['size']} MB\n"

                    )



                    report.write("\n")



            logging.info(

                "Report Generated Successfully."

            )



        except Exception as error:



            logging.error(

                f"Report Generation Failed : {error}"

            )



            print(

                "\nUnable to Generate Report."

            )



    # ----------------------------------------------------



    def display_summary(self):

        """

        Displays project summary.

        """



        execution_time = (

            time.time() - self.start_time

        )



        print()

        print("=" * 60)

        print("PROJECT SUMMARY")

        print("=" * 60)



        print(

            f"Total Images        : {self.total_images}"

        )



        print(

            f"Successfully Processed : {self.success_count}"

        )



        print(

            f"Failed Images       : {self.failed_count}"

        )



        print(

            f"Output Folder       : output_images"

        )



        print(

            f"Report File         : image_report.txt"

        )



        print(

            f"Execution Time      : {execution_time:.2f} Seconds"

        )



        print("=" * 60)



        logging.info(

            "Image Analysis Completed."

        )



        logging.info(

            f"Total Images : {self.total_images}"

        )



        logging.info(

            f"Processed : {self.success_count}"

        )



        logging.info(

            f"Failed : {self.failed_count}"

        )



        logging.info(

            f"Execution Time : {execution_time:.2f} Seconds"

        )