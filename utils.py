def save_model(model,save_dir='./',name='keras_model'):
  json_string = model.to_json()
  prefix = save_dir+name
  json_model = prefix+'.json'
  model_weights_file = prefix+'_weights.h5'
  model.save_weights(model_weights_file)
  with open(json_model,'w') as f:
    f.write(json_string)
  print("Done. Model saved.")

def load_model(json_file,weights_file):
  with open(json_file,'r') as f:
    json_loaded_string = f.read()
  modelx = keras.models.model_from_json(json_loaded_string)
  modelx.load_weights(weights_file)
  return modelx
  
def get_gaussian_channels(inp,index,batch=True,
                          gaussian_args={'std':2,'resolution':100,'shape':(96,96)}
                          ):
    o = []
    for _ in range(inp.shape[1]//2):
      x,y = inp[index,_*2,],inp[index,_*2+1]
      if (x>0) and (y>0):
        row, col = y, x
        c = gaussian_point(row=row,col=col,**gaussian_args)
      else: 
        c = np.zeros((96,96))
      o.append(c.copy())
    o = np.dstack(o)
    if batch==True:
      o = np.expand_dims(o,0)
    return o.copy()
  
  def gaussian_2d(std,points):
  mean = 0
  start = mean - points/2
  end = mean + points/2
  sigma = std
  xs = np.linspace(start,end,points)
  exp = ((xs-mean)/sigma)**2
  xs = (1/(2*sigma*np.pi))*np.exp(-0.5*exp)
  x = np.expand_dims(xs,1)
  y = np.expand_dims(xs,0)
  xy = np.abs(np.dot(x,y))
  xy = xy + np.abs(xy.min())
  xy = xy/xy.max()
  return xy

def gaussian_point(std,row,col,resolution=100,shape=(50,50)):
  g = gaussian_2d(std,resolution)
  o = np.zeros(shape)
  r2 = resolution//2
  rs = row - r2
  re = row + r2
  cs = col - r2
  ce = col + r2
  dr = re - shape[0] 
  dc = ce - shape[1] 
  rsg, reg = abs(min(0,rs)), resolution - max(0,dr)
  csg, ceg = abs(min(0,cs)), resolution - max(0,dc)
  reg = max(reg,rsg+1)
  ceg = max(ceg,csg+1)
  gx = g[rsg:reg,csg:ceg]
  rso,reo = max(0,rs),min(shape[0],re)
  cso,ceo = max(0,cs),min(shape[1],ce)
  reo = max(reo,rso+1)
  ceo = max(ceo,cso+1)
  ox = o[rso:reo,cso:ceo]
  o[rso:reo,cso:ceo] = ox+gx
  return o.copy()


gp = gaussian_point(std=2,row=55,col=5,resolution=100,shape=(100,100))
