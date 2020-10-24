# Convert TensorFlow Checkpoint to Frozen pb.
a high level code for users to convert tensorflow checkpoint file to frozen protobuff file.

## requirements
tensorflow

## usage
use 
`python3 view_ckpt_graph.py` to get output nodes' name of checkpoint model.

modify line 19 in ckpt2pb.py to match the output nodes' name of checkpoint model you get via view_ckpt_graph.py.

use `python3 view_pb_graph.py` to check the converted model.
