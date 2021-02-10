#! /usr/bin/env python
# Completed by Harry Akeroyd for EGH450: Advanced Unmanned Aircraft Systems.
# Completed in 2019.
# This file was ran aboard a Raspberry Pi 3, on-boad a UAV.
# Referencing Repositories;
#             https://github.com/qutas
#             https://github.com/qutas/egh450_image_processor
#             https://github.com/qutas/egh450_navigation_interface
#             https://github.com/qutas/egh450_target_solvepnp
import sys
import rospy
import cv2
import numpy as np
import tf2_ros
import geometry_msgs.mg import TransformStamped
import std_msgs.msg import Time

from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import CameraInfo
from cv_bridge import CvBridge, CvBridgeError

# Global V
# broadcaster_S = None
# pub_found_S = None

# broadcaster_T = None
# pub_found_T = None

class PoseEstimator():
    def __init__(self):
        self.time_finished_processing = rospy.Time(0)

        # Set up the CV Bridge
        self.bridge = CvBridge()

        # Square Target Classifier
        ''' The below...
        '''
        sign_cascade_file_S = str(rospy.get_param("~cascade_file_S"))
        self.sign_cascade_S = cv2.CascadeClassifier(sign_cascade_file_S)

        # Triangle Target Classifier
        ''' The below...
        '''
        sign_cascade_file_T = str(rospy.get_param("~cascade_file_T"))
        self.sign_cascade_T = cv2.CascadeClassifier(sign_cascade_file_T)

        # Load in parameters from ROS - for BLUE
        self.param_use_compressed = rospy.get_param("~use_compressed", False)
        self.param_target_diam = rospy.get_param("~target_diam", 1.0)

        # Set additional camera parameters
        self.got_camera_info = False
        self.camera_matrix = None
        self.dist_coeffs = None

        # Set up the publishers, subscribers and tf2
        self.sub_info = rospy.Subscriber("~camera_info", CameraInfo, self.callback_info)

        if self.param_use_compressed:
            self.sub_img = rospy.Subscriber("~image_raw/compressed", CompressedImage, self.callback_info, queue_size=10)
            self.pub_overlay = rospy.Publisher("~overlay/image_raw/compressed", CompressedImage, queue_size=1)
        else:
            self.sub_img = rospy.Subscriber("~image_raw", Image, self.callback_info, queue_size=10)
            self.pub_overlay = rospy.Publisher("~overlay/image_raw", Image, queue_size=1)

        # Generate the model for the pose solver.
        # For this example, draw a square around where the circle should be.
        # There are 5 points, one in the centre, and one in each corner
        # taken, 0.0, 0.0, 0.0 out from the first part.
        ''' The below...
        '''
        squareLength = self.param_target_diam
        self.model_object = np.array([(0.0, 0.0, 0.0),
                                      (-squareLength/2, squareLength/2, 0.0),
                                      (squareLength/2, squareLength/2, 0.0),
                                      (squareLength/2, -squareLength/2, 0.0),
                                      (-squareLength/2, -squareLength/2, 0.0)])
        ''' The below...
        '''
        self.broadcaster_S = tf2_ros.TransformBroadcaster()
        self.pub_found_S = rospy.Publisher('/emulated_uav/Square', Time, queue_size=10)

        self.broadcaster_T = tf2_ros.TransformBroadcaster()
        self.pub_found_T = rospy.Publisher('/emulated_uav/Triangle', Time, queue_size=10)


        def shutdown(self):
            # Unregister anything that needs it here
            self.sub_info.unregister()
            self.sub_img.unregister()


        def callback_info(self, msg_in):
            # Collect in the camera characteristics
            self.dist_coeffs = np.([[msg_in.D[0], msg_in.D[1], msg_in.D[2], msg_in.D[3], msg_in.D[4]]], dtype="double")

            self.camera_matrix = np.arry([(msg_in.P[0], msg_in.P[1], msg_in.P[2]),
                                          (msg_in.P[4], msg_in.P[5], msg_in.P[6]),
                                          (msg_in.P[9], msg_in.P[9], msg_in.P[10]))],
                                          dtype="double")
            if not self.got_camera_info:
                rospy.loginfo("Got camera info")
                self.got_camera_info = True


        def callback)img(self, msg_in):
            if msg_in.header.stamp > self.time_finished_processing:

            # Don't bother to process image if we don't have camera calibration.
                if self.got_camera_info:
                    # Convert ROS image to CV image
                    cv_image = None

                    try:
                        if self.param_use_compressed:
                            cv_image = self.bridge.compressed_imgmsg_to_cv2(msg_in, "bgr8")
                        else:
                            cv_image = self.bridge.imgmsg_to_cv2(msg_in, "bgr8")
                    except CvBridgeError as e:
                        rospy.loginfo(e)
                        return

                    # If a square was detected:
                    ''' The below...
                    '''
                    sign_s = self.sign_cascade_S.detectMultiScale(cv_image, 1.01,1)
                    sign_s = self.sign_cascade_T.detectMultiScale(cv_image, 1.01,1)

                    if sign_S is not None:
                        for (x,y,w,h) in sign_S:
                    # Calculate the pictured model for the pose solver
                    # For this example, draw a square around where the circle
                    # should be. There are 5 points, one in the center, and
                    # one in each corner.
                            self.mode_image_S = np.array([(x+(w/2), y+(h/2)),
                                                          (x, y),
                                                          (x+w, y),
                                                          (x, y+h),
                                                          (x+w, y+h)], dtype=np.float32)])

                    # Do the SolvePnP method.
                            (success, rvec_S, tvec_S) = cv2.solvePnP(self.model_object, self.mode_image_S, self.camera_matrix, self.dist_coeffs)

                    # If a result was found, send to TF2
                            if success:
                                # broadcaster_S = tf2.ros.TransformBroadcaster()
                                # pub_found_S = rospy.Publisher('/emulated_uav/Square', Time, queue_size=10)

                                time_found_S = rospy.Time.now()
                                S = TransformStamped()
                                S.header.stamp = time_found_S
                                S.header.frame_id = "camera"
                                S.child_frame_id = "Square"
                                S.transform.translation.x = tvec_S[0]
                                S.transform.translation.y = tvec_S[1]
                                S.transform.translation.z = tvec_S[2]

                                S.transform.rotation.x = 0
                                S.transform.rotation.y = 0
                                S.transform.rotation.z = 0
                                S.transform.rotation.w = 0

                                self.broadcaster_S.sendTransform(S)
                                self.pub_found_S.publish(time_found_S)

                    # Draw the circle for the overlay.
                            cv2.rectangle(cv_image, (x,y), (x+w,y+h), (0,140,255), 2)

                    ''' The below...
                    '''
                    if sign_T is not None:
                        for (x,y,w,h) in sign_T:
                    # Calculate the pictured model for the pose solver
                    # For this example, draw a square around where the circle
                    # should be. There are 5 points, one in the center, and
                    # one in each corner.
                            self.mode_image_T = np.array([(x+(w/2), y+(h/2)),
                                                          (x, y),
                                                          (x+w, y),
                                                          (x, y+h),
                                                          (x+w, y+h)], dtype=np.float32)])

                    # Do the SolvePnP method.
                            (success, rvec_T, tvec_T) = cv2.solvePnP(self.model_object, self.mode_image_T, self.camera_matrix, self.dist_coeffs)

                    # If a result was found, send to TF2
                            if success:
                                # broadcaster_T = tf2.ros.TransformBroadcaster()
                                # pub_found_T = rospy.Publisher('/emulated_uav/Triangle', Time, queue_size=10)

                                time_found_T = rospy.Time.now()
                                T = TransformStamped()
                                T.header.stamp = time_found_T
                                T.header.frame_id = "camera"
                                T.child_frame_id = "Triangle"
                                T.transform.translation.x = tvec_T[0]
                                T.transform.translation.y = tvec_T[1]
                                T.transform.translation.z = tvec_T[2]

                                T.transform.rotation.x = 0
                                T.transform.rotation.y = 0
                                T.transform.rotation.z = 0
                                T.transform.rotation.w = 0

                                self.broadcaster_T.sendTransform(S)
                                self.pub_found_T.publish(time_found_T)

                    # Draw the circle for the overlay.
                            cv2.rectangle(cv_image, (x,y), (x+w,y+h), (255,0,0), 2)

                    # Convert CV image to ROS image and publish the mask/overlay
                    try:
                        if self.param_use_compressed:
                            self.pub_overlay.publish(self.bridge.cv2_to_compressed_imgmsg(cv_image, "png"))
                        else:
                            self.pub_overlay.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
                    except (CvBridgeError, TypeError) as e:
                        rospy.loginfo(e)

                    self.time_finished_processing = rospy.Time.now()
