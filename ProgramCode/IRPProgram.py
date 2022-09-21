# -*- codinF: utf-8 -*-
"""
Created on Sat Jul 23 16:50:07 2022

@author: Epic_
"""
import time
import cv2 as cv
import sys
import numpy as np
import tensorflow as tf
import pandas as pd
import sklearn
import glob
import imutils
import pickle
import matplotlib.patches as patches
import os
from pathlib import Path
import PIL.Image as Image
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras import activations, datasets, layers, losses, metrics, models, optimizers, regularizers,utils,callbacks,preprocessing,applications
plt.rcParams['figure.dpi'] = 300


def imagetoarray(imagepath):
    image = cv.resize(cv.imread(imagepath),(224,224)) #resize image 
    image = image.astype('float32')
    image /= 255.0 #scaling 
    return image #creates array from iamges


def image2array(imagepath):
    imagelist = []
    for i in imagepath:
        image = cv.resize(cv.imread(i),(224,224))
        image = image.astype("float32")
        image /= 255.0
        imagelist.append(image)
    print("Images Imported")
    return imagelist #creates array from iamges

def readcsv(csvfileloc):
    trbbdf = pd.read_csv(csvfileloc,encoding = 'unicode_escape',header = None)
    trbbdf = trbbdf.iloc[1:,:]
    trbbdf = trbbdf[trbbdf[3] != "banana tip"]
    trbbdf = trbbdf[trbbdf[3] != "cauliflower"]
    # trbbdf[3] = trbbdf[3].apply(str.lower)
    return trbbdf

def getimagepaths(dataframe,add):
    impdf = dataframe[0].to_numpy(dtype="unicode")
    imgpath = []
    for i in impdf:
        imgpath.append("F:\Cranfield\IRP\Datasets\SecondWindOrange\\"+add+i)
   # imparray = impdf.to_numpy()
    
    return imgpath

def getgroundtruths(dataframe,imgpath,testbool):
   
    if testbool == False:
       bbdfpre = dataframe.loc[:,4:7] ##bbox dataframe
       bbdf = dataframe.loc[:,4:7] ##bbox dataframe
       ldf = dataframe[3].to_numpy() #label dataframe
       ldf.astype("str") 
    elif testbool == True:
        bbdfpre = dataframe.loc[:,1:4] ##bbox dataframe
        bbdf = dataframe.loc[:,1:4] ##bbox 
        ldf = dataframe[0].to_numpy() #label dataframe
        ldf.astype("str") 
        
    k = 0
    bbto = []
    for i in imgpath:
        image = cv.imread(i)
        #print(i)
        (h,w) = image.shape[:2]
        blabdo = []
        blabdo.append(bbdf.iat[k,0])
        blabdo.append(bbdf.iat[k,1])
        blabdo.append(bbdf.iat[k,2])
        blabdo.append(bbdf.iat[k,3])
        blabdo = np.array(blabdo)
        blabdo = blabdo.astype("float32")
        # print("height: ",h)
        # print("weight: ",w)
        blabdo[0] = (blabdo[0])/w  #converts labels into correct ratios for the w/h of the specific image data. (x)
        blabdo[1] = (blabdo[1])/h #(y)
        blabdo[2] = (blabdo[2])/w #(width)
        blabdo[3] = (blabdo[3])/h #(height)
        bbto.append(blabdo)
        k = k + 1
        
    
    lb_list = []
    for i in ldf:
        lb_list.append(i)
    label = np.array(lb_list)
    lb = LabelBinarizer()
    cl_label = lb.fit_transform(label)
    print(len(lb.classes_))
    #cl_label = utils.to_categorical(cl_label,1)
    
    return bbto,cl_label,lb

def generate_ground_truth_bbox_images(image_fp,image_bb_data):
    a = 0
    for i in image_fp:
        bb_true = image_bb_data[a]
        print(bb_true)
        test_img = Image.open(i)
        test_img_array = cv.imread(i)
        (h,w) = test_img_array.shape[:2]
        bb_true[0]=bb_true[0]*w
        bb_true[1]=bb_true[1]*h
        bb_true[2]=bb_true[2]*w
        bb_true[3]=bb_true[3]*h
        
        fig, ax = plt.subplots()
        ax.imshow(test_img)
        bb_true_rect = patches.Rectangle((bb_true[0],bb_true[1]),bb_true[2],bb_true[3], linewidth=2, edgecolor="#e7364b", facecolor="none")
        ax.add_patch(bb_true_rect)
        
        ax.legend("True_BB",loc="best")
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        plt.show()       #create ground truth.
        a = a+1
def train_stuff():
    
    l1 = tf.keras.regularizers.L1(l1=0.01)
    vgg_net = applications.VGG16(weights = "imagenet" , include_top = False, input_tensor = layers.Input(shape = (224,224,3)))
    #import vggnet
    vgg_net.trainable = False
    #make it untrainable
    flatten = vgg_net.output
    flatten = layers.Flatten()(flatten)
    bboxHead = layers.Dense(128, activation="relu",)(flatten)
    bboxHead = layers.Dropout(0.2)(bboxHead)
    bboxHead = layers.Dense(64, activation="relu")(bboxHead)
    bboxHead = layers.Dropout(0.2)(bboxHead)
    bboxHead = layers.Dense(64, activation="relu")(bboxHead)
    # bboxHead = layers.BatchNormalization()(bboxHead)
    bboxHead = layers.Dense(32, activation="relu",kernel_regularizer=l1)(bboxHead)
    bboxHead = layers.Dense(4, activation="sigmoid",name="bounding_box")(bboxHead)
    
    softmaxHead = layers.Dense(512, activation="relu")(flatten)
    softmaxHead = layers.Dropout(0.2)(softmaxHead)
    softmaxHead = layers.Dense(512, activation="relu")(softmaxHead)
    # softmaxHead = layers.Dropout(0.5)(softmaxHead)
    # softmaxHead = layers.Dense(64, activation="relu",kernel_regularizer=l1)(softmaxHead)
    softmaxHead = layers.Dropout(0.2)(softmaxHead)
    # softmaxHead = layers.BatchNormalization()(softmaxHead)
    softmaxHead = layers.Dense(5, activation="softmax",name="class_label")(softmaxHead)

    #make the model
    model = models.Model(inputs= vgg_net.input, outputs=(bboxHead,softmaxHead))
    losses = {"class_label":"categorical_crossentropy","bounding_box":"mean_squared_error"}
    lossWeights = {"class_label": 1.0,"bounding_box": 1.0}
    
    # #es callback stop 
    callback = [callbacks.EarlyStopping(patience=10, restore_best_weights=True)]
    model.compile(optimizer=optimizers.Adam(learning_rate=0.001),loss = losses,loss_weights = lossWeights,metrics = ["accuracy"])
    print(model.summary())
    print("STARTING TRAINING")
    t = time.process_time()
    history = model.fit(x_train, train_targets, epochs = 50, verbose = 1 , batch_size = 32,
                        validation_data = (y_train,valid_targets), 
              callbacks = callback,
              shuffle = True)
    
    elapsed_time=time.process_time() - t
    print(f"Finished Training in {elapsed_time} seconds") 
   
   
    class_acc = history.history["class_label_accuracy"]
    val_class_acc = history.history["val_class_label_accuracy"]
    class_loss = history.history["class_label_loss"]
    val_class_loss = history.history["val_class_label_loss"]
    bbox_loss = history.history["bounding_box_loss"]
    val_bbox_loss = history.history["val_bounding_box_loss"]
    epochs = range(1,len(class_acc)+1)
    

    #class loss plot
    plt.plot(epochs,class_loss,color = "#e7364b" ,linestyle = "--",linewidth=3,label="Training Class Label Loss") #loss data
    plt.plot(epochs,val_class_loss,color = "#364be7", linestyle = "-" ,linewidth=3,label="Validation Class Label Loss") #valid data
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, alpha=0.4)
    plt.xlabel("Epochs",fontdict = {"fontsize": 12}) #number of epochs
    plt.ylabel("Class Label Losses",fontdict = {"fontsize": 12}) #label the loss
    plt.title("Training|Validation Class_Label_Loss",fontdict = {"fontsize": 12})
    plt.legend(loc = "best") #adds legends to the plot
    plt.figure() #creates plot
    plt.show() #presents the plots to me. 
    
    
    #bbox loss plot
    plt.plot(epochs,bbox_loss,color = "#896799" ,linestyle = "--",linewidth=3,label="Training Bounding Box Loss") #loss data
    plt.plot(epochs,val_bbox_loss,color = "#779967", linestyle = "-" ,linewidth=3,label="Validation Bounding Box Loss") #valid data
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, alpha=0.4)
    plt.xlabel("Epochs",fontdict = {"fontsize": 12}) #number of epochs
    plt.ylabel("BBox Losses",fontdict = {"fontsize": 12}) #label the loss
    plt.title("Training|Validation Bounding_Box_Loss",fontdict = {"fontsize": 12})
    plt.legend(loc = "best") #adds legends to the plot
    plt.figure() #creates plot
    plt.show() #presents the plots to me. 
    
    #class accuracy plot
    plt.plot(epochs,class_acc,color = "#36fc79",linestyle = "--",linewidth=3,label="Training Class Label Accuracy") #plots the acc
    plt.plot(epochs,val_class_acc,color = "#fc36b9",linestyle = "-",linewidth=3,label="Validation Class Label Accuracy") #plots the validation acc
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, alpha=0.4)
    plt.xlabel("Epochs",fontdict = {"fontsize": 12}) #number of epochs
    plt.ylabel("Class Label Accuracy",fontdict = {"fontsize": 12}) #label the accuracy
    plt.title("Training|Validation Class Accuracy",fontdict = {"fontsize": 12})
    plt.legend(loc = "best") #adds the legends to the plot
    plt.figure()  #creates the plot
    plt.show()
    
    model.save("weight.h5")


def prediction_creation(classlbl,imgfp,model):
    model = tf.keras.models.load_model(model)
    #model.summary()
    for i in imgfp:
        image = utils.load_img(i,target_size=(224,224))
        image = utils.img_to_array(image)/255.0
        image = np.expand_dims(image,axis=0)
        (box_pred,label_pred)= model.predict(image)
        (x,y,w,h) = box_pred[0]
        a = np.argmax(label_pred,axis=1)
        label = classlbl.classes_[a][0]
        text = "{}: {:.8f}".format(label,np.max(label_pred))
        t_size = cv.getTextSize(text, 0, font_size, font_thickness)[0]
        image = cv.imread(i)
        image = imutils.resize(image,width = 600)
        (image_height,image_width)= image.shape[:2]
        x = int(x * image_width)
        y = int(y * image_height)
        w = int(w * image_width)
        h = int(h * image_height)
        cv.rectangle(image,(x-1,y),(x + t_size[0], y-t_size[1]-3),colour,-1)
        cv.rectangle(image,(x,y),(w,h),colour,2)
        cv.putText(image,text,(x,y-3),cv.FONT_HERSHEY_SIMPLEX,0.65,(0,0,0),2)
        cv.imshow("output",image)
        cv.waitKey(0)
        cv.destroyAllWindows()
        break
    
def prediction_custom_input(classlbl,inputimage,model):
    model = tf.keras.models.load_model(model)
    #model.summary()
    i = inputimage
    image = utils.load_img(i,target_size=(224,224))
    image = utils.img_to_array(image)/255.0
    image = np.expand_dims(image,axis=0)
    (box_pred,label_pred)= model.predict(image)
    (x,y,w,h) = box_pred[0]
    a = np.argmax(label_pred,axis=1)
    label = classlbl.classes_[a][0]
    text = "{}: {:.8f}".format(label,np.max(label_pred))
    t_size = cv.getTextSize(text, 0, font_size, font_thickness)[0]
    image = cv.imread(i)
    # image = imutils.resize(image,width = 600)
    (image_height,image_width)= image.shape[:2]
    x = int(x * image_width)
    y = int(y * image_height)
    w = int(w * image_width)
    h = int(h * image_height)
    cv.rectangle(image,(x-1,y),(x + t_size[0], y-t_size[1]-3),colour,-1)
    cv.rectangle(image,(x,y),(w,h),colour,2)
    cv.putText(image,text,(x,y-3),cv.FONT_HERSHEY_SIMPLEX,0.65,(0,0,0),2)
    cv.imshow("output",image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
def prediction_loop_filepath(classlbl,fruit,filepath,model):

    model = tf.keras.models.load_model(model)
    test_fp = []
    test_directory = os.fsencode(filepath)
    for file in os.listdir(test_directory):
        filename = os.fsdecode(file)
        path_test = filepath + "/" + filename
        test_fp.append(path_test)
        
    images_test = []
    for i in test_fp:
        image = utils.load_img(i,target_size=(224,224))
        # cv.imshow("output",image)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        image = utils.img_to_array(image)/255.0
        image = np.expand_dims(image,axis=0)
     
        (box_pred,label_pred)= model.predict(image)
        print(box_pred)
        (x,y,w,h) = box_pred[0]
        a = np.argmax(label_pred,axis=1)
        label = classlbl.classes_[a][0]
        text = "{}: {:.8f}".format(label,np.max(label_pred))
        t_size = cv.getTextSize(text, 0, font_size, font_thickness)[0]
        image = cv.imread(i)
        image = imutils.resize(image,width = 600)
        (image_height,image_width)= image.shape[:2]
        x = int(x * image_width)
        y = int(y * image_height)
        w = int(w * image_width)
        h = int(h * image_height)
        cv.rectangle(image,(x-1,y),(x + t_size[0], y-t_size[1]-3),colour,-1)
        cv.rectangle(image,(x,y),(w,h),colour,2)
        cv.putText(image,text,(x,y-3),cv.FONT_HERSHEY_SIMPLEX,0.65,(0,0,0),2)
        cv.imshow("output",image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    
def prediction_loop_filepath_saver(fruit_type,light,path,env,model,classlbl,filepath):

    y_pred_exp_class = []
    y_pred_exp_bbox = []
    y_pred_exp_class_scores = []
    model = tf.keras.models.load_model(model)
    test_fp = []
    filepath = filepath + path +"\\"+ light + "\\" + fruit_type.capitalize()
    test_directory = os.fsencode(filepath)
    for file in os.listdir(test_directory):
        filename = os.fsdecode(file)
        path_test = filepath + "/" + filename
        test_fp.append(path_test)
        
    images_test = []
    number = 0.5
    for i in test_fp:
        image = utils.load_img(i,target_size=(224,224))
        image = utils.img_to_array(image)/255.0
        image = np.expand_dims(image,axis=0)

        (box_pred,label_pred)= model.predict(image)
        # print(box_pred)
        y_pred_exp_bbox.append(box_pred)
        (x,y,w,h) = box_pred[0]
        a = np.argmax(label_pred,axis=1)
        label = classlbl.classes_[a][0]
        text = "{}: {:.8f}".format(label,np.max(label_pred))
        y_pred_exp_class.append(label)
        y_pred_exp_class_scores.append(np.max(label_pred))
        
        t_size = cv.getTextSize(text, 0, font_size, font_thickness)[0]
        image = cv.imread(i)
        image = imutils.resize(image,width = 600)
        (image_height,image_width)= image.shape[:2]
        x = int(x * image_width)
        y = int(y * image_height)
        w = int(w * image_width)
        h = int(h * image_height)
        cv.rectangle(image,(x-1,y),(x + t_size[0], y-t_size[1]-3),colour,-1)
        cv.rectangle(image,(x,y),(w,h),colour,2)
        cv.putText(image,text,(x,y-3),cv.FONT_HERSHEY_SIMPLEX,0.65,(0,0,0),2)
        savefp = ("F:\Cranfield\IRP\DataCollect\PostProcessing\\"
                  +env+"\\"+light+"\\"+fruit_type.capitalize()+"\\"+str(number)+".png") #no (s)
        print(savefp)
        # awubdauowdb.ahdihas()
        number = number + 0.5
        cv.imwrite(savefp,image)
    return y_pred_exp_class,y_pred_exp_bbox,y_pred_exp_class_scores
        
def iou_calc(box1,box2):
    x1 = max(box1[0],box2[0])
    y1 = max(box1[1],box2[1])
    x2 = min(box1[2],box2[2])
    y2 = min(box1[3],box2[3])
    area_of_int = max(0,x2 - x1 + 1) * max(0,y2 - y1 + 1)
    bbox1area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    bbox2area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)
    iouscore = area_of_int / float(bbox1area + bbox2area - area_of_int)
    return iouscore #creates iou score based on bboxs.       

def predict_creation_with_iou_calc(bboxgt,imgfp,classlbl,model,label_data):
        model = tf.keras.models.load_model(model)
        #model.summary()
        a = 0
        for i in test_imgpath:
            image = utils.load_img(i,target_size=(224,224))
            image = utils.img_to_array(image)/255.0
            image = np.expand_dims(image,axis=0)
            (xt,yt,wt,ht) = bboxgt[a]
            (box_pred,label_pred)= model.predict(image)
            (xp,yp,wp,hp) = box_pred[0]
            a = np.argmax(label_pred,axis=1)
            label = label_data.classes_[a][0]
            text = "{}: {:.8f}".format(label,np.max(label_pred))
            t_size = cv.getTextSize(text, 0, font_size, font_thickness)[0]
            image = cv.imread(i)
            image = imutils.resize(image,width = 600)
            (image_height,image_width)= image.shape[:2]
           
            box_gtr = [xt,yt,xt+wt,yt+ht] 
            box_ptr = [xp,yp,xp+wt,yp+hp]
            iouscore = iou_calc(box_gtr,box_ptr)
            iousct = ("IOU Score:" + "{:.9f}".format(iouscore))
            #get prediction bbox
            xp = int(xp * image_width)
            yp = int(yp * image_height)
            wp = int(wp * image_width)
            hp = int(hp * image_height)
            #get true bbox
            xt = int(xt * image_width)
            yt = int(yt * image_height)
            wt = int(wt * image_width)
            ht = int(ht * image_height)
            

            #start image writing.
            cv.rectangle(image,(xp-1,yp),(xp + t_size[0], yp-t_size[1]-3),colour,-1)
            cv.rectangle(image,(xp,yp),(wp,hp),colour,2)
            cv.rectangle(image,(xt,yt),(wt,ht),(75, 54, 231),2)
            cv.putText(image,iousct,(xp+100,yp+400),cv.FONT_HERSHEY_SIMPLEX,0.65,(0,0,0),2)
            cv.putText(image,text,(xp,yp-3),cv.FONT_HERSHEY_SIMPLEX,0.65,(0,0,0),2)
            cv.imshow("output",image)
            cv.waitKey(0)
            cv.destroyAllWindows()
            break
 
    
def confusion_matrix_creator(model,testimgpath,testbbgt,testclass,classlbl,dataframe):
    model = tf.keras.models.load_model(model)
    a = 0
    p = 0
    tot_bb = []
    y_pred = []
    y_pred_truth = []
    avgiou = []
    
    tstcl = dataframe[3].to_numpy() #label dataframe
    tstcl.astype("str") 
    for i in tstcl:
       y_pred_truth.append(i)
    
    for i in test_imgpath:
        image = utils.load_img(i,target_size=(224,224))
        image = utils.img_to_array(image)/255.0
        image = np.expand_dims(image,axis=0)
        (box_pred,label_pred) = model.predict(image)
        tot_bb.append(box_pred)
        
        a = np.argmax(label_pred,axis=1)
        label_conv = str(classlbl.classes_[a][0])
        y_pred.append(label_conv)
        
        (xt,yt,wt,ht) = testbbgt[p] #test_bbox
        box_gtr = [xt,yt,xt+wt,yt+ht]
        (xp,yp,wp,hp) = box_pred[0]
        box_ptr = [xp,yp,xp+wt,yp+hp]
        p = p+1
        vals = iou_calc(box_gtr,box_ptr)
        avgiou.append(vals)
        
    classreport = (sklearn.metrics.classification_report(y_pred_truth, y_pred))  
    #f1 score chosen as it it much better to get an understanding of imbalanced classification (the number of items are not the same)
    print(classreport)
    print("MCC:", sklearn.metrics.matthews_corrcoef(y_pred_truth, y_pred))
    cm = sklearn.metrics.confusion_matrix(y_pred_truth,y_pred)#,labels=classlbl.classes_)
    cm_df = pd.DataFrame(cm,index=["orange","apple","banana","broccoli","tomato"],columns=["orange","apple","banana","broccoli","tomato"])
    fig,ax1 = plt.subplots(figsize=(15,8))
    ax1 = sns.heatmap(cm_df,annot=True,fmt='d',ax=ax1,cmap ="coolwarm")
    ax1.set_xlabel("Predicted",fontdict = {"fontsize": 16})
    ax1.set_ylabel("True",fontdict = {"fontsize": 16})
    title = "Confusion Matrix + Avg IOU:" + str(np.average(avgiou))
    ax1.set_title(title,fontdict = {"fontsize": 16})
    
def confusion_matrix_creator_exp(model,y_pred_experiment_class,y_pred_experiment_bbox,y_pred_experiment_class_scores,fpd,bb_fp_head):
    model = tf.keras.models.load_model(model)
    a = 0
    p = 0
    # tot_bb = []
    y_pred = []
    y_truth_experiment_class = []
    y_truth_experiment_bbox = []
    avgiou = []
    fp = (fpd + bb_fp_head + "bboxdata.csv" )
    truths = readcsv(fp)
    
    impdf = truths[5].to_numpy(dtype="unicode")
    imgpath_tr = []
    for i in impdf:
        imgpath_tr.append(fpd+bb_fp_head+i)
        
    truth_images = image2array(imgpath_tr)
    y_truth_experiment_bbox,y_truth_experiment_class_lb,label_data_truth = getgroundtruths(truths,imgpath_tr,True)
    
    trcl = truths[0].to_numpy()
    trcl.astype("str") 
    for i in trcl:
        y_truth_experiment_class.append(i)
 
    
    for i in imgpath_tr:
        image = utils.load_img(i,target_size=(224,224))
        image = utils.img_to_array(image)/255.0
        image = np.expand_dims(image,axis=0)
    
 
        
        (xt,yt,wt,ht) = y_truth_experiment_bbox[p]
        box_gtr = [xt,yt,xt+wt,yt+ht]
        bboxdata = y_pred_experiment_bbox[p]
        (xp,yp,wp,hp) = bboxdata[0]
        box_ptr = [xp,yp,xp+wt,yp+hp]
        p = p+1
        vals = iou_calc(box_gtr,box_ptr)
        avgiou.append(vals)

        
    lbcm = LabelBinarizer()#neg_label = 1,pos_label = 0)
    y_pred_experiment_class_lb = lbcm.fit_transform(y_pred_experiment_class)
    test = [1,1,1,1,1,1]
    

    print("------")
    print(bb_fp_head)
    print("Accuracy:",sklearn.metrics.accuracy_score(y_truth_experiment_class,y_pred_experiment_class))
    print("Precision:",sklearn.metrics.precision_score(y_truth_experiment_class, y_pred_experiment_class,pos_label=y_truth_experiment_class[0]))
    print("Recall:",sklearn.metrics.recall_score(y_truth_experiment_class, y_pred_experiment_class,pos_label=y_truth_experiment_class[0]))
    print("F1-Score:",sklearn.metrics.f1_score(y_truth_experiment_class, y_pred_experiment_class,pos_label=y_truth_experiment_class[0]))
    print("MCC:", sklearn.metrics.matthews_corrcoef(y_truth_experiment_class, y_pred_experiment_class))#,pos_label=y_truth_experiment_class[0]))
    print("Ap:",sklearn.metrics.average_precision_score(y_pred_experiment_class_lb, y_pred_experiment_class_scores))
    print("iou:")
    lel = 0.5
    for i in range(6):
 
        # print("ious "+str(lel)+": ",avgiou[i])
        print(avgiou[i])
        lel += 0.5
    cm = sklearn.metrics.confusion_matrix(y_truth_experiment_class, y_pred_experiment_class)#,labels=classlbl.classes_)
    cm_df = pd.DataFrame(cm,index=lbcm.classes_,columns=lbcm.classes_)
    fig,ax1 = plt.subplots(figsize=(15,8))
    ax1 = sns.heatmap(cm_df,annot=True,fmt='d',ax=ax1,cmap ="coolwarm")
    ax1.set_xlabel("Predicted",fontdict = {"fontsize": 16})
    ax1.set_ylabel("True",fontdict = {"fontsize": 16})
    badb = bb_fp_head.split("\\")
    # print(badb)
    title = "Confusion Matrix: Fruit: " + str(badb[2]) + " Light Intensity: " + str(badb[1])
    ax1.set_title(title,fontdict = {"fontsize": 16}) 
    


#Global Parameters :- Start;
font_size = 0.7
font_thickness = 2
colour = (30,199,43)
#Global Parameters :- End;

# train_data = readcsv("F:\Cranfield\IRP\Datasets\Second\\trainingdata.csv")
# valid_data = readcsv("F:\Cranfield\IRP\Datasets\Second\\validationdata.csv")
test_data = readcsv("F:\Cranfield\IRP\Datasets\Second\\testdata.csv")
# train_imgpath = getimagepaths(train_data,"\\train\\") 
# valid_imgpath = getimagepaths(valid_data,"\\valid\\")
test_imgpath = getimagepaths(test_data,"\\test\\")

# train_images = image2array(train_imgpath)
# valid_images = image2array(valid_imgpath)
test_images = image2array(test_imgpath)
# train_bbox,train_cl,label_data_train = getgroundtruths(train_data,train_imgpath,False)
# valid_bbox,valid_cl,label_data_valid = getgroundtruths(valid_data,valid_imgpath,False)
test_bbox,test_cl,label_data_test = getgroundtruths(test_data,test_imgpath,False)
print(label_data_test.classes_)
# 
# x_test = np.array(train_bbox)q

# train_targets = {"class_label" : train_cl,"bounding_box":np.array(train_bbox)}
# valid_targets = {"class_label": valid_cl, "bounding_box":np.array(valid_bbox)}
test_targets = {"class_label" : test_cl,"bounding_box":np.array(test_bbox)}

# x_train = np.array(train_images[0:1845])
# y_train = np.array(valid_images[0:448]) 
# train_stuff()

prediction_custom_input(label_data_test,"F:\Cranfield\IRP\\multitest.jpg","weight.h5")


model_test = "weight.h5"
prefp = "F:\Cranfield\IRP\DataCollect\\"
path = "SimulationSecondWind"
realpath = "Realworld1080\Augment"
sim = "Simulation"
real = "Realworld"
fprl = "F:\Cranfield\IRP\DataCompile\Realworld\\"
fpsim = "F:/Cranfield/IRP/DataCompile/Simulation\\"

                 
#x_train data ^
#y_train bbdox data and classes
#x test data for test images
#y test bbox data and classes
