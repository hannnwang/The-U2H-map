import netCDF4 as nc
import numpy as np
import os
import pickle
datapath='./'
ncfilename='s10_LLC4320_2012031018.nc'
ncfile=os.path.join(datapath,ncfilename)
ncds=nc.Dataset(ncfile)

u=ncds['u'][:]
v=ncds['v'][:]
x1d=ncds['x'][:] #Unit: meter
y1d=ncds['y'][:]
x1d=x1d.data
y1d=y1d.data

hsWW3=ncds['hs'][:]

#unmask
hs_WW3=hsWW3.data
Hs_WW3=np.mean(hs_WW3[:,:])+1 #Compute the mean over the hs that is away from left boundary
hs_WW3=hs_WW3-Hs_WW3+1 #Perturbation SWH

u=u.data
v=v.data
hs_WW3=np.transpose(hs_WW3)
u=np.transpose(u)
v=np.transpose(v)

f = open('snapshot_uv.pckl', 'wb')
pickle.dump([x1d, y1d, u, v], f)
f.close()