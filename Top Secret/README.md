### Environment

```
python3 -m venv ./env
pip3 install -r requirements.txt
```

`topsecret/.env`
```
[APP]
SECRET_KEY=yoursecretkey

[DB]
DB_URL = mysql+pymysql://user:pass@localhost:3306/dbname