from __future__ import print_function
import os
import scenedetect
from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.frame_timecode import FrameTimecode
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors import ContentDetector


def extract_shots_with_pyscenedetect(src_video, threshold=0, min_scene_length=15):
	# INFO_FILE_PATH = src_video + ".csv"

	video_manager = VideoManager([src_video])
	stats_manager = StatsManager()
	scene_manager = SceneManager(stats_manager)
	scene_manager.add_detector(ContentDetector(threshold, min_scene_length))
	base_timecode = video_manager.get_base_timecode()

	try:
		start_time = base_timecode
		# end_time = base_timecode + 20.0
		video_manager.set_duration(start_time=start_time)
		video_manager.set_downscale_factor(downscale_factor=1)
		video_manager.start()
		scene_manager.detect_scenes(frame_source=video_manager,frame_skip = 0)
		scene_list = scene_manager.get_scene_list(base_timecode)
		print('List of scenes obtained:')
		for i, scene in enumerate(scene_list):
			print('    Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
				i + 1,
				scene[0].get_timecode(), scene[0].get_frames(),
				scene[1].get_timecode(), scene[1].get_frames(),))

		return scene_list
	except:
		print("error")
	finally:
		video_manager.release()