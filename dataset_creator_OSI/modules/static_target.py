from osi3.osi_groundtruth_pb2 import GroundTruth


def build_static_target(width, length, height, x, y, roll, pitch, yaw,
                        timestamp_s, host_vehicle_id=0):
    """Build a GroundTruth message containing a single stationary object.

    Replaces the deprecated SensorDataSeries-based approach.

    Args:
        timestamp_s: Timestamp in seconds (e.g. from bag.get_start_time()).
            Mandatory per OSI spec (GroundTruth.timestamp is_set rule).
        host_vehicle_id: Identifier for the host vehicle. A matching
            moving_object entry is created so the reference is valid
            (required by Lichtblick FrameTransforms).

    Returns:
        A populated GroundTruth protobuf message.
    """
    gt = GroundTruth()
    gt.timestamp.seconds = int(timestamp_s)
    gt.timestamp.nanos = int((timestamp_s % 1) * 1e9)
    gt.host_vehicle_id.value = host_vehicle_id

    # host_vehicle_id must reference a moving_object entry (OSI spec).
    # Only set the id — no type/dimensions since the ego vehicle properties
    # are not available in the source data.
    ego = gt.moving_object.add()
    ego.id.value = host_vehicle_id

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
