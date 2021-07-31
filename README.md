# PyFlink LightGBM

Setup.

```sh
$ conda env create -f environment.yaml
$ conda activate pyflink-lightgbm
$ brew install lightgbm
```

Reference https://github.com/microsoft/LightGBM/blob/bc9d34e4e651b5744b29a556a2e9d2301707e35b/examples/python-guide/simple_example.py


Train. This will produce a trained model and save it as model.txt.

```sh
$ python train.py
```

Infer with vanilla Python.

```sh
$ python vanilla_infer.py
```

Infer with PyFlink.

```sh
$ # Spin up Flink locally
$ ~/softwares/flink-1.13.0/bin/start-cluster.sh
$ # Prepare resources needed for a PyFlink run
$ (cd /usr/local/anaconda3/envs/pyflink-lightgbm && zip -r - .) > pyenv.zip
$ zip archive.zip model.txt
$ # Submit to Flink cluster. Open http://localhost:8081/ to check
$ ~/softwares/flink-1.13.0/bin/flink run -d -pyexec pyflink-lightgbm/bin/python -pyarch archive.zip,pyenv.zip#pyflink-lightgbm -py pyflink_infer.py
```
