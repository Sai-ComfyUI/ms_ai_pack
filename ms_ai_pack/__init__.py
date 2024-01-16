__version__ = "0.0.6"

from .line_extractor.lineart import LineartDetector
from .line_extractor.lineart_anime import LineartAnimeDetector
from .line_extractor.mlsd import MLSDdetector
from .line_extractor.pidi import PidiNetDetector
from .line_extractor.hed import HEDdetector
from .line_extractor.canny import CannyDetector

from .depth_solve.midas import MidasDetector
from .depth_solve.leres import LeresDetector
from .depth_solve.zoe import ZoeDetector

from .body_detector.open_pose import OpenposeDetector
from .body_detector.mediapipe_face import MediapipeFaceDetector
from .body_detector.dwpose import DWposeDetector

from .normalmap_solve.normalbae import NormalBaeDetector


# from .segment_anything import SamDetector
# from .shuffle import ContentShuffleDetector
