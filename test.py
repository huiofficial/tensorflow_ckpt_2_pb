import tensorflow as tf
import os
import tensorflow as tf
import os.path
import argparse
from tensorflow.python.framework import graph_util
checkpoint = tf.train.get_checkpoint_state("ckpt") #
input_checkpoint = checkpoint.model_checkpoint_path  # 得ckpt文件路径

saver = tf.train.import_meta_graph(input_checkpoint + '.meta',
                                   clear_devices=True)  # 得到图、clear_devices ：Whether or not to clear the device field for an `Operation` or `Tensor` during import.

graph = tf.get_default_graph()  # 获得默认的图
input_graph_def = graph.as_graph_def()
tensor_name_list = [tensor.op for tensor in tf.get_default_graph().as_graph_def().node]
for e in tensor_name_list:
    print(e)
