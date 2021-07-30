# PyFlink LightGBM

Setup.

```sh
$ conda env create -f environment.yaml
$ brew install lightgbm
```

Reference https://github.com/microsoft/LightGBM/blob/bc9d34e4e651b5744b29a556a2e9d2301707e35b/examples/python-guide/simple_example.py


Train. This will produce a trained model and save it as model.txt.

```sh
python train.py
```

Infer with vanilla Python.

```sh
python vanilla_infer.py
```

Infer with PyFlink.

```sh
python pyflink_infer.py
```
