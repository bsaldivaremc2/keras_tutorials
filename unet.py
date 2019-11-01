import numpy as np
import tensorflow as tf
import keras
import numpy as np
import tensorflow as tf
import keras

from keras.layers import *
from keras.models import *
from keras.optimizers import Adam,Adadelta

def get_name(prefix,layer_counter,scope="CNN"):
    #If layer_counter does not exist create it
    counter = layer_counter.get(prefix,0)
    output = scope+"_"+prefix+"_"+str(counter)
    counter+=1
    layer_counter[prefix]=counter
    return output

def get_unet(input_size = (256,256,3),output_channels = 1,lr = 0.01,decay = 1e-6,model_name="Unet",layers_depth = [64,128,256,512,1024]):
    lc = {}
    inputs = Input(input_size,name="Input")
    x = inputs
    scope="CNN"
    layers = []
    layers_depth_up = layers_depth[:-1]
    layers_depth_up.reverse()
    for layer_depth in layers_depth:
        for _ in range(2):
            x = Conv2D(layer_depth,3,padding = 'same',kernel_initializer = 'he_normal',name=get_name("Conv",lc,scope=scope))(x)
            x = BatchNormalization(name=get_name("batch_norm",lc,scope=scope))(x)
            x = Activation('relu',name=get_name("relu",lc,scope=scope))(x)
            if _ == 1:
                layers.append(x)
        if layer_depth!=layers_depth[-1]:
            x = MaxPooling2D(pool_size=(2, 2),name=get_name("MaxPool",lc,scope=scope))(x)
    for i,layer_depth_up in enumerate(layers_depth_up):
        x = UpSampling2D(size = (2,2),name=get_name("Upsampling",lc,scope=scope))(x)
        x = Concatenate(axis = 3)([layers[-(i+2)],x])
        for _ in range(2):
            x = Conv2D(layer_depth_up,3,padding = 'same',kernel_initializer = 'he_normal',name=get_name("Conv",lc,scope=scope))(x)
            x = BatchNormalization(name=get_name("batch_norm",lc,scope=scope))(x)
            x = Activation('relu',name=get_name("relu",lc,scope=scope))(x)
    #Make output
    x = Conv2D(output_channels,3,padding = 'same',kernel_initializer = 'he_normal',name=get_name("Conv",lc,scope=scope))(x)
    x = BatchNormalization(name=get_name("batch_norm",lc,scope=scope))(x)
    x = Activation('sigmoid',name="Output")(x)
    model = Model(inputs=inputs,outputs=x,name=model_name)
    optimizer=Adadelta(lr=lr, rho=0.95, epsilon=None, decay=decay)
    model.compile(optimizer=optimizer,loss = 'binary_crossentropy', metrics = ['accuracy'])
    return model



unet = get_unet(input_size = (96,96,1),output_channels = 15,lr = 0.01,decay = 1e-6,model_name="Unet",layers_depth = [64,128,256,512,1024])
