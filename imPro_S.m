%% IMAGE PROCESSING CODE:                                          15/08/19
%% CLEAN UP
clc, clear, close all

%% LOADING IN POSITIVE SAMPLES
load('pos_label.mat');

%% SELECTING THE BOUNDING BOXES FROM THE SUPPLIED SAMPLES
positiveInstances_S = pos_roi;

%% ADDING THE IMAGE FOLDER TO THE PATH
imDirPos_S = fullfile('/Users/h/Desktop/6 - - EGH450/G1_Image_Processor/training_cascade_opencv/pos_S');
addpath(imDirPos_S);

%% SPECIFYING THE NEGATIVE IMAGES FOLDER
negativeFolder_S = fullfile('/Users/h/Desktop/6 - - EGH450/G1_Image_Processor/training_cascade_opencv/neg_S');

%% STORING THE NEGATIVE IMAGES IN A OBJECT
negativeImages = imageDatastore(negativeFolder_S);

%% TRAINING THE CLASSIFIER USING HAAR FEATURES
trainCascadeObjectDetector('cascade_S.xml',positiveInstances_S, negativeFolder_S,...
                           'FalseAlarmRate',0.1,...
                           'TruePositiveRate',0.98,...
                           'NumCascadeStages', 20,...
                           'FeatureType', 'Haar');

%% USING THE NEWLY TRAINED CLASSIFIER
detector = vision.CascadeObjectDetector('cascade_S.xml');

%% IMAGE TESTING SAMPLES
T1 = imread('IMG_6423.jpeg'); 

%% IMAGE 1 -------- SUB T1 FOR TESTING IMAGE
bbox = step(detector,T1);
detectedImg = insertObjectAnnotation(T1, 'rectangle', bbox, 'Target - Orange Square', 'LineWidth', 10, 'FontSize', 70);
figure; imshow(detectedImg);

%% VIDEO
vid = VideoReader('test_vid.mp4');
detector = vision.CascadeObjectDetector('cascade.xml');

    while hasFrame(vid)
        vf = readFrame(vid);
        bbox = step(detector, vf);
        detectedImg = insertObjectAnnotation(vf, 'rectangle', bbox, 'Target Identified', 'LineWidth', 10, 'FontSize', 20);
        imshow(detectedImg);
    end

%% NB:
%{
%}

