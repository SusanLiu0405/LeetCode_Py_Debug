import numpy as np
import dask.array as da

chunk_size = (10, 10)
arr_size = (100, 100)
da4 = da.random.randint(1, 10, size = arr_size, chunks=chunk_size)
print(da4.compute())
print(da4.chunksize[0])