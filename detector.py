from __future__ import print_function
import os
import csv
import scenedetect
from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.frame_timecode import FrameTimecode
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors import ContentDetector

_CSV_FOLDER = './CSV'

def extract_shots_with_pyscenedetect(src_video, threshold=0, min_scene_length=15):
	video_manager = VideoManager([src_video])
	stats_manager = StatsManager()
	scene_manager = SceneManager(stats_manager)
	scene_manager.add_detector(ContentDetector(threshold, min_scene_length))
	base_timecode = video_manager.get_base_timecode()
	scene_list = []

	try:
		start_time = base_timecode
		video_manager.set_duration(start_time=start_time)
		video_manager.set_downscale_factor(downscale_factor=1)
		video_manager.start()
		scene_manager.detect_scenes(frame_source=video_manager, frame_skip = 0)
		scene_list = scene_manager.get_scene_list(base_timecode)
		# print('List of scenes obtained:')
		# for i, scene in enumerate(scene_list):
		# 	print('    Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
		# 		i + 1,
		# 		scene[0].get_timecode(), scene[0].get_frames(),
		# 		scene[1].get_timecode(), scene[1].get_frames(),))
		write_csv(src_video, scene_list)
	except:
		print("error")
	finally:
		video_manager.release()
	return scene_list


def write_csv(src_video, scene_list):
	if not (os.path.isdir(_CSV_FOLDER)):
		os.makedirs(os.path.join(_CSV_FOLDER))
	video_name = src_video.split('/')[2]
	video_name = video_name.split('.')[0] + '.csv'
	csv_path = os.path.join(_CSV_FOLDER, video_name)
	print(csv_path)
	f = open(csv_path, 'w', encoding='utf-8', newline='')
	wr = csv.writer(f)
	wr.writerow(["Start Frame", "End Frame", "Start Time", "End Time"])
	for i, scene in enumerate(scene_list):
		start_frame_num = "%08d" %(scene[0].get_frames())
		end_frame_num = "%08d" % (scene[1].get_frames())
		wr.writerow([start_frame_num, end_frame_num, scene[0].get_timecode(), scene[1].get_timecode()])
	f.close()