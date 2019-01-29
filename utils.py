import cv2
import csv
import os

_CSV_FOLDER = './CSV'
frame_threshold = 32

def video2frames(src_video, shot_list):
	vidcap = cv2.VideoCapture(src_video)
	video_name = src_video.split('/')[2]
	video_name = video_name.split('.')[0]
	csv_name = video_name + '.csv'
	csv_path = os.path.join(_CSV_FOLDER, csv_name)
	f = open(csv_path, 'r', encoding='utf-8')
	rdr = csv.reader(f)

	line_num = 0
	count = 0
	for line in rdr:
		if line_num != 0:
			Start_frame_num = line[0]
			End_frame_num = line[1]
			frame_n = int(End_frame_num) - int(Start_frame_num) + 1
			_FRAME_FOLDER = os.path.join('./','FRAMES', video_name, Start_frame_num)
			if not (os.path.isdir(_FRAME_FOLDER)):
				os.makedirs(os.path.join(_FRAME_FOLDER))

			while count <= End_frame_num-1:
				success, image = vidcap.read()
				if success:
					img_name = "%d.jpg" % count
					img_path = os.path.join(_FRAME_FOLDER, img_name)
					cv2.imwrite(img_path, image)
				count += 1
		line_num += 1

	f.close()
