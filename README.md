# IPPT
> 👟 API to calculate IPPT scores

## 🤔 Usage

```
GET https://ippt.vercel.app/api?age=<age>&situps=<situp reps>&pushups=<pushup reps>&run=<run time>
```

where `run time` is the seconds taken to complete the 2.4 km run.

**Example:**

```bash
$ curl "https://ippt.vercel.app/api?age=18&situps=40&pushups=20&run=720"

{
  "age_group": 0,
  "pushups": {
    "next": 0,
    "score": 9
  },
  "run": {
    "next": 1,
    "score": 33
  },
  "situps": {
    "next": 3,
    "score": 20
  },
  "result": {
    "cash": 0,
    "min_score": 61,
    "name": "Pass",
    "subtitle": "NSMen incentive"
  },
  "total": 62
}
```

## ⚙️ Build setup
Fork or download the repository.

```bash
pipenv shell
python playground.py
```

### Testing
```
pipenv run pytest tests
```
