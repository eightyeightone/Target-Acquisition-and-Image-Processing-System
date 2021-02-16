## Target Acquisition and Image Processing System
###### Queensland University of Technology Project: EGH450 Advanced Unmanned Aircraft Systems, completed in Semester 2 of 2019 (22 July - 25 October).

#### Summary
The premise of this project was to develop an Unmanned Aircraft System (UAS) to complete an Urban Search and Rescue Mission (simulated in a QUT Laboratory). The project was separated into subsystems;

1. Project Manager,
2. Airframe, Power and Propulsion,
3. Payload Deployment,
4. Autopilot, Navigation and Localization,
5. Operator Interfaces,
6. **Target Acquisition and Image Processing**. 

I was the Target Acquisition \& Image Processing Lead, with six group members taking different leads. The task was to develop the UAS such that it could conduct an autonomous search of a simulated urban environment after a natural disaster. During the flight the UAS was required to identify and locate two human targets and deploy the correct emergency medication based on the target’s requirements (represented by a square and a triangle).

**High Level Objectives**

The designed system was required to adhere to the below high-level objectives. My subsystem pertained particularly to HLO-M-1, HLO-M-2, HLO-M-3, **HLO-M-4**, HLO-M-5 and HLO-M-7.

**HLO-M-1 – Autonomous Operation**
The UAS shall be capable of fully autonomous flight whilst remaining below a take-off weight of 1.8kg. The QUT ASL Robotic Operating System (ROS) UAV software is to be used as the base control system for navigation and image processing. The UAV shall be commanded to start the mission by user input then no further input is allowed. All interactions with the UAV are via a ground control station: a display of real flight time, telemetry and an imagery feed are to be provided.

**HLO-M-2 – Indoor Zone Coverage**
The UAV is to navigate around a 4x4m grid without colliding with any obstacles and successfully locate the two targets and deploy the correct medication in a single flight.

**HLO-M-3 – Sensor Data**
The UAV is to transmit live telemetry and imagery from the on-board computer to the ground control station. All telemetry information is to be provided to the customer in real time. On detection of each persons the ground control station shall alert the operator by vocalising the location and injury type. The information is to be displayed in a 3D model. 

**HLO-M-4 – Marker Identification**
Using real time flight imagery, the on-board computer must be able to autonomously detect the injured persons and their specific injury type and do so with a degree of error no greater than 50cm. All marker identification shall be carried out on-board the UAV.

**HLO-M-5 – Medication Delivery**
When each marker is identified and located, the UAV must deploy the correct medication. The computer vision system must relay the appropriate information to the navigation and payload subsystems, navigation must then interrupt the flight path and fly to the location of the target. The payload is then to be deployed.

**HLO-M-6 – Basic Hardware Demonstration**
A demonstration of the flight capabilities of the UAS shall be conducted in week 11 of the semester.

**HLO-M-7 – Systems Engineering Method**
The developed solution shall conform to the Systems Engineering approach taught throughout the unit.

**HLO-M-8 – Equipment**
Equipment shall be gathered by the team and adhere to the customers’ requirements in regards to budget and recommended suppliers.


###### By Harry Akeroyd. n9997121@QUT.edu.au
