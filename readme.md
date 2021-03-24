# Places API

## Counts

```javascript
{
  cities: 128768,
  countries: 249,
  continents: 7,
  languages: 185
}
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
