import sir3d
import numpy as np

#iterator = sir3d.Iterator(use_mpi=False)

iterator = sir3d.Iterator(use_mpi=True, batch=256)

mod = sir3d.Model('rempel.ini', rank=iterator.get_rank())
iterator.use_model(model=mod)

#iterator.run_all_pixels(rangex=[0,100], rangey=[0,100])
iterator.run_all_pixels()