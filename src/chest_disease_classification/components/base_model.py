from chest_disease_classification import logger
from chest_disease_classification.config_class import BaseModelConfig
import tensorflow as tf
from pathlib import Path







class BaseModel:
    def __init__(self, config: BaseModelConfig):
        self.config = config
        self.model = None

    @staticmethod
    def save_model(path:Path, model = tf.keras.Model):
        model.save(path)

    def get_base_model(self):
        self.model = tf.keras.applications.VGG16(
                        include_top = self.config.include_top,
                        weights = self.config.weights,
                        input_shape = self.config.image_size,
                    )
        self.save_model(path = self.config.base_model_dir, model = self.model)

    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units = classes,
            activation = "softmax"
            )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
        )

        full_model.compile(
            optimizer = tf.keras.optimizers.SGD(learning_rate = learning_rate),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ["accuracy"]
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        if self.model == None:
            raise ValueError("Base model has not been created. Call get_base_model() first")
        full_model = self.prepare_full_model(
            model = self.model,
            classes = self.config.classes, 
            freeze_all = True, 
            freeze_till = None, 
            learning_rate = self.config.learning_rate
            )
        
        self.save_model(path = self.config.updated_base_model_dir, model = full_model)


        