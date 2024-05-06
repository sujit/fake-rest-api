# Fake REST API Runner

Generate a few fake CSV entries and run a REST API against the generated data.


### Generate 10K fake (CSV) entries
-----------------

```sh
fake -f csv -n 10000 pyint,user_name,mac_address,job,company,ssn > input.csv
```


### Run server indefinitely
-----------------

```bash
nohup python app.py > nohup.out 2>&1 &
```

### Test API
-----------------

```bash
curl http://<ip>:8080/random/test
curl http://<ip>:8080/random/junk
```


## References

* [faker-cli (Python)](https://github.com/dacort/faker-cli/tree/main)
* [fakedata - Standalone binary](https://github.com/lucapette/fakedata)
* [Faker (Python - quite popular)](https://github.com/joke2k/faker)
