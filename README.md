# data-engineering-common

This is a library of common functionality used by data engineering microservices.

### Running tests locally

After setting up a python 3 virtualenv and activating it:
```console
$ python setup.py develop
$ cp sample.env .env
$ USE_DOTENV=1 py.test
```

### Issues with pyscopg2 on MacOS

When running `python setup.py develop` you may encounter an error related to openssl. If this is the case, it can be resolved by running the following commands first:

```console
$ brew install openssl
$ export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
$ export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"
```