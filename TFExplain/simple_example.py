import tensorflow as tf
import matplotlib.pyplot as plt

from tf_explain.core.smoothgrad import SmoothGrad

IMAGE_PATH = '../images/cat.jpg'

if __name__ == '__main__':
    model = tf.keras.applications.vgg16.VGG16(weights='imagenet', include_top=True)

    image = tf.keras.preprocessing.image.load_img(IMAGE_PATH, target_size=(224, 224))
    img = tf.keras.preprocessing.image.img_to_array(image)

    model.summary()
    data = ([img], None)

    tabby_cat_class_index = 281
    explainer = SmoothGrad()
    # Compute SmoothGrad on VGG16
    grid = explainer.explain(data, model, tabby_cat_class_index, 20, 1.)

    # Save result
    explainer.save(grid, '.', 'smoothgrad.png')

    # Plot result
    fig, ax = plt.subplots(1, 2, figsize=(16, 10))
    ax[0].imshow(image)
    ax[1].imshow(grid, cmap='gray', vmin=0, vmax=255)
    plt.show()
    