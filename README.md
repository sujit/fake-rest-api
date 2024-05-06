# fake-rest-api
Generate fake CSV and run a REST API for data rendering


## Generate 10K fake (CSV) entries

```sh
fake -f csv -n 10000 pyint,user_name,mac_address | sponge input.csv
```


## Run server in the background (after remote ssh terminal exit)

```bash
nohup python app.py > nohup.out 2>&1 &
```

## Fake data genetion tools

* [faker-cli (Python)](https://github.com/dacort/faker-cli/tree/main)
* [fakedata - Standalone binary](https://github.com/lucapette/fakedata)
