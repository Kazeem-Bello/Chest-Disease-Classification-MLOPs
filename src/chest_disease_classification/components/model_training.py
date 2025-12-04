from pathlib import Path
from chest_disease_classification.config_class import ModelTrainingConfig
import tensorflow as tf


class Model:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def get_base_model(self):
        model = tf.keras.models.load_model(self.config.updated_base_model_dir)
        model.compile(
            optimizer = tf.keras.optimizers.SGD(learning_rate = self.config.learning_rate),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ["accuracy"],
            run_eagerly=True,
        )

        return model
    
    def train_valid_generator(self):
        datagenerator_kwargs = dict( rescale = 1./255, validation_split = 0.2)

        data_flow_kwargs = dict(target_size = self.config.image_size[:-1], batch_size = self.config.batch_size, interpolation = "bilinear")
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "validation",
            shuffle = False,
            **data_flow_kwargs
        )

        if self.config.augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range = 40,
                horizontal_flip = True,
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                shear_range = 0.2,
                zoom_range = 0.2,
                **datagenerator_kwargs
            )

        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            shuffle = True,
            subset = "training",
            **data_flow_kwargs
        )
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size
        model = self.get_base_model()
        model.fit(
            self.train_generator,
            epochs = self.config.epoch,
            steps_per_epoch = self.steps_per_epoch,
            validation_steps = self.validation_steps,
            validation_data = self.valid_generator
        )

        self.save_model(path = self.config.model_dir, model = model)