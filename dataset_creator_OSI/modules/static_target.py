from osi3.osi_groundtruth_pb2 import GroundTruth


def build_static_target(width, length, height, x, y, roll, pitch, yaw,
                        timestamp_s):
    """Build a GroundTruth message containing a single stationary object.

    Replaces the deprecated SensorDataSeries-based approach.

    Args:
        timestamp_s: Timestamp in seconds (e.g. from bag.get_start_time()).
            Mandatory per OSI spec (GroundTruth.timestamp is_set rule).

    Returns:
        A populated GroundTruth protobuf message.
    """
    gt = GroundTruth()
    gt.timestamp.seconds = int(timestamp_s)
    gt.timestamp.nanos = int((timestamp_s % 1) * 1e9)
    obj = gt.stationary_object.add()
    obj.base.dimension.width = width
    obj.base.dimension.length = length
    obj.base.dimension.height = height
    obj.base.position.x = x
    obj.base.position.y = y
    obj.base.orientation.roll = roll
    obj.base.orientation.pitch = pitch
    obj.base.orientation.yaw = yaw
    return gt
