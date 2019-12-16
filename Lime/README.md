# LIME (Local Interpretable Model-Agnostic Explanations)

ime,  Local Interpretable Model-Agnostic, is a local model interpretation technique using Local surrogate models to approximate the predictions of the underlying black-box model.

Local surrogate models are interpretable models like Linear Regression or a Decision Trees that are used to explain individual predictions of a black-box model.

Lime trains a surrogate model by generating a new data-set out of the datapoint of interest. The way it generates the data-set varies dependent on the type of data. Currently Lime supports text, image and tabular data.

## Installation

Lime can be installed using PIP:

```bash
pip install lime
```

Or by cloning the repository and running the setup.py file:
```bash
git clone https://github.com/marcotcr/lime
cd lime/
python setup.py install
```

## Examples

Lime can be used for many different applications. Below are some example use cases which you can use to get started.

