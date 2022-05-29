#train the data if you have updated intents file

from preprocessData import training, output
from Mmodel import create_model

model = create_model()
model.fit(training, output, n_epoch=1000, batch_size=9, show_metric=True)
model.save("model.tflearn")


