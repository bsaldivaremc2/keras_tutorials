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
  
