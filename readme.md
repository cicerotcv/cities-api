# Cities API

## Counts

```javascript
{
  cities: 128768,
  countries: 249,
  continents: 7,
  languages: 185
}
```

## Calling the API

### **Cities**

This endpoint returns a list of cities (see City model below)

- **URL**

  _/cities/_

- **Method:**

  _`GET`_

- **URL Params**

  **Required:**

  `query=[url encoded string]`

  **Optional:**

  `populate=[boolean]`

- **Data Params**

  `No needed`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:** `City[]`

- **Error Response:**

  - **Code:** 400 BAD REQUEST <br />
    **Content:** `{"error": "No query provided."}`

  OR

  - **Code:** 400 BAD REQUEST <br />
    **Content:** `{"error": "To many results. Consider being more specific.", "matches": [integer]}`

- **Sample Call:**

  ```bash
  curl -X GET "127.0.0.1:5000/cities/?query=sao+paulo&populate=false"
  ```

## Search `(search.py)`

```bash
# input
$ python ./search.py "sao paulo"
# output
[
    {
        "_id": "5fa0b349b20d4824443f6c89",
        "name": "São Paulo do Potengi",
        "lat": "-5.895",
        "lng": "-35.76278",
        "country": "5fa08226bea7a74c5c69abfa"
    },
    {
        "_id": "5fa0b349b20d4824443f6f2e",
        "name": "São Paulo",
        "lat": "-23.5475",
        "lng": "-46.63611",
        "country": "5fa08226bea7a74c5c69abfa"
    },
    {
        "_id": "5fa0b349b20d4824443f73c0",
        "name": "São Paulo de Olivença",
        "lat": "-3.37833",
        "lng": "-68.8725",
        "country": "5fa08226bea7a74c5c69abfa"
    }
]
Elapsed time: 0.9119657
```

## Examples (Schemas open to suggestions)

### City

```json
{
  "_id": "5fa0b349b20d4824443f6f2e",
  "name": "São Paulo",
  "lat": "-23.5475",
  "lng": "-46.63611",
  "country": "5fa08226bea7a74c5c69abfa"
}
```

### Country

```json
{
  "_id": "5fa08226bea7a74c5c69abfa",
  "currency": ["BRL"],
  "languages": ["5fa06fb848b4572eb409287b"],
  "name": "Brazil",
  "native": "Brasil",
  "phone": "55",
  "capital": "Brasília",
  "initials": "BR",
  "continent": "5fa07297a260950fb890031c"
}
```

### Continents

```json
{
  "_id": "5fa07297a260950fb890031c",
  "name": "South America",
  "initials": "SA"
}
```

### Languages

```json
{
  "_id": "5fa06fb848b4572eb409287b",
  "name": "Portuguese",
  "native": "Português",
  "initials": "pt"
}
```

## Can't find your city?

Feel free to send a PR whenever you want
